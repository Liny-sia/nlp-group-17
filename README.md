# Sentiment Analysis Model Comparison

## Project Overview
This project focuses on sentiment analysis of product reviews using Natural Language Processing (NLP).

The goal is to classify reviews into:
- Negative
- Neutral
- Positive

We compare multiple machine learning and deep learning models to determine which performs best.

## Models Used
- BERT (Transformer-based model)
- Logistic Regression
- LSTM (Recurrent Neural Network)
- Random Forest Classifier
- Linear Support Vector Classifier (Linear SVC)

## Dataset
- Source: Product review dataset (CSV file)
- Features:
  - Review text
  - Star rating
- Labels:
  - Negative (1–2)
  - Neutral (3)
  - Positive (4–5)

## Workflow
1. Load dataset  
2. Data cleaning (rename columns, remove missing values)  
3. Convert ratings to sentiment labels  
4. Train/validation/test split (shared across all models)  
5. Train and evaluate each model  
6. Compare results  

## Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  

## Setup Instructions

### 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the notebook
Open:
sentiment_analysis.ipynb
Make sure to select the correct kernel.

## Results

