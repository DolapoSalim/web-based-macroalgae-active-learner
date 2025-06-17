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
├── custom-yolo/           # folder containing pre-trained YOLO model but .gitignored
├── images/                # raw images to label
├── output/
│   ├── masks/             # generated masks
│   ├── overlays/          # visualization of predictions
│   └── annotations.json   # structured result
├── sam-model              # contains the Segment Anything Model
└── scr/                   # contains notebook
|   ├── app.py
├── readMe.md
├── requirements.txt
```

##### 📂 To Run It Locally:
- Save this file as app.py
- Place yolo_model.pt and sam_b.pt in the same directory
- Run the requirement file
```Bash
pip install -r requirements.txt
```
- Install dependencies:
``` Bash
pip install streamlit opencv-python pillow ultralytics
```
- Run the app:

```Bash
streamlit run project/scr/app.py
```
