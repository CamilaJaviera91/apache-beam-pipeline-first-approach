import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Set a style for the plots
sns.set_style('whitegrid')

# Load the dataset from the specified CSV file.
df = pd.read_csv('./download/chins_filtered_7.csv')

# Check first rows of the dataset
print(df.head())

# Check structure of the dataset
print(df.info())

# Check for null values
print(df.isnull().sum())

# Ensure the output directory exists
output_dir = './download'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'histogram.pdf')

# Create a PDF file with the plots
with PdfPages(output_path) as pdf:
    # Identify outliers and understand the distribution of each variable.
    for feature in df.columns:
        plt.figure(figsize=(10, 6))  # Optionally set the figure size
        ax = plt.gca()
        sns.histplot(df[feature], ax=ax)
        
        # Add bar labels if containers are present
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        
        plt.title(f'Histogram of {feature}')  # Corrected typo: "Hitogram" -> "Histogram"
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        
        # Save the current figure to the PDF
        pdf.savefig()
        plt.close()

print('PDF file created successfully!')