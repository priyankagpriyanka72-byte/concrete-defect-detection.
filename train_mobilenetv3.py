"""
MobileNetV3-Small Training Script for Concrete Defect Classification
Classes: Crack, Honeycombing, No Defect, Spalling, Void
"""

import os
import sys

def train():
    try:
        import tensorflow as tf
        from tensorflow.keras.preprocessing.image import ImageDataGenerator
        from architecture import build_mobilenetv3_small_model, CLASSES
    except ImportError:
        print("TensorFlow is required to train the model. Install via: pip install tensorflow")
        sys.exit(1)

    print("Building MobileNetV3-Small defect classification model...")
    model = build_mobilenetv3_small_model(num_classes=len(CLASSES))
    if model is None:
        print("Failed to initialize MobileNetV3-Small.")
        return

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    model.summary()
    print("\nModel ready for training with dataset directory structure: [CRACK, HONEYCOMBING, NO_DEFECT, SPALLING, VOID]")
    print("Export path: model/mobilenetv3_defect_model.keras")

if __name__ == '__main__':
    train()
