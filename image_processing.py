"""
AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
Image Processing, Validation, and Feature Extraction Module
Built with OpenCV and Pillow.
"""

import os

# Limit thread pool allocations to prevent Windows memory exhaustion and paging file errors
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import cv2
import numpy as np
from PIL import Image
import base64
import io

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    """Verifies that filename has an approved image extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_image_file(file_storage):
    """
    Validates file format and decodes image.
    Rejects non-image files and unsupported formats.
    Returns:
        tuple: (is_valid: bool, cv_image_bgr, pil_image, error_message: str)
    """
    if not file_storage or file_storage.filename == '':
        return False, None, None, "No image file was selected."

    if not allowed_file(file_storage.filename):
        return False, None, None, "Invalid file format. Only JPG, JPEG, and PNG images are accepted."

    try:
        file_bytes = file_storage.read()
        file_storage.seek(0)  # Reset pointer for subsequent reads
        
        # Verify with Pillow
        pil_img = Image.open(io.BytesIO(file_bytes))
        pil_img.verify()  # Ensure it is a genuine, uncorrupted image
        
        # Reopen for actual processing
        pil_img = Image.open(io.BytesIO(file_bytes))
        if pil_img.mode != 'RGB':
            pil_img = pil_img.convert('RGB')
            
        # Convert to OpenCV BGR
        np_arr = np.frombuffer(file_bytes, np.uint8)
        cv_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if cv_img is None:
            return False, None, None, "Unable to decode image data. The file may be corrupted."
            
        # Memory optimization: Downscale oversized images (>1200px) to prevent paging file exhaustion
        h, w = cv_img.shape[:2]
        if max(h, w) > 1200:
            scale = 1200.0 / max(h, w)
            new_w, new_h = int(w * scale), int(h * scale)
            cv_img = cv2.resize(cv_img, (new_w, new_h), interpolation=cv2.INTER_AREA)
            pil_img = pil_img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
        return True, cv_img, pil_img, ""
    except Exception as e:
        return False, None, None, f"File validation error: Non-image or corrupted file ({str(e)})."

def verify_concrete_suitability(img_bgr):
    """
    Checks whether the uploaded image is suitable for concrete surface inspection.
    Rejects non-concrete objects (people, animals, vehicles, furniture, food, solid screens).
    
    Returns:
        tuple: (is_suitable: bool, user_message: str, technical_reason: str, metrics: dict)
    """
    h, w = img_bgr.shape[:2]
    if h < 60 or w < 60:
        return (
            False,
            "Unable to verify concrete surface. Please upload a clear concrete surface image.",
            "Image dimensions are too small (<60px) for reliable structural defect assessment.",
            {"height": h, "width": w}
        )

    # Convert color spaces
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    s_chan = hsv[:, :, 1]
    
    # Texture & roughness metrics
    lap_var = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    edges = cv2.Canny(gray, 50, 150)
    edge_ratio = float(np.mean(edges > 0))
    mean_sat = float(np.mean(s_chan))
    vivid_sat_ratio = float(np.mean(s_chan > 130))

    metrics = {
        "dimensions": f"{w}x{h}",
        "laplacian_variance": round(lap_var, 2),
        "edge_ratio": round(edge_ratio, 4),
        "mean_saturation": round(mean_sat, 2),
        "vivid_saturation_ratio": round(vivid_sat_ratio, 4)
    }

    # 1. Reject isolated object on solid/white/black background (product shots, food, furniture)
    flat_mask = (s_chan < 20) & ((gray > 240) | (gray < 15))
    flat_ratio = float(np.mean(flat_mask))
    metrics["flat_background_ratio"] = round(flat_ratio, 4)
    if flat_ratio > 0.22:
        return (
            False,
            "Unable to verify concrete surface. Please upload a clear concrete surface image.",
            "Isolated object on uniform/studio background detected rather than continuous in-situ concrete.",
            metrics
        )

    # 2. Reject vivid non-concrete colors (vehicles, food, bright furniture, clothing, flowers)
    # If the surface is smooth (<300 lap_var) and has high saturation -> non-concrete
    # If it is coarse aggregate/gravel (>300 lap_var), allow earthy stone hues
    if lap_var < 300:
        if mean_sat > 80 or vivid_sat_ratio > 0.15:
            return (
                False,
                "Unable to verify concrete surface. Please upload a clear concrete surface image.",
                "Vivid non-concrete colors detected. Vehicles, food, furniture, or clothing are not concrete surfaces.",
                metrics
            )
    else:
        if mean_sat > 105 or vivid_sat_ratio > 0.45:
            return (
                False,
                "Unable to verify concrete surface. Please upload a clear concrete surface image.",
                "Abnormally high saturation for concrete materials detected.",
                metrics
            )

    # 3. Reject human subjects / skin portraits (people, selfies, arms)
    ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
    _, cr, cb = cv2.split(ycrcb)
    skin_cand = (cr >= 135) & (cr <= 170) & (cb >= 85) & (cb <= 125) & (s_chan > 35) & (s_chan < 160)
    skin_ratio = float(np.mean(skin_cand))
    metrics["skin_tone_ratio"] = round(skin_ratio, 4)
    # Skin is smooth (low edge ratio), whereas gravel/concrete has high edge roughness
    if skin_ratio > 0.32 and edge_ratio < 0.10:
        return (
            False,
            "Unable to verify concrete surface. Please upload a clear concrete surface image.",
            "Human subject or skin tone detected. Please upload an image of a concrete structural element.",
            metrics
        )

    # 4. Reject flat uniform images (blank paper, blank wall, computer screen, blur)
    if lap_var < 12.0 and edge_ratio < 0.01:
        return (
            False,
            "Unable to verify concrete surface. Please upload a clear concrete surface image.",
            "Surface is excessively smooth or blurry and lacks concrete aggregate texture.",
            metrics
        )

    return (
        True,
        "Concrete surface verified for structural defect inspection.",
        "Passed colorimetric, texture variance, and concrete suitability criteria.",
        metrics
    )

def generate_inspection_overlay(img_bgr):
    """
    Generates an OpenCV inspection overlay highlighting edges, cavities, and surface contours.
    Returns:
        tuple: (overlay_base64_str, cv_stats: dict)
    """
    h, w = img_bgr.shape[:2]
    scale = min(800 / max(h, w), 1.0)
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(img_bgr, (new_w, new_h), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 1. Edge detection for crack profiling
    edges = cv2.Canny(blurred, 40, 130)
    
    # 2. Dark cavity / void detection
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 6
    )
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    overlay = resized.copy()
    
    # Highlight edges in vibrant amber
    edge_bgr = np.zeros_like(resized)
    edge_bgr[edges > 0] = [245, 158, 11] # Safety amber
    overlay = cv2.addWeighted(overlay, 0.75, edge_bgr, 0.65, 0)
    
    # Draw significant void/cavity boundaries in crimson
    void_count = 0
    total_void_area = 0
    for c in contours:
        area = cv2.contourArea(c)
        if 15 < area < 4000:
            void_count += 1
            total_void_area += area
            cv2.drawContours(overlay, [c], -1, (30, 30, 230), 1)

    _, buffer = cv2.imencode('.jpg', overlay, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
    overlay_b64 = base64.b64encode(buffer).decode('utf-8')

    cv_stats = {
        "edge_pixel_ratio": round(float(np.mean(edges > 0)), 4),
        "detected_cavities": void_count,
        "cavity_area_ratio": round(float(total_void_area / (new_w * new_h)), 4),
        "mean_surface_brightness": round(float(np.mean(gray)), 2)
    }

    return f"data:image/jpeg;base64,{overlay_b64}", cv_stats
