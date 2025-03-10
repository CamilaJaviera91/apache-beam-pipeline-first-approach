from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def mse_mae(df, selected_columns):

    for i in range(len(selected_columns)):

        next_index = (i + 1) % len(selected_columns)

        X = np.array(df[[selected_columns[i]]]).reshape(-1, 1)
        y = np.array(df[selected_columns[next_index]]).reshape(-1, 1)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        print(f'MSE for {selected_columns[i]} and {selected_columns[next_index]}: {mse:.4f}')
        print(f'MAE for {selected_columns[i]} and {selected_columns[next_index]}: {mae:.4f}')
        
        print('\n')

if __name__ == '__main__':

    # Load the dataset from the specified CSV file.
    df = pd.read_csv('./src/download/chins_filtered_7.csv')

    # Select columns
    selected_columns = ['Situps', 'Jumps', 'Chins']
   
    mse_mae(df, selected_columns)