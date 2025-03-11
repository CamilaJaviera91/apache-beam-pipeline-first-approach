import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def linear_regression(df, selected_columns):

    for i in range(len(selected_columns)):

        next_index = (i + 1) % len(selected_columns)

        X = np.array(df[[selected_columns[i]]]).reshape(-1, 1)
        y = np.array(df[selected_columns[next_index]]).reshape(-1, 1)

        print(f"\nRegression between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y):")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        print(f"Coef: {model.coef_[0]}")
        print(f"Intercept: {model.intercept_}")
        print(f"R2: {r2_score(y_test, y_pred)}")
        print(f"MSE: {mean_squared_error(y_test, y_pred)}")

        plt.figure(figsize=(8, 5))
        plt.scatter(X_test, y_test, color='blue', label='Real data')
        plt.plot(X_test, y_pred, color='red', label='Linear model')
        plt.xlabel('Situps')
        plt.ylabel('Jumps')
        plt.title('Linear Regression')
        plt.legend()
        plt.show()

if __name__ == '__main__':

    df = pd.read_csv('./src/download/chins_filtered_7.csv')
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    linear_regression(df, selected_columns)