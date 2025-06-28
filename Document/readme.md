project report in pdf
# HematoVision – Advanced Blood Cell Classification

## 📌 Abstract
HematoVision is an AI-driven system designed to classify blood cell images into various categories using deep learning, specifically transfer learning models. It aims to aid medical professionals by providing faster, more accurate insights into hematological conditions such as leukemia and anemia.

---

## 🎯 Objectives
- Automate classification of blood cells from microscopic images.
- Improve diagnostic speed and accuracy using deep learning.
- Assist pathologists in early detection of hematologic disorders.

---

## 🧠 Methodology

### 1. Data Collection
- Source: Public datasets (e.g., Kaggle Blood Cell dataset).
- Categories: Neutrophils, Eosinophils, Monocytes, Lymphocytes, etc.

### 2. Data Preprocessing
- Image resizing and normalization.
- Augmentation techniques: rotation, zoom, flip.

### 3. Model Architecture
- **Transfer Learning**: MobileNetV2 or VGG16.
- Fine-tuning final layers.
- Loss: Categorical Crossentropy  
- Optimizer: Adam

### 4. Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score.
- Confusion matrix visualization.

---

## 🖼️ UI Overview

### Home Page (`home.html`)
- Title: HematoVision
- Upload Image
- Submit button to predict

### Results Page (`result.html`)
- Displays: Predicted class, confidence level
- Option to return to home or upload another image

---

## ⚙️ Tech Stack

| Component         | Technology Used     |
|------------------|---------------------|
| Frontend         | HTML, CSS, Bootstrap |
| Backend          | Flask (Python)      |
| Model Training   | TensorFlow, Keras   |
| Deployment       | Localhost / Flask server |
| Data Visualization | Seaborn, Matplotlib |

---

## 🧪 Results

| Metric         | Value       |
|----------------|-------------|
| Training Accuracy | 98.7%     |
| Validation Accuracy | 95.3% |
| Precision       | 0.94        |
| Recall          | 0.95        |

Confusion matrix and classification reports available in `/notebooks/`.

---

## 🏆 Achievements
- Achieved >95% validation accuracy.
- Robust classification even on noisy or augmented data.
- Lightweight model suitable for deployment in medical devices.

---

## 🔒 Limitations
- Model performance may degrade with unseen stain types or lighting conditions.
- Real-time integration with microscopes not implemented yet.

---

## 📈 Future Scope
- Integrate real-time classification via camera input.
- Deploy on cloud with user management system.
- Train on more diverse and larger datasets.

---

## 👩‍💻 Contributors
- **Gayathri V. S.** – Developer, Model Trainer, UI Designer

---



