import os
import cv2
from model.classifier import classifier
import image_processing as ip

print("Checking samples in static/images/samples:")
for s in sorted(os.listdir('static/images/samples')):
    if s.endswith('.jpg'):
        p = os.path.join('static/images/samples', s)
        img = cv2.imread(p)
        ok, msg, reason, metrics = ip.verify_concrete_suitability(img)
        if not ok:
            print(f"{s:26s} -> VALIDATION REJECTED: {msg}")
        else:
            res = classifier.predict(img)
            p_class = res['predicted_class']
            conf = res['confidence_display']
            print(f"{s:26s} -> VERIFIED | Predicted: {p_class:14s} | Confidence: {conf}")
