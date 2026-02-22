import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras

st.title("Digit recognizer app")
st.write("Draw a digit (0-9) below and click and predict!")

def load_model():
    return keras.models.load_model("mnist_ann_model.keras")

model = load_model()

def preprocess(image: Image.Image) -> np.ndarray:
    # Convert to grayscale
    img = image.convert("L")
    # Resize to 28x28
    img = img.resize((28, 28))
    # Convert to numpy array
    arr = np.array(img).astype("float32")
    # Invert colors (white background → black, digit white)
    arr = 255.0 - arr
    # Normalize to 0-1
    arr /= 255.0
    # Flatten to (1, 784)
    arr = arr.reshape(1, 784)
    return arr

from streamlit_drawable_canvas import st_canvas
canvas_result = st_canvas(
        fill_color="rgba(255,255,255,0)",  # Transparent background
        stroke_width=15,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )
if st.button("Predict!"):
        if canvas_result.image_data is not None:
            # Convert canvas image to PIL
            img = Image.fromarray(canvas_result.image_data.astype("uint8"), "RGBA").convert("RGB")
            # Preprocess and predict
            x = preprocess(img)
            probs = model.predict(x, verbose=0)[0]
            pred_digit = int(np.argmax(probs))
            confidence = float(probs[pred_digit]) * 100
            st.success(f"Predicted Digit: {pred_digit} (Confidence: {confidence:.1f}%)")
        else:
            st.warning("Please draw a digit first!")