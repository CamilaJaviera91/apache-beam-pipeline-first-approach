from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def decision_tree(df, selected_columns):
    # Loop through each selected column to build a decision tree comparing it with the next column
    for i in range(len(selected_columns)):

        # Determine the index of the next column in a circular manner
        next_index = (i + 1) % len(selected_columns)

        # Define features (X) and labels (y) for the decision tree
        X = np.array(df[[selected_columns[i]]])  # Current column used as features
        y = np.array(df[selected_columns[next_index]]).ravel()  # Next column used as labels (flattened)

        print(f"Decision tree between '{selected_columns[i]}' (X) and '{selected_columns[next_index]}' (y)")

        # Split the dataset into training and testing sets (70% training, 30% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Display the shapes of training data
        print(f"X_train shape: {X_train.shape}")
        print(f"y_train shape: {y_train.shape}")

        # Display the unique classes in the training labels
        print("Unique classes in y_train:", np.unique(y_train))

        # Initialize and train the decision tree classifier
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
        clf.fit(X_train, y_train)

        # Calculate the accuracy of the model on the test set
        accuracy = clf.score(X_test, y_test)
        print(f"Accuracy: {accuracy:.2f}")

        # Plot the decision tree
        plt.figure(figsize=(12, 8))
        tree.plot_tree(clf, filled=True, feature_names=[selected_columns[i]])
        plt.show()

        print('\n')


if __name__ == '__main__':
    # Load the dataset from a CSV file
    df = pd.read_csv('./src/download/chins_filtered_7.csv')

    # List of columns to use in the decision tree analysis
    selected_columns = ['Situps Range', 'Jumps Range', 'Chins Range']

    # Call the decision_tree function
    decision_tree(df, selected_columns)