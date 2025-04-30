import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define class names
DEFECT_CLASSES = [
    'missing_hole',
    'mouse_bite',
    'open_circuit',
    'short',
    'spur',
    'spurious_copper',
    'normal'  # No defect found
]

def create_model(num_classes=7):
    """
    Create a transfer learning model based on MobileNetV2
    for PCB defect classification
    """
    # Load the pretrained MobileNetV2 model without the top layer
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    # Freeze the base model layers
    for layer in base_model.layers:
        layer.trainable = False
    
    # Add custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    
    # Create the final model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Compile the model
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def train_model(model, train_dir, validation_dir, batch_size=32, epochs=10):
    """
    Train the model using data from the specified directories
    """
    # Data augmentation for training
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    # Validation data should only be rescaled
    validation_datagen = ImageDataGenerator(rescale=1./255)
    
    # Flow training images in batches
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical'
    )
    
    # Flow validation images in batches
    validation_generator = validation_datagen.flow_from_directory(
        validation_dir,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical'
    )
    
    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples // batch_size,
        epochs=epochs,
        validation_data=validation_generator,
        validation_steps=validation_generator.samples // batch_size
    )
    
    return history

def save_model(model, model_path='pcb_defect_model.h5'):
    """
    Save the trained model to disk
    """
    model.save(model_path)
    print(f"Model saved to {model_path}")

def load_model_from_file(model_path='pcb_defect_model.h5'):
    """
    Load a trained model from disk
    """
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        print(f"Model file {model_path} not found. Creating a new model.")
        return create_model()

def create_dummy_model(model_path='models/pcb_defect_model.h5'):
    """
    Create a dummy model for demonstration purposes
    This is useful when you don't have time to train a real model
    but want to demonstrate the application flow
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    
    # Create a simple model with the expected input/output shape
    model = create_model(len(DEFECT_CLASSES))
    
    # Save the model
    model.save(model_path)
    print(f"Dummy model created and saved to {model_path}")
    
    return model

if __name__ == "__main__":
    # This will create a dummy model when the script is run directly
    create_dummy_model()