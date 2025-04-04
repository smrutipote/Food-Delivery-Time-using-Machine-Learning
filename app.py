import pandas as pd
import numpy as np
import gradio as gr

from utils import distcalculate
from model import prepare_data, train_models

# Load and preprocess data
df = pd.read_csv("deliverytime.txt")

# Calculate distance for each row using the haversine formula
df["distance"] = [
    distcalculate(row["Restaurant_latitude"], row["Restaurant_longitude"],
                  row["Delivery_location_latitude"], row["Delivery_location_longitude"])
    for _, row in df.iterrows()
]

# Prepare training and test data
xtrain, xtest, ytrain, ytest = prepare_data(df)

# Train the models and select Gradient Boosting
models = train_models(xtrain, ytrain)
gb_model = models["GradientBoosting"]  # Correct key name

# Prediction function
def predict_time_taken(age, rating, distance):
    input_data = np.array([[age, rating, distance]])
    prediction = gb_model.predict(input_data)
    return f"{prediction[0]:.2f} minutes"

# Gradio interface
demo = gr.Interface(
    fn=predict_time_taken,
    inputs=[
        gr.Number(label="Delivery Person Age", value=30),
        gr.Slider(minimum=1.0, maximum=5.0, step=0.1, label="Delivery Person Rating", value=4.5),
        gr.Number(label="Distance (km)", value=3.0)
    ],
    outputs="text",
    title="Food Delivery Time Predictor",
    description="Enter delivery details to predict the estimated delivery time.",
)

# Run the app
if __name__ == "__main__":
    demo.launch()