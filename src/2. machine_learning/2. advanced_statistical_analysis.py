import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# Load the dataset from the specified CSV file.
df = pd.read_csv('./src/download/chins_filtered_7.csv')

def hypothesis_testing(value_mean, name):
    for i, mean in enumerate(value_mean):
        # Wrap around when accessing the next mean and its corresponding name
        next_i = (i + 1) % len(value_mean)
        next_mean = value_mean[next_i]
        next_name = name[next_i]

        print(f"Mean {name[i]}: {mean}")
        print(f"Mean {next_name}: {next_mean}")

        # Generate random data for group_a and group_b with the current and next mean
        group_a = np.random.normal(loc=mean, scale=10, size=30)
        group_b = np.random.normal(loc=next_mean, scale=10, size=30)

        # Perform t-test to compare the means of the two groups
        t_stat, p_value = stats.ttest_ind(group_a, group_b)
        
        print(f"T-statistic: {t_stat:.4f}")
        print(f"P-value: {p_value:.4f}")

        if p_value < 0.05:
            print("We reject the null hypothesis: the means are significantly different.")
        else:
            print("There is not enough evidence to reject the null hypothesis.")

        print('\n')

def clustering(value, name):
    for i in range(len(value)):
        next_index = (i + 1) % len(value)

        # Convert to DataFrame for processing
        data = pd.DataFrame({name[i]: value[i], name[next_index]: value[next_index]})

        # Scale the data using StandardScaler
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)

        # Elbow method for selecting the optimal number of clusters (k)
        inertia = []
        K_range = range(2, 11)  # Fix: Start from k=2

        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
            kmeans.fit(data_scaled)
            inertia.append(kmeans.inertia_)

        # Plot inertia (sum of squared errors) for different values of k
        plt.figure(figsize=(8, 5))
        plt.plot(K_range, inertia, marker='o')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Inertia (SSE)')
        plt.title(f'Elbow Method for k selection (Iteration {i})')
        plt.show()

        # Apply K-Means clustering with 2 clusters (chosen based on elbow method)
        kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(data_scaled)

        # Convert scaled data back to DataFrame for visualization
        data = pd.DataFrame(data_scaled, columns=[name[i], name[next_index]])
        data['Cluster'] = clusters

        # Scatter plot with clusters
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=data[name[i]], y=data[name[next_index]], hue=data['Cluster'], palette='viridis')
        plt.xlabel(name[i])
        plt.ylabel(name[next_index])
        plt.title(f'Customer Segmentation with K-Means (Iteration {i})')
        plt.show()

        # Compute silhouette score to evaluate the clustering quality
        silhouette_avg = silhouette_score(data_scaled, clusters)
        print(f'Iteration {i} - Silhouette Score: {silhouette_avg:.2f}')
        
        print('\n')
        
if __name__ == '__main__':
    # Calculate the means for the specified ranges
    value = [df['Situps Range'], df['Jumps Range'], df['Chins Range']]
    value_mean = [float(df['Situps Range'].mean()), float(df['Jumps Range'].mean()), float(df['Chins Range'].mean())]
    name = ['Situps', 'Jumps', 'Chins']

    # Perform hypothesis testing to compare the means
    hypothesis_testing(value_mean, name)    
    # Perform clustering using K-Means
    clustering(value, name)