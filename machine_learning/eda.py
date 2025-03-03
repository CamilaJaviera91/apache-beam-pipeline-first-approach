import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the specified CSV file.
df = pd.read_csv('./download/chins_filtered_7.csv')

# Check first rows of the dataset
print(df.head())

# Check structure of the dataset
print(df.info())

# Check for null values
print(df.isnull().sum())

# Identify outliers and understand the distribution of each variable.
for feature in df.columns:
    sns.histplot(df[feature])
    
    for container in plt.gca().containers:
        plt.gca().bar_label(container, fmt='%d')

    plt.title(f'Hitogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()