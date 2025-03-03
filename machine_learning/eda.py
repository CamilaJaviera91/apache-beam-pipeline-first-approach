import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import io

# Set a style for the plots
sns.set_style('whitegrid')

# Load the dataset from the specified CSV file.
df = pd.read_csv('./download/chins_filtered_7.csv')

# Ensure the output directory exists
output_dir = './download'
os.makedirs(output_dir, exist_ok=True)
output_path_h = os.path.join(output_dir, 'histogram.pdf')
output_path_r = os.path.join(output_dir, 'dataset_report.pdf')

# Capture outputs as strings
head_str = df.head().to_string()
nulls_str = df.isnull().sum().to_string()
buffer = io.StringIO()
df.info(buf=buffer)
structure_str = buffer.getvalue()

# Combine the strings
text_content = f"First rows of the dataset:\n{head_str}\n\nStructure:\n{structure_str}\n\nNull values:\n{nulls_str}"

with PdfPages(output_path_r) as pdf:
    # Create a figure
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')  # Hide the axes

    # Add the text to the figure
    ax.text(0.5, 0.5, text_content, ha='center', va='center', fontsize=10, wrap=True)

    # Save the figure to the PDF
    pdf.savefig(fig)
    plt.close(fig)

print("PDF file created successfully!")

# Create a PDF file with the plots
with PdfPages(output_path_h) as pdf:
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