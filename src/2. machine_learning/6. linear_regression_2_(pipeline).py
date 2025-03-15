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

    for i in range(len(selected_columns)):

        next_index = (i + 1) % len(selected_columns)

        X = np.array(df[[selected_columns[i]]])
        y = np.array(df[selected_columns[next_index]]).ravel()

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        pipeline = Pipeline(steps=[
            ('scaler', StandardScaler()),
            ('feature_selection', SelectKBest(score_func=f_regression, k='all')),
            ('model', LinearRegression())        
        ])

        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)

        print(f"\nLinear Regression between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y)")

        print(f"MSE: {mse:.4f}")

        # Plot the regression results
        plt.figure(figsize=(8, 5))
        plt.scatter(X_test, y_test, color='blue', label='Real data')  # Scatter plot for real data points
        plt.plot(X_test, y_pred, color='red', label='Linear model')  # Line plot for predicted values
        plt.xlabel(selected_columns[i])  # X-axis label
        plt.ylabel(selected_columns[next_index])  # Y-axis label
        plt.title(f'Linear Regression Betewen {selected_columns[i]} & {selected_columns[next_index]}')  # Plot title
        plt.legend()  # Add legend
        plt.show()  # Display the plot

if __name__ == '__main__':
    # Load the dataset from a CSV file
    df = pd.read_csv('./src/download/chins_filtered_7.csv')

    # List of columns to use in the decision tree analysis
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    # Call the decision_tree function
    linear_regression()
