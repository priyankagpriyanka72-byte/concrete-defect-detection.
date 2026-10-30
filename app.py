"""
AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
Flask Backend Application
Supports 6 Defect Categories:
1. Segregation
2. Honeycombing
3. Spalling
4. Crack
5. Void
6. Efflorescence
+ Normal Concrete Validation & Advisory
+ 7-Step RCC Slab Strengthening Module
"""

import os

# Limit thread pool allocations to prevent Windows memory exhaustion and paging file errors
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import json
import base64
import io
import cv2
import numpy as np
from PIL import Image
from flask import Flask, render_template, request, jsonify, send_from_directory

import image_processing as ip
from model.classifier import classifier
from knowledge_base import (
    DEFECT_ADVISORY, 
    RCC_SLAB_STRENGTHENING_STEPS, 
    MANDATORY_STRUCTURAL_NOTE, 
    CASE_STUDY_CLARIFICATION
)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25 MB max upload

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
SAMPLES_DIR = os.path.join(STATIC_DIR, 'images', 'samples')
META_PATH = os.path.join(BASE_DIR, 'model', 'model_metadata.json')

def load_app_metadata():
    if os.path.exists(META_PATH):
        try:
            with open(META_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "model_name": "Concrete Defect Multi-Class Classifier",
        "classes": classifier.classes,
        "total_images": 326,
        "test_accuracy_pct": 79.59,
        "is_genuine_model": classifier.is_loaded
    }

APP_METADATA = load_app_metadata()

@app.route('/')
def index():
    """Renders the primary application dashboard."""
    return render_template(
        'index.html',
        metadata=APP_METADATA,
        classes=classifier.classes,
        rcc_steps=RCC_SLAB_STRENGTHENING_STEPS,
        structural_note=MANDATORY_STRUCTURAL_NOTE,
        case_study_note=CASE_STUDY_CLARIFICATION
    )

@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Primary image inspection and classification endpoint.
    Performs:
    1. File validation (JPG, JPEG, PNG only).
    2. Concrete suitability check (rejects unrelated objects: people, animals, vehicles, food, furniture).
    3. OpenCV inspection overlay generation.
    4. Normal concrete / no-defect validation.
    5. Multi-class model classification with genuine confidence scores.
    6. Retrieval of causes, prevention, repair, and slab strengthening advisory.
    """
    img_bgr = None
    original_b64 = None

    # Check for direct file upload or camera capture / base64 payload
    if 'image' in request.files:
        file = request.files['image']
        is_valid, cv_img, pil_img, err_msg = ip.validate_image_file(file)
        if not is_valid:
            return jsonify({
                "status": "error",
                "message": err_msg,
                "error_type": "file_validation_error"
            }), 400
        img_bgr = cv_img
        
        # Prepare base64 for frontend display
        buffered = io.BytesIO()
        pil_img.save(buffered, format="JPEG", quality=85)
        original_b64 = f"data:image/jpeg;base64,{base64.b64encode(buffered.getvalue()).decode('utf-8')}"
        
    elif request.is_json and 'image_base64' in request.json:
        data_uri = request.json['image_base64']
        try:
            if ',' in data_uri:
                header, encoded = data_uri.split(',', 1)
            else:
                encoded = data_uri
            file_bytes = base64.b64decode(encoded)
            pil_img = Image.open(io.BytesIO(file_bytes))
            if pil_img.mode != 'RGB':
                pil_img = pil_img.convert('RGB')
            np_arr = np.array(pil_img)
            img_bgr = cv2.cvtColor(np_arr, cv2.COLOR_RGB2BGR)
            original_b64 = data_uri if data_uri.startswith('data:') else f"data:image/jpeg;base64,{encoded}"
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Failed to parse base64 image data: {str(e)}",
                "error_type": "decoding_error"
            }), 400
    elif 'sample_name' in request.form or (request.is_json and 'sample_name' in request.json):
        sample_name = request.form.get('sample_name') or request.json.get('sample_name')
        sample_path = os.path.join(SAMPLES_DIR, os.path.basename(sample_name))
        if not os.path.exists(sample_path):
            return jsonify({
                "status": "error",
                "message": f"Sample image '{sample_name}' not found.",
                "error_type": "sample_not_found"
            }), 404
        img_bgr = cv2.imread(sample_path)
        pil_img = Image.open(sample_path)
        buffered = io.BytesIO()
        pil_img.save(buffered, format="JPEG", quality=85)
        original_b64 = f"data:image/jpeg;base64,{base64.b64encode(buffered.getvalue()).decode('utf-8')}"
    else:
        return jsonify({
            "status": "error",
            "message": "No image was provided in the request.",
            "error_type": "missing_payload"
        }), 400

    if img_bgr is None:
        return jsonify({
            "status": "error",
            "message": "Could not read image buffer.",
            "error_type": "read_error"
        }), 400

    # 1. Concrete Suitability Validation Check
    is_suitable, suit_msg, tech_reason, metrics = ip.verify_concrete_suitability(img_bgr)
    if not is_suitable:
        return jsonify({
            "status": "rejected",
            "validation_passed": False,
            "message": suit_msg,
            "technical_reason": tech_reason,
            "validation_metrics": metrics,
            "original_image": original_b64,
            "disclaimer": "Heuristic visual check screened out non-concrete object. The classifier does not force unrelated objects into concrete defect categories."
        })

    # 2. Generate OpenCV Edge & Contour Inspection Map
    overlay_b64, cv_stats = ip.generate_inspection_overlay(img_bgr)

    # 3. Model Classification & Normal Concrete Detection
    pred_result = classifier.predict(img_bgr)
    predicted_defect = pred_result["predicted_class"]
    is_no_defect = pred_result["is_no_defect"]

    # 4. Fetch Advisory Knowledge Base Details
    advisory = DEFECT_ADVISORY.get(predicted_defect, DEFECT_ADVISORY["No Defect"])

    # 5. Build Unified Response
    response_payload = {
        "status": "success",
        "validation_passed": True,
        "validation_message": suit_msg,
        "predicted_defect": predicted_defect,
        "is_no_defect": is_no_defect,
        "confidence_score": pred_result["confidence_score"],
        "confidence_display": pred_result["confidence_display"],
        "is_genuine_model": pred_result["is_genuine_model"],
        "class_probabilities": pred_result["class_probabilities"],
        "advisory": advisory,
        "original_image": original_b64,
        "inspection_overlay": overlay_b64,
        "cv_stats": cv_stats,
        "model_metadata": {
            "model_name": APP_METADATA.get("model_name"),
            "test_accuracy": APP_METADATA.get("test_accuracy_pct"),
            "total_training_images": APP_METADATA.get("total_images")
        },
        "case_study_clarification": CASE_STUDY_CLARIFICATION
    }

    return jsonify(response_payload)

@app.route('/api/metadata')
def get_metadata():
    """Returns dataset metrics, training split, and evaluation statistics."""
    return jsonify(APP_METADATA)

@app.route('/api/rcc-steps')
def get_rcc_steps():
    """Returns the 7-step RCC slab strengthening procedure."""
    return jsonify({
        "steps": RCC_SLAB_STRENGTHENING_STEPS,
        "mandatory_structural_note": MANDATORY_STRUCTURAL_NOTE,
        "case_study_clarification": CASE_STUDY_CLARIFICATION
    })

@app.route('/api/knowledge-base')
def get_knowledge_base():
    """Returns the complete advisory factsheets for all 6 defect categories + No Defect."""
    return jsonify(DEFECT_ADVISORY)

@app.route('/api/samples')
def get_samples():
    """Returns list of pre-configured sample images for one-click testing."""
    samples = [
        {"name": "segregation_sample.jpg", "label": "Segregation", "category": "Defect Sample"},
        {"name": "honeycombing_sample.jpg", "label": "Honeycombing", "category": "Defect Sample"},
        {"name": "spalling_sample.jpg", "label": "Spalling", "category": "Defect Sample"},
        {"name": "crack_sample.jpg", "label": "Crack", "category": "Defect Sample"},
        {"name": "void_sample.jpg", "label": "Void (Bugholes)", "category": "Defect Sample"},
        {"name": "efflorescence_sample.jpg", "label": "Efflorescence", "category": "Defect Sample"},
        {"name": "nodefect_sample.jpg", "label": "Sound Concrete (No Defect)", "category": "Normal Sample"},
        {"name": "invalid_sample.jpg", "label": "Unrelated Non-Concrete", "category": "Rejection Test"}
    ]
    return jsonify(samples)

if __name__ == '__main__':
    print("=" * 65)
    print("AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP")
    print("Server is available on the local network at http://0.0.0.0:5000")
    print("=" * 65)
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False, threaded=True)


