Check out this project live on huggingface : https://huggingface.co/spaces/smrup/Food-Delivery-Time-Prediction-using-Machine-Learning

🛵 Food Delivery Time Predictor – Project Overview
Objective: Predict estimated food delivery time using machine learning based on:

Delivery person’s age

Delivery person’s rating

Distance between the restaurant and the customer

Features:

Calculates distance using the Haversine formula from lat-long coordinates

Implements and compares three models:

Linear Regression

Random Forest

Gradient Boosting

Clean, user-friendly Gradio web interface

Designed for deployment on Hugging Face Spaces

🗂️ Project Structure
app.py: Main file to launch the Gradio UI and handle predictions

model.py: Functions for data preprocessing and model training

utils.py: Contains the Haversine formula to compute distances

deliverytime.txt: Dataset used for training and evaluation

requirements.txt: Lists necessary Python packages for the project

⚙️ Tech Stack
Language: Python

Libraries:

pandas, numpy for data handling

scikit-learn for model building

gradio for UI and deployment

Deployment: Hugging Face Spaces compatible

🛠️ How to Run
Clone the repository or download the files.

Ensure your environment has Python installed.

Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Run the app locally with:

bash
Copy
Edit
python app.py
To deploy on Hugging Face:

Upload all files (including requirements.txt) to a new Space

Select Gradio as the SDK

📈 Output
Takes input: age, rating, and distance

Returns the predicted time in minutes

Uses the Gradient Boosting model by default for best accuracy

