import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Cardio-Neuro ECG Risk Analysis")

st.write("Upload an ECG image for rhythm analysis.")
st.write("⚠️ Not a medical diagnosis system.")

uploaded_file = st.file_uploader("Upload ECG Image", type=["png","jpg","jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = np.array(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)

    signal_variation = np.std(edges)

    st.image(image, caption="Uploaded ECG", use_column_width=True)
    st.image(edges, caption="Edge Detection", use_column_width=True)

    st.subheader("Analysis Result")

    if signal_variation < 20:
        st.success("Low Risk - Rhythm appears regular")
    elif signal_variation < 40:
        st.warning("Moderate Risk - Possible irregularity")
    else:
        st.error("High Risk - Irregular rhythm indicator")
