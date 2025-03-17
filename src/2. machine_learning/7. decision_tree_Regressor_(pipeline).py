import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def decision_tree():
    """
    Function to perform decision tree regression between each pair of columns from the dataset.
    It also plots the regression tree and calculates the Mean Squared Error (MSE).
    """

    for i in range(len(selected_columns)):
        
        next_index = (i + 1) % len(selected_columns)

        # Define features (X) and target variable (y)
        X = np.array(df[[selected_columns[i]]])  # Select the current column as the independent variable
        y = np.array(df[selected_columns[next_index]]).ravel()  # Select the next column as the dependent variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a pipeline for preprocessing and modeling
        pipeline = Pipeline(steps=[
            ('scaler', StandardScaler()),  # Standardize features
            ('model', DecisionTreeRegressor(max_depth=3, random_state=42))  # Decision Tree for regression
        ])

         # Train the model using the training data
        pipeline.fit(X_train, y_train)

        # Make predictions using the test data
        y_pred = pipeline.predict(X_test)

        # Calculate Mean Squared Error (MSE)
        mse = mean_squared_error(y_test, y_pred)
        
        # Display the results
        print(f"\nDecision Tree between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y)")
        print(f"MSE: {mse:.4f}")

        # Plot results
        plt.figure(figsize=(12, 8))
        plt.scatter(X_test, y_test, color='blue', label='Actual Data')
        plt.scatter(X_test, y_pred, color='red', label='Predicted Data')
        plt.title(f'Decision Tree Regression Plot: {selected_columns[i]} vs {selected_columns[next_index]}')
        plt.xlabel(selected_columns[i])
        plt.ylabel(selected_columns[next_index])
        plt.legend()
        plt.show()

if __name__ == '__main__':
    # Load the dataset from a CSV file
    df = pd.read_csv('./src/download/chins_filtered_7.csv')

    # List of columns to use for the analysis
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    # Call the decision_tree function
    decision_tree()