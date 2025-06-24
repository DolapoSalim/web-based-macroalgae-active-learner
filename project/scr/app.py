import os
import cv2
import tempfile
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="Macroalgae YOLOv8 Detection", layout="wide")
st.title("Macroalgae Detection using YOLOv8")

YOLO_MODEL_PATH = r"C:\Users\dolap\OneDrive\Documents\DOLAPO\data-analysis\web-based-macroalgae-active-learner\project\custom-yolo\customV8.pt"
model = YOLO(YOLO_MODEL_PATH)
class_names = model.names  # <-- Add this line here

uploaded_file = st.file_uploader("Upload an underwater macroalgae image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    temp_dir = tempfile.mkdtemp()
    image_path = os.path.join(temp_dir, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    original_image = Image.open(image_path)

    with st.spinner("Running YOLOv8 detection..."):
        results = model(image_path)
        result = results[0]
        detected_image = result.plot()
    detected_image_rgb = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original Image")
        st.image(original_image, use_container_width=True)

    with col2:
        st.subheader("🔍 YOLOv8 Detection")
        st.image(detected_image_rgb, use_container_width=True)

    st.subheader("Detected macroalgae with Confidence Scores")

    if result.boxes:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            conf = box.conf[0].item()  # confidence score as a float
            class_name = class_names[cls_id]
            st.write(f"- {class_name}: {conf:.2%} confidence")
    else:
        st.write("No detections found.")

    if result.boxes:
        df = result.to_df()
        df['image'] = uploaded_file.name
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')

        if st.button("Download CSV"):
            st.download_button(
                label="Download Detection as CSV",
                data=csv,
                file_name="detection_results.csv",
                mime="text/csv",
            ):
    else:
        st.write("No detection found")