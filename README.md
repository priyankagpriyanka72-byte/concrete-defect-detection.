# AI-ENABLED CONCRETE DEFECT DETECTION, PREVENTION AND REPAIR ADVISORY APP

A complete, professional civil-engineering-themed web application for structural defect identification, image suitability screening, repair methodology advisory, and structural strengthening guidance.

---

## 🏗️ 1. Project Overview

This application serves as a structural engineering decision-support platform designed for civil engineers, site inspectors, researchers, and academic project presentations. It combines computer vision preprocessing, machine learning defect classification, an engineering knowledge base, and a dedicated 7-step RCC slab strengthening protocol.

### Defect Categories (6 Classes)
1. **Segregation**: Separation of coarse aggregate from cement mortar paste causing localized weak planes.
2. **Honeycombing**: Porous stone pockets resulting from congested rebar or inadequate compaction.
3. **Spalling**: Concrete delamination and flaking exposing corroded reinforcing steel bars.
4. **Crack**: Tensile stress separations caused by thermal shrinkage, settlement, or load overstress.
5. **Void (Bugholes)**: Entrapped air/bleed water pockets along formwork surfaces.
6. **Efflorescence**: Leached crystalline mineral salt deposits formed by water evaporation.
7. **Sound Concrete (No Defect)**: Dedicated verification mechanism for undamaged surfaces.

---

## 📊 2. Genuine Dataset & Model Training Metrics

The classification model was trained and evaluated directly on the provided dataset of **326 genuine site inspection images**:

| Defect Class | Dataset Folder | Total Images | Hold-out Precision | Hold-out Recall | Hold-out F1-Score |
|---|---|---|---|---|---|
| **Segregation** | `SEGREGATION/` | 50 | 0.67 | 1.00 | 0.80 |
| **Honeycombing** | `HONEYCOMBING/` | 32 | 1.00 | 0.60 | 0.75 |
| **Spalling** | `SPALLING/` | 39 | 1.00 | 0.50 | 0.67 |
| **Crack** | `CRACK/` | 82 | 0.75 | 1.00 | 0.86 |
| **Void** | `VOID/` | 29 | 1.00 | 0.75 | 0.86 |
| **Efflorescence** | `EFFLORESCENCE/` | 94 | 0.83 | 0.71 | 0.77 |
| **TOTAL** | | **326** | **Weighted Avg: 0.84** | **0.80** | **0.79** |

- **Training Convergence**: 100.00%
- **Validation Accuracy**: 71.43%
- **Hold-out Test Accuracy**: **79.59% (~80%)**
- *Note*: All performance statistics are mathematically evaluated from the hold-out dataset partition without fabrication.

---

## 🛡️ 3. Concrete Surface Validation Protocol

Before running defect classification, every uploaded image undergoes a four-stage civil engineering suitability check:
1. **File Type**: Accepts only valid JPG, JPEG, and PNG image files. Non-image files are rejected.
2. **Object Rejection**: Screens out non-concrete objects (people, animals, vehicles, food, furniture, and solid computer screenshots).
3. **Suitability Safeguard**: If an image cannot be verified as concrete, it displays:
   > *"Unable to verify concrete surface. Please upload a clear concrete surface image."*
   Unrelated objects are never forced into a concrete defect category.
4. **Honest Engineering Disclaimer**: Image validation operates via visual heuristics (colorimetry, saturation, texture variance). No false claims of perfect segmentation are made.

---

## 🔩 4. RCC Slab Repair and Strengthening Module (7 Steps)

The application includes a dedicated engineering section displaying the observed RCC slab strengthening case study in exact chronological sequence:

- **Step 1: Removal of plaster and surface preparation**
- **Step 2: Removal of loose and deteriorated concrete**
- **Step 3: Treatment of exposed reinforcement**
- **Step 4: Fixing of wire mesh**
- **Step 5: Guniting (Shotcreting)**
- **Step 6: Curing and finishing**
- **Step 7: Installation of MS Steel Sections for Structural Strengthening**

Each step is accompanied by technical explanations, action checklists, and high-resolution SVG technical illustrations.

> **Mandatory Structural Notice:**
> The actual strengthening method, structural steel section sizing, anchor embedment depth, and execution sequence must be strictly verified against the approved site-specific structural design and calculations verified by a certified Structural Engineer.

---

## 📁 5. Project Structure

```
├── app.py                     # Flask application backend
├── train_model.py             # 6-class dataset training pipeline
├── image_processing.py        # Image validation & OpenCV overlay generator
├── knowledge_base.py          # Civil engineering advisory knowledge base
├── requirements.txt           # Python dependencies
├── README.md                  # Comprehensive documentation
├── templates/
│   └── index.html             # Civil engineering frontend dashboard
├── static/
│   ├── css/
│   │   └── style.css          # Responsive dark-theme engineering stylesheet
│   ├── js/
│   │   └── script.js          # Interactive frontend controller & camera
│   └── images/
│       ├── logo.svg           # Application logo
│       ├── samples/           # Real test samples from the 6 dataset folders
│       └── steps/             # 7 high-res SVG technical step diagrams
├── model/
│   ├── architecture.py        # MobileNetV3-Small & pipeline architecture
│   ├── classifier.py          # Real-time inference & normal concrete engine
│   ├── concrete_defect_classifier_6class.joblib  # Trained model weights
│   └── model_metadata.json    # Genuine training & test evaluation metrics
├── CRACK/                     # 82 site images
├── EFFLORESCENCE/             # 94 site images
├── HONEYCOMBING/              # 32 site images
├── SEGREGATION/               # 50 site images
├── SPALLING/                  # 39 site images
└── VOID/                      # 29 site images
```

---

## 🚀 6. How to Run the Application Locally

### Prerequisites
- Python 3.10, 3.11, 3.12, or 3.13
- Web browser (Chrome, Firefox, Edge, Safari)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: (Optional) Re-train Model on Dataset
If you wish to re-train the model or modify hyperparameters:
```bash
python train_model.py
```

### Step 3: Start the Flask Application
```bash
python app.py
```

### Step 4: Access in Browser (Desktop & Phone)
- **From this computer**:
  ```
  http://127.0.0.1:5000
  ```
- **From your phone (same Wi-Fi network)**:
  ```
  http://<Your-Computer-IP>:5000
  ```
  *(The computer's Wi-Fi IP address is printed in the terminal when `python app.py` starts, e.g. `http://10.126.45.49:5000`)*


---

## 🎯 7. Features for College Presentation

1. **One-Click Quick Test Gallery**: Test any of the 6 defect categories, sound concrete, or rejection tests with 1 click.
2. **Interactive OpenCV Surface Map**: Toggle between the original photo and the edge/contour inspection map.
3. **Camera Snapshot Support**: Live video stream capture for mobile phones and laptops.
4. **Softmax Probability Distribution**: View model probabilities across all 6 classes.
5. **Printable Specification Report**: Single-click clean printing of advisory factsheets and RCC slab strengthening instructions.
6. **Zero External API Cost**: Operates 100% locally on CPU without paid cloud APIs or OpenAI keys.
