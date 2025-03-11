from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Function to calculate and print Mean Squared Error (MSE) and Mean Absolute Error (MAE)
def mse_mae(df, selected_columns):
    
    # Loop over the selected columns to compare pairs of columns
    for i in range(len(selected_columns)):
        
        # Get the next column in the list (wraps around to the first if at the last element)
        next_index = (i + 1) % len(selected_columns)
        
        # Select the current column for X (features) and the next column for y (target)
        X = np.array(df[[selected_columns[i]]]).reshape(-1, 1)  # Reshape X to be a 2D array
        y = np.array(df[selected_columns[next_index]]).reshape(-1, 1)  # Reshape y to be a 2D array
        
        # Split the data into training and test sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Create and train the Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Make predictions using the trained model
        y_pred = model.predict(X_test)
        
        # Calculate Mean Squared Error (MSE) and Mean Absolute Error (MAE)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        # Print the results for the current pair of columns
        print(f'MSE for {selected_columns[i]} and {selected_columns[next_index]}: {mse:.4f}')
        print(f'MAE for {selected_columns[i]} and {selected_columns[next_index]}: {mae:.4f}')
        
        print('\n')  # Print a new line for better readability

# Main block of code to run when the script is executed
if __name__ == '__main__':
    
    # Load the dataset from the specified CSV file
    df = pd.read_csv('./src/download/chins_filtered_7.csv')
    
    # List of selected columns to compare
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']
    
    # Call the function to calculate MSE and MAE for the selected columns
    mse_mae(df, selected_columns)