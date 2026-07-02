import pandas as pd
import pickle
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Read TSV file
data = pd.read_csv("dataset/spam.csv", sep="\t")

data.columns = ["label", "message"]

data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

X = data["message"]
y = data["label"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

os.makedirs("models", exist_ok=True)

pickle.dump(model, open("models/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("models/vectorizer.pkl", "wb"))

print("Model trained successfully!")