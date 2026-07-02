# Restaurant Reviews Sentiment Analysis

This project was developed as part of the i2i Systems Academy NLP assignment.

The application performs basic sentiment analysis on restaurant reviews using Natural Language Processing (NLP) techniques in Python.

---

## Project Features

- Load restaurant review dataset
- Text preprocessing
  - Lowercase conversion
  - Remove punctuation
  - Remove stopwords
  - Word stemming
- Sentiment polarity calculation using TextBlob
- Sentiment classification
  - Positive
  - Neutral
  - Negative
- Export analysis results to CSV

---

## Technologies

- Python 3
- Pandas
- NLTK
- TextBlob

---

## Dataset

Restaurant_Reviews.tsv

- 1000 restaurant reviews
- Binary sentiment labels

---

## Project Structure

```
i2i-Academy-NLP-1
│
├── Restaurant_Reviews.tsv
├── sentiment_analysis.py
├── sentiment_results.csv
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aysenur-dogan/i2i-Academy-NLP-1.git
```

Install the required libraries:

```bash
pip install pandas nltk textblob
```

Download NLTK resources:

```python
import nltk

nltk.download("stopwords")
nltk.download("punkt")
```

---

## Run

```bash
python3 sentiment_analysis.py
```

---

## Output

The application generates:

- Sentiment polarity score
- Predicted sentiment
- sentiment_results.csv

Example output:

| Review | Score | Prediction |
|--------|------:|------------|
| Loved this place | 0.80 | Positive |
| Not tasty | -0.60 | Negative |
| Service was okay | 0.00 | Neutral |

---

## Repository

https://github.com/aysenur-dogan/i2i-Academy-NLP-1

---

Developed for the **i2i Systems Academy NLP Assignment**.
