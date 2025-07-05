# 🌾 Crop Prediction Web App

A machine learning-powered web application that predicts the most suitable crop to cultivate based on user inputs such as temperature, humidity, pH level, and rainfall. Built using Django for the backend and HTML/CSS for the frontend.

## 🚀 Features

- 📊 User-friendly form to collect key soil and weather parameters
- 🤖 ML model trained to recommend crops based on data patterns
- 📱 Responsive, clean UI designed with CSS and modern layouts
- 🧠 Built with Django for handling form processing and predictions
- 💡 Doodle-inspired background design for a creative, aesthetic touch

## 🛠️ Tech Stack

| Frontend        | Backend         | Machine Learning |
|-----------------|-----------------|------------------|
| HTML, CSS       | Django (Python) | scikit-learn     |
| JavaScript (optional) | MySQL or SQLite | Pandas, NumPy     |

## 🧾 How It Works

1. User visits the homepage and enters:
   - 🌡️ Temperature
   - 💧 Humidity
   - 🧪 pH
   - ☔ Rainfall / Water availability

2. On form submission:
   - Input is sent via POST request to the Django view
   - The trained ML model processes the data and returns the best crop suggestion
   - The predicted crop is displayed dynamically on a new results page


