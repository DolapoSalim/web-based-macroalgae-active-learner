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

##### Directory Structure
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