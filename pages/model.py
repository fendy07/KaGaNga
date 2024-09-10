import numpy as np
from PIL import Image
import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas

st.title("KAGANGA (Lampung Scripts Handwriting Recognition)")

def load_model_safe(model_path):
    try:
        with tf.keras.backend.name_scope("model_loading"):
            model = load_model(model_path, compile=False)
        return model
    except IndexError as e:
        print(f"IndexError: {e}. model loading failed with error")
        return None
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

model = load_model_safe("model/model_cnn.h5")

if model is None:
    st.error("Failed to load model. Please check the model path.")
else:
    st.success("Model loaded successfully!")

