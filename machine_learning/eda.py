import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hashlib
import io
from matplotlib.backends.backend_pdf import PdfPages

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

# Function to calculate file hash
def file_hash(filepath):
    """Calculates the SHA256 hash of a file."""
    if not os.path.exists(filepath):
        return None
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Function to save a PDF only if it has changed
def save_if_modified(new_filepath, pdf_buffer):
    """Saves the PDF only if the file is new or has changed."""
    new_hash = hashlib.sha256(pdf_buffer.getvalue()).hexdigest()
    existing_hash = file_hash(new_filepath)

    if existing_hash != new_hash:
        with open(new_filepath, 'wb') as f:
            f.write(pdf_buffer.getvalue())
        print(f"File saved: {new_filepath}")
    else:
        print(f"No changes detected. File not saved: {new_filepath}")

# ---------------------------
# Create Dataset Report PDF
# ---------------------------
pdf_buffer = io.BytesIO()
with PdfPages(pdf_buffer) as pdf:
    # First Rows Table
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.head().values, colLabels=df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.title('First Rows of the Dataset', fontsize=14)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

    # Dataset Summary (Structure & Null Values)
    buffer = io.StringIO()
    df.info(buf=buffer)
    structure_str = buffer.getvalue()
    nulls_str = df.isnull().sum().to_string()

    text_content = f"Dataset Structure:\n{structure_str}\n\nNull Values:\n{nulls_str}"
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    ax.text(0.01, 0.99, text_content, ha='left', va='top', fontsize=10, wrap=True, transform=ax.transAxes)
    plt.title('Dataset Summary', fontsize=14)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

save_if_modified(output_path_r, pdf_buffer)

# ---------------------------
# Create Histogram PDF
# ---------------------------
pdf_buffer = io.BytesIO()
with PdfPages(pdf_buffer) as pdf:
    for feature in df.columns:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        sns.histplot(df[feature], ax=ax)
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        plt.title(f'Histogram of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        pdf.savefig()
        plt.close()

save_if_modified(output_path_h, pdf_buffer)

# ---------------------------
# Create Density Plots PDF
# ---------------------------
pdf_buffer = io.BytesIO()
with PdfPages(pdf_buffer) as pdf:
    numeric_columns = df.select_dtypes(include=['number']).columns
    for feature in numeric_columns:
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        sns.kdeplot(data=df, x=feature, fill=True, ax=ax)
        plt.title(f'Density Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Density')
        pdf.savefig()
        plt.close()

save_if_modified(output_path_d, pdf_buffer)