"""
AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
Model Package Initialization
"""

import os
import sys

# Ensure root directory is in sys.path so modules inside model can import train_model
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from .architecture import CLASSES_6, build_mobilenetv3_small_model
from .classifier import classifier, ConcreteDefectClassifier

__all__ = [
    "CLASSES_6",
    "build_mobilenetv3_small_model",
    "classifier",
    "ConcreteDefectClassifier"
]
