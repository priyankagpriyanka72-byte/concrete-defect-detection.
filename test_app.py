import os

# Limit thread pool allocations to prevent Windows memory exhaustion and paging file errors
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import unittest
import json
import cv2
from app import app

class ConcreteAppTestSuite(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AI-ENABLED CONCRETE DEFECT DETECTION', response.data)
        self.assertIn(b'RCC SLAB REPAIR AND STRENGTHENING PROCEDURE', response.data)
        print("[OK] Home page loaded successfully (HTTP 200)")

    def test_rcc_steps_endpoint(self):
        response = self.client.get('/api/rcc-steps')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['steps']), 7)
        self.assertEqual(data['steps'][0]['title'], "Removal of plaster and surface preparation")
        self.assertEqual(data['steps'][6]['title'], "Installation of MS Steel Sections for Structural Strengthening")
        self.assertIn("IMPORTANT ENGINEERING NOTICE", data['mandatory_structural_note'])
        print("[OK] All 7 RCC Slab Strengthening steps verified in exact sequence")

    def test_knowledge_base_endpoint(self):
        response = self.client.get('/api/knowledge-base')
        self.assertEqual(response.status_code, 200)
        kb = json.loads(response.data)
        required_classes = ["Segregation", "Honeycombing", "Spalling", "Crack", "Void", "Efflorescence", "No Defect"]
        for cls in required_classes:
            self.assertIn(cls, kb)
        print(f"[OK] Knowledge base contains all {len(required_classes)} classes")

    def test_predict_with_crack_sample(self):
        response = self.client.post('/api/predict', json={'sample_name': 'crack_sample.jpg'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['predicted_defect'], 'Crack')
        self.assertTrue(data['is_genuine_model'])
        self.assertIsNotNone(data['confidence_score'])
        self.assertIn('data:image/jpeg;base64,', data['inspection_overlay'])
        print(f"[OK] Crack prediction: {data['predicted_defect']} ({data['confidence_display']})")

    def test_predict_with_segregation_sample(self):
        response = self.client.post('/api/predict', json={'sample_name': 'segregation_sample.jpg'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['predicted_defect'], 'Segregation')
        print(f"[OK] Segregation prediction: {data['predicted_defect']} ({data['confidence_display']})")

    def test_predict_with_sound_concrete(self):
        response = self.client.post('/api/predict', json={'sample_name': 'nodefect_sample.jpg'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['predicted_defect'], 'No Defect')
        self.assertTrue(data['is_no_defect'])
        print("[OK] Sound concrete validation verified (NO DEFECT DETECTED)")

    def test_predict_with_unrelated_object_rejection(self):
        response = self.client.post('/api/predict', json={'sample_name': 'invalid_sample.jpg'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'rejected')
        self.assertFalse(data['validation_passed'])
        self.assertEqual(data['message'], "Unable to verify concrete surface. Please upload a clear concrete surface image.")
        print(f"[OK] Unrelated object successfully rejected: '{data['message']}'")

if __name__ == '__main__':
    unittest.main()
