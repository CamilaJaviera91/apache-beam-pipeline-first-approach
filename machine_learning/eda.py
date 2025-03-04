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
output_path_d = os.path.join(output_dir, 'density_analysis.pdf')
output_path_r = os.path.join(output_dir, 'dataset_report.pdf')

# Capture outputs as strings
head_str = df.head().to_string()
nulls_str = df.isnull().sum().to_string()
buffer = io.StringIO()
df.info(buf=buffer)
structure_str = buffer.getvalue()

# Combine the strings
text_content = f"First rows of the dataset:\n{head_str}\n\nStructure:\n{structure_str}\n\nNull values:\n{nulls_str}"

# Create a PDF file for dataset summary
with PdfPages(output_path_r) as pdf:
    
    # **Page 1: Table with First Rows**
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')

    # Convert df.head() to a table
    table = ax.table(cellText=df.head().values,  
                     colLabels=df.columns,
                     loc='center',
                     cellLoc='center')

    # Formatting
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)

    plt.title('First Rows of the Dataset', fontsize=14)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # **Page 2: Data Structure & Null Values**
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')  # Hide axes

    text_content = f"Dataset Structure:\n{structure_str}\n\nNull Values:\n{nulls_str}"
    ax.text(0.01, 0.99, text_content, ha='left', va='top', fontsize=10, wrap=True, transform=ax.transAxes)

    plt.title('Dataset Summary', fontsize=14)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

print("PDF file created successfully!")

# Create a PDF file with histograms
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

# Create a PDF file with histograms
with PdfPages(output_path_d) as pdf:
    # Identify outliers and understand the distribution of each variable.
    for feature in df.columns:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()  # Get the current axis
        
        # Create the KDE plot for the current feature
        sns.kdeplot(data=df, x=feature, shade=True, ax=ax)
        
        plt.title(f'Density Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Density')
        
        # Save the current figure to the PDF
        pdf.savefig()
        plt.close()

print('PDF file created successfully!')