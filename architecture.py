"""
AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP
Model Architecture Specification (MobileNetV3-Small & Trained Ensemble)
Defect Categories:
1. Segregation
2. Honeycombing
3. Spalling
4. Crack
5. Void
6. Efflorescence
"""

CLASSES_6 = [
    "Segregation",
    "Honeycombing",
    "Spalling",
    "Crack",
    "Void",
    "Efflorescence"
]

def build_mobilenetv3_small_model(num_classes=6, input_shape=(224, 224, 3)):
    """
    Constructs the MobileNetV3-Small architecture for 6-class concrete defect classification.
    Used for Deep Learning transfer learning when TensorFlow is available.
    """
    try:
        import tensorflow as tf
        from tensorflow.keras import layers, models
        from tensorflow.keras.applications import MobileNetV3Small

        base_model = MobileNetV3Small(
            input_shape=input_shape,
            include_top=False,
            weights='imagenet',
            minimalistic=False,
            pooling='avg'
        )
        base_model.trainable = False

        inputs = tf.keras.Input(shape=input_shape)
        x = base_model(inputs, training=False)
        x = layers.Dropout(0.3)(x)
        x = layers.Dense(128, activation='relu')(x)
        x = layers.BatchNormalization()(x)
        outputs = layers.Dense(num_classes, activation='softmax')(x)

        model = models.Model(inputs, outputs, name="Concrete_Defect_MobileNetV3_Small_6Class")
        return model
    except Exception as e:
        return None
