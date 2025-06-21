import pandas as pd
import re

def clean_amharic_text(text):
    if pd.isnull(text):
        return ""
    text = re.sub(r'\.{3,}', ' ', text)                     # Remove long series of dots
    text = re.sub(r'[^\u1200-\u137F\u0020-\u007F0-9A-Za-z]+', ' ', text)  # Keep Amharic + Latin
    text = re.sub(r'\s+', ' ', text).strip()                # Collapse whitespace
    return text

def normalize_amharic_text(text):
    if pd.isnull(text):
        return ""
    text = text.replace('፡', ' ').replace('።', '')  # Normalize Amharic punctuation
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_amharic(text):
    return text.split()

# File paths
input_file = "data/raw/telegram_data.csv"
output_file = "data/Proccesed/cleaned_telegram_data.csv"

try:
    # Load data
    df = pd.read_csv(input_file)
    print(f"✅ Loaded data: {df.shape[0]} rows")

    # Clean and normalize
    df['cleaned_message'] = df['Message'].apply(clean_amharic_text)
    df['normalized_message'] = df['cleaned_message'].apply(normalize_amharic_text)
    df['tokens'] = df['normalized_message'].apply(tokenize_amharic)

    print("✅ Text cleaning, normalization, and tokenization complete.")

    # Save processed file
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to: {output_file}")

except FileNotFoundError:
    print(f"❌ File '{input_file}' not found. Make sure the path is correct.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
