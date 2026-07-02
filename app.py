from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model and vectorizer
model = pickle.load(open("models/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    # Convert message into vector
    transformed_message = vectorizer.transform([message])

    # Predict class
    result = model.predict(transformed_message)[0]

    # Predict probability
    probability = model.predict_proba(transformed_message)[0]

    confidence = round(max(probability) * 100, 2)

    if result == 1:
        prediction = "🚨 Spam Message"
    else:
        prediction = "✅ Not Spam Message"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)