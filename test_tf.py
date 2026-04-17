import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("TensorFlow version:", tf.__version__)

# Simple model test
model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')

print("✅ TensorFlow working perfectly 🚀")