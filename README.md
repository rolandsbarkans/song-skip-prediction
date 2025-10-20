## 🎧 Song Skip Prediction

This project uses my personal Spotify streaming history to build a machine learning model that predicts whether I will skip a song. The entire analysis from data processing to the final model interpretation is detailed in the [`skip_predict_model.ipynb`](skip_predict_model.ipynb) notebook.

The final tuned **Random Forest** model successfully identifies **67%** of the songs I would skip, revealing that **repetition fatigue** is the single most important predictor of my listening behavior.

---

### 🚀 Getting Started

To reproduce this analysis, clone the repository and install the required packages.

**Prerequisites**
- Python 3.x  
- Jupyter Notebook or JupyterLab  

---

### 🧩 Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/spotify-skip-prediction.git
cd spotify-skip-prediction
```

**2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

### 💻 Usage
Launch the Jupyter Notebook to see the code and analysis:
```bash
jupyter notebook main.ipynb
```