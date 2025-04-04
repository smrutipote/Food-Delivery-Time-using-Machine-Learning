## model.py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

def prepare_data(df):
    X = np.array(df[["Delivery_person_Age", "Delivery_person_Ratings", "distance"]])
    y = np.array(df["Time_taken(min)"])
    xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.1, random_state=42)
    return xtrain, xtest, ytrain, ytest

def train_models(xtrain, ytrain):
    models = {}

    # Linear Regression
    lin_model = LinearRegression()
    lin_model.fit(xtrain, ytrain)
    models["LinearRegression"] = lin_model

    # Random Forest Regressor
    rf_model = RandomForestRegressor()
    rf_model.fit(xtrain, ytrain)
    models["RandomForest"] = rf_model

    # Gradient Boosting Regressor
    gb_model = GradientBoostingRegressor()
    gb_model.fit(xtrain, ytrain)
    models["GradientBoosting"] = gb_model

    return models

