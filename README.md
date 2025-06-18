# Amharic-NER-Data-Collector
# 🛍️ EthioMart Amharic Named Entity Recognition (NER) System

EthioMart aims to become the central hub for all Telegram-based e-commerce activities in Ethiopia. With the rise of decentralized vendor channels on Telegram, the need for a unified and intelligent platform has become critical. This project focuses on building a fine-tuned Amharic Named Entity Recognition (NER) system that extracts key business-related entities (e.g., Product, Price, Location) from text and images shared across Ethiopian Telegram e-commerce channels.

---

## 🚀 Project Objectives

- **Data Collection**: Ingest real-time messages and media from 5+ Telegram e-commerce channels.
- **Preprocessing**: Clean and structure Amharic text data for downstream NLP tasks.
- **Labeling**: Create a high-quality, custom NER dataset following CoNLL format.
- **Model Training**: Fine-tune large pre-trained multilingual models (e.g., XLM-R, mBERT) for Amharic NER.
- **Model Comparison**: Evaluate and compare models using precision, recall, F1-score.
- **Interpretability**: Use SHAP and LIME to explain model predictions and ensure transparency.
- **Business Insight**: Populate EthioMart’s centralized product database with extracted structured data.

---

## 📦 Extracted Entity Types

### Primary Entities:
- **PRODUCT**: Product names or types
- **PRICE**: Monetary values in birr (e.g., "25,000 ብር")
- **LOCATION**: City/region references (e.g., "አዲስ አበባ")

### Optional Entities:
- **DELIVERY_FEE**: Additional shipping costs (e.g., "በነፃ መመዝገቢያ")
- **CONTACT_INFO**: Phone numbers or Telegram usernames

---

## 🗂️ Project Structure
```
├── data/
│ ├── raw/ # Unprocessed raw Telegram messages
│ ├── cleaned/ # Cleaned Amharic texts
│ ├── images/ # Downloaded product/media images
│ └── labeled/ # CoNLL-style labeled datasets
├── notebooks/ # Jupyter notebooks for EDA and model training
├── scripts/ # Python scripts for scraping, preprocessing, training
├── models/ # Saved models and checkpoints
├── outputs/ # Evaluation reports and SHAP/LIME results
├── requirements.txt # Project dependencies
└── README.md # This file
```
