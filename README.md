📩 SMS Spam Detection System

A simple Machine Learning + Web UI project to classify SMS messages as Spam or Not Spam using a trained model and interactive web interface.

🚀 Project Overview

This project detects whether an SMS message is:

🚨 Spam Message
✅ Not Spam Message

It uses a trained ML model (NLP based) and a clean web UI for user interaction.

🧠 Features
📱 Simple and clean UI
⚡ Real-time message prediction
🤖 Machine Learning based classification
📊 Text preprocessing (TF-IDF / Vectorization)
🎯 Accurate spam detection
📱 Mobile responsive design
🛠️ Tech Stack

Frontend:

HTML
CSS
JavaScript

Backend (if using ML):

Python
Flask

Machine Learning:

Scikit-learn
Pandas
Numpy
NLP (TF-IDF Vectorizer)
📂 Project Structure
sms-spam-detection-system/
│
├── index.html
├── style.css
├── app.py
├── model.pkl
├── vectorizer.pkl
├── dataset/
│    └── spam.csv
├── static/
├── templates/
│    └── index.html
└── README.md
⚙️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/sms-spam-detection.git
2️⃣ Go to project folder
cd sms-spam-detection
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run Flask app
python app.py
5️⃣ Open browser
http://127.0.0.1:5000/
📊 Model Training (Optional Info)
Dataset: SMS Spam Collection Dataset
Algorithm: Naive Bayes / Logistic Regression
Text Processing: TF-IDF Vectorization
Accuracy: ~95% (approx)
🧪 Example

Input:

Congratulations! You won a free iPhone

Output:

🚨 Spam Message Detected
📸 UI Preview

👉 Clean card-based interface
👉 Input box for SMS
👉 Result shown instantly
🔮 Future Improvements
📱 Mobile App version
🌐 Deploy on cloud (Render / Vercel)
🤖 Deep Learning model (LSTM)
📊 Better accuracy with large dataset
🔐 User login system
👨‍💻 Author
Developed by: Kailashini
