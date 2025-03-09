from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np
import pandas as pd

# Load the dataset from the specified CSV file.
df = pd.read_csv('./src/download/chins_filtered_7.csv')

def cluster(value, name):
    results = {}
    total_best_k = 0
    total_best_score = 0
    num_variables = len(value)

    for i in range(len(value)):  # Loop over each variable in the list
        X = np.array(value[i]).reshape(-1, 1)

        best_score = -1
        best_k = 0

        for k in range(2, 11):  # Trying cluster numbers from 2 to 10
            kmeans = KMeans(n_clusters=k, random_state=42)
            clusters = kmeans.fit_predict(X)
            score = silhouette_score(X, clusters)

            if score > best_score:
                best_score = score
                best_k = k

        # Store results for each variable
        results[name[i]] = {'Best k': best_k, 'Best Score': best_score}

        # Accumulate the best_k and best_score for averaging
        total_best_k += best_k
        total_best_score += best_score

    # Calculate the average best_k and best_score
    avg_best_k = total_best_k / num_variables

    # Print the average results
    print(f'\nAverage Optimal number of clusters: {avg_best_k:.2f} \n')

    return results

        

def mse_mae(value, name, ncluster):

    for i in range(len(value)):

        np.random.seed(42)

        X = np.array(value[i]).reshape(-1, 1)
        
        kmeans = KMeans(n_clusters=ncluster, random_state=42)
        y_pred = kmeans.fit_predict(X)

        y_true = np.random.randint(0, 3, size=len(X))

        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)

        print(f'MSE for {name[i]}: {mse:.4f}')
        print(f'MAE for {name[i]}: {mae:.4f}')
        
        print('\n')

if __name__ == '__main__':
    # Calculate the means
    
    value = [df['Situps'], df['Jumps'], df['Chins']]
    name = ['Situps', 'Jumps', 'Chins']

    cluster(value,  name)

    ncluster = int(input('Enter the number of clusters: '))
    print('\n')
    
    mse_mae(value, name, ncluster)
