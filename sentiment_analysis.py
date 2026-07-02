import re
import string
import pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords

# Load dataset
df = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t")

# Stop words list
stop_words = set(stopwords.words("english"))

# Keep negative words because they affect sentiment meaning
negative_words = {
    "no", "not", "nor",
    "don", "dont", "didn", "didnt",
    "doesn", "doesnt", "isn", "isnt",
    "wasn", "wasnt", "weren", "werent",
    "won", "wont", "wouldn", "wouldnt",
    "couldn", "couldnt", "shouldn", "shouldnt"
}

stop_words = stop_words - negative_words


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    words = text.split()

    words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(words)


def get_sentiment_score(text):
    return TextBlob(text).sentiment.polarity


def get_sentiment_label(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"


# Clean reviews
df["Cleaned_Review"] = df["Review"].apply(clean_text)

# Calculate sentiment scores
df["Sentiment_Score"] = df["Cleaned_Review"].apply(get_sentiment_score)

# Create sentiment labels
df["Predicted_Sentiment"] = df["Sentiment_Score"].apply(get_sentiment_label)

# Print sample results
print("\nFirst 20 results:")
print(df[["Review", "Cleaned_Review", "Sentiment_Score", "Predicted_Sentiment"]].head(20))

# Print final statistics
print("\nFinal Sentiment Statistics:")
print(df["Predicted_Sentiment"].value_counts())

# Save final result
df.to_csv("sentiment_results.csv", index=False)

print("\nAnalysis completed successfully.")
print("Results saved to sentiment_results.csv")