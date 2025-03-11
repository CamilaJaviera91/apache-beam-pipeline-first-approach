from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def decision_tree(df, selected_columns):

    for i in range(len(selected_columns)):

        next_index = (i + 1) % len(selected_columns)

        X = np.array(df[[selected_columns[i]]])
        y = np.array(df[selected_columns[next_index]]).ravel()

        print(f"Decision tree between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y)")

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        print(f"X_train shape: {X_train.shape}")
        print(f"y_train shape: {y_train.shape}")

        print("Clases únicas en y_train:", np.unique(y_train))

        clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
        clf.fit(X_train, y_train)

        accuracy = clf.score(X_test, y_test)
        print(f"Accuracy: {accuracy:.2f}")

        plt.figure(figsize=(12, 8))
        tree.plot_tree(clf, filled=True, feature_names=[selected_columns[i]])
        plt.show()

        print('\n')
        
if __name__ == '__main__':
    
    df = pd.read_csv('./src/download/chins_filtered_7.csv')
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    decision_tree(df, selected_columns)