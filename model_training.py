import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def train_hockey_model(file_path="data/processed_hockey_data.csv"):
    """Train a prediction model for hockey game outcomes"""
    
    # Load processed data
    df = pd.read_csv(file_path)
    
    # For a real project, you'd want more features
    # This is simplified for demonstration
    X = df[['total_goals', 'goal_diff']]  
    y = df['home_win']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))
    
    # Save model
    os.makedirs('models', exist_ok=True)
    with open('models/hockey_prediction.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved to models/hockey_prediction.pkl")
    
    return model

if __name__ == "__main__":
    train_hockey_model()