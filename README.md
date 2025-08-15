# 🌪️ Disaster Tweets Classification

A machine learning project that classifies tweets as disaster-related or not using RNN models. Built with Python, TensorFlow, and FastAPI.

## 📋 Overview

This project uses natural language processing and deep learning to identify disaster-related tweets. The system analyzes text content and predicts whether a tweet is about a disaster or not.

## ✨ Features

- **Data Analysis & Preprocessing**: Text cleaning using NLTK
- **Multiple Embedding Methods**: GloVe, FastText, and custom embeddings
- **RNN Models**: LSTM/GRU-based neural networks
- **REST API**: FastAPI service for predictions
- **Docker Support**: Easy deployment

## 📁 Project Structure

```
├── src/
│   ├── app/                    # FastAPI application
│   ├──── api/                    # API endpoints
│   ├──── core/                   # Configuration
│   ├──── services/               # classificationa and text preprocessing logic
│   ├──── schemas/                # response and request classes
│   ├──── main.py                 # Entry point
│   ├── data/                   # Dataset files
│   ├── notebooks/              # Jupyter notebook
│   │   └── notebook.ipynb      # Data analysis and model training
│   ├── artifacts/              # Trained models
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Quick Start

### Local Installation

1. **Clone and setup**
   ```bash
   git clone <repo-url>
   cd disaster-tweets-classification
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run the API**
   ```bash
   uvicorn app:main --reload
   ```

### Docker Deployment

```bash
# Build and run
docker build -t disaster-classifier .
docker run -p 8000:8000 disaster-classifier
```

## 📡 API Usage

### Classify Texts

**POST** `/predict`

```json
{
  "texts": ["Earthquake hits the city!", "Having lunch with friends"]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "text": "Earthquake hits the city!",
      "predicted_label": "disaster",
      "probability": 0.89
    },
    {
      "text": "Having lunch with friends",
      "predicted_label": "non-disaster",
      "probability": 0.92
    }
  ]
}
```

## 🧠 Models

The project includes three different approaches:

1. **GloVe Embeddings**: Pre-trained word vectors + LSTM
2. **FastText Embeddings**: Facebook's FastText vectors + GRU  
3. **Custom Embeddings**: Trainable embedding layer + LSTM


## 🔧 Configuration

Edit `.env` file:

```bash
APP_NAME="Text-Classification"
VERSION="1.0.0"
API_SECRET_KEY="" <-- add your api key here
```

## 📝 Development

### Training Models

Open `src/notebooks/analysis.ipynb` to:
- Explore the dataset
- Preprocess text data
- Train different models
- Evaluate performance


## 🛠️ Tech Stack

- **Python 3.12**
- **TensorFlow/Keras** - Deep learning
- **FastAPI** - Web framework
- **NLTK** - Text preprocessing
- **spaCy** - NLP tools
- **Docker** - Containerization

## 📞 Contact

For questions or suggestions, please open an issue or contact [diaa.kotb42@gmail.com](mailto:diaa.kotb42@gmail.com).

---

⭐ If this project helps you, please give it a star!