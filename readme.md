### Macroalgae Auto-Label + Coverage Web Tools

##### 🧩 Core Features
| Features | Description |
|----------- | ----------- |
| 📤 Upload new underwater images | User can upload new image(s) via the web interface |
| ⚙️ Auto-label with YOLO + SAM | YOLO detects → SAM segments each detection |
| 🖼️ Display results interactively | 	Show segmentation overlays + class-wise masks |
| 📊 Calculate % coverage | Pixel-based area per class (for each image) |
| 💾 Download annotations & coverage | Export JSON or image+mask zip archive |


##### 🛠️ Tech Stack
- Frontend + Backend: Streamlit (modern, fast, interactive UI)
- Model Backend: Your fine-tuned YOLO model + pretrained SAM model
- Image Ops: OpenCV & NumPy
- Optional Storage: Save results locally or integrate with Firebase/GCP later.

##### 📁 Directory Structure
``` graphql
project/
├── images/                # raw images to label
├── yolo_model.pt          # your trained YOLO model
├── sam_b.pt               # pretrained SAM model
├── output/
│   ├── masks/             # generated masks
│   ├── overlays/          # visualization of predictions
│   └── annotations.json   # structured result
└── pipeline.py            # your main script
```

##### 📂 To Run It Locally:
- Save this file as app.py
- Place yolo_model.pt and sam_b.pt in the same directory
- Run the requirement file
```Bash
pip install -r requirements.txt
streamlit run src/app.py
```
- Install dependencies:
``` Bash
pip install streamlit opencv-python pillow ultralytics
```
- Run the app:

```Bash
streamlit run app.py
```
