import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Function for linear regression between selected columns of a dataframe
def linear_regression(df, selected_columns):

    # Loop through the selected columns for creating regression models
    for i in range(len(selected_columns)):

        # Get the next index for pairwise regression
        next_index = (i + 1) % len(selected_columns)

        # X is the independent variable (current column), y is the dependent variable (next column)
        X = np.array(df[[selected_columns[i]]]).reshape(-1, 1)  # Independent variable reshaped as a 2D array
        y = np.array(df[selected_columns[next_index]]).reshape(-1, 1)  # Dependent variable reshaped as a 2D array

        print(f"\nRegression between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y):")

        # Split the data into training and test sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Initialize and train the linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Print model coefficients, intercept, R2 score, and Mean Squared Error
        print(f"Coef: {model.coef_[0]}")
        print(f"Intercept: {model.intercept_}")
        print(f"R2: {r2_score(y_test, y_pred)}")
        print(f"MSE: {mean_squared_error(y_test, y_pred)}")

        # Plot the regression results
        plt.figure(figsize=(8, 5))
        plt.scatter(X_test, y_test, color='blue', label='Real data')  # Scatter plot for real data points
        plt.plot(X_test, y_pred, color='red', label='Linear model')  # Line plot for predicted values
        plt.xlabel('Situps')  # X-axis label
        plt.ylabel('Jumps')  # Y-axis label
        plt.title('Linear Regression')  # Plot title
        plt.legend()  # Add legend
        plt.show()  # Display the plot

# Main block of code to execute the regression
if __name__ == '__main__':

    # Load the dataset
    df = pd.read_csv('./src/download/chins_filtered_7.csv')
    
    # Specify the columns to be used for regression
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    # Call the linear regression function
    linear_regression(df, selected_columns)