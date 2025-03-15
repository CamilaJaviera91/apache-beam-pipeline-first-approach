import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def linear_regression():
    """
    Function to perform linear regression between each pair of columns from the dataset.
    It also plots the regression line and calculates the Mean Squared Error (MSE).
    """

    # Loop through all selected columns
    for i in range(len(selected_columns)):
        
        # Determine the index of the next column (circular indexing)
        next_index = (i + 1) % len(selected_columns)

        # Define features (X) and target variable (y)
        X = np.array(df[[selected_columns[i]]])  # Select the current column as the independent variable
        y = np.array(df[selected_columns[next_index]]).ravel()  # Select the next column as the dependent variable

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create a Pipeline for preprocessing and modeling
        pipeline = Pipeline(steps=[
            ('scaler', StandardScaler()),  # Standardize features to have mean = 0 and variance = 1
            ('feature_selection', SelectKBest(score_func=f_regression, k='all')),  # Use all features
            ('model', LinearRegression())  # Apply Linear Regression model
        ])

        # Train the model using the training data
        pipeline.fit(X_train, y_train)

        # Make predictions using the test data
        y_pred = pipeline.predict(X_test)

        # Calculate Mean Squared Error (MSE)
        mse = mean_squared_error(y_test, y_pred)
        
        # Display the results
        print(f"\nLinear Regression between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y)")
        print(f"MSE: {mse:.4f}")

        # Plotting the regression results
        plt.figure(figsize=(8, 5))
        plt.scatter(X_test, y_test, color='blue', label='Real data')  # Scatter plot of the real data points
        plt.plot(X_test, y_pred, color='red', label='Linear model')  # Line plot of the predicted values
        plt.xlabel(selected_columns[i])  # Label for the X-axis
        plt.ylabel(selected_columns[next_index])  # Label for the Y-axis
        plt.title(f'Linear Regression Between {selected_columns[i]} & {selected_columns[next_index]}')  # Plot title
        plt.legend()  # Show legend
        plt.show()  # Display the plot

if __name__ == '__main__':
    # Load the dataset from a CSV file
    df = pd.read_csv('./src/download/chins_filtered_7.csv')

    # List of columns to use for the analysis
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    # Call the linear_regression function
    linear_regression()