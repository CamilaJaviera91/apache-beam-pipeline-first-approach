import os
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import io

# Set a style for the plots
sns.set_style('whitegrid')

# Load the dataset from the specified CSV file.
df = pd.read_csv('./src/download/chins_filtered_7.csv')

# Ensure the output directory exists
output_dir = './download'
os.makedirs(output_dir, exist_ok=True)

# File paths
output_paths = {
    "histogram": os.path.join(output_dir, 'histogram.pdf'),
    "density_analysis": os.path.join(output_dir, 'density_analysis.pdf'),
    "dataset_report": os.path.join(output_dir, 'dataset_report.pdf')
}

def file_hash(filepath):
    """Returns SHA-256 hash of a file, or None if it does not exist."""
    if not os.path.exists(filepath):
        return None
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):  # Read in 4 KB chunks
            hasher.update(chunk)
    return hasher.hexdigest()

def files_are_equal(filepath, temp_filepath):
    """Compares two files using SHA-256 hash and byte content."""
    if not os.path.exists(filepath):
        return False  # If original file does not exist, consider it different
    return file_hash(filepath) == file_hash(temp_filepath)

# 1️⃣ 📜 **Dataset Summary PDF**
temp_report_path = output_paths["dataset_report"] + ".temp"
with PdfPages(temp_report_path) as pdf:
    # Capture dataset info
    head_str = df.head().to_string()
    nulls_str = df.isnull().sum().to_string()
    buffer = io.StringIO()
    df.info(buf=buffer)
    structure_str = buffer.getvalue()

    # **Page 1: Table with First Rows**
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

    # **Page 2: Data Structure & Null Values**
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')
    text_content = f"Dataset Structure:\n{structure_str}\n\nNull Values:\n{nulls_str}"
    ax.text(0.01, 0.99, text_content, ha='left', va='top', fontsize=10, wrap=True, transform=ax.transAxes)
    plt.title('Dataset Summary', fontsize=14)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close(fig)

if not files_are_equal(output_paths["dataset_report"], temp_report_path):
    os.replace(temp_report_path, output_paths["dataset_report"])
    print(f"✅ File saved: {output_paths['dataset_report']}")
else:
    os.remove(temp_report_path)
    print(f"⚠️ No changes detected: {output_paths['dataset_report']}")

# 2️⃣ 📊 **Histogram PDF**
temp_histogram_path = output_paths["histogram"] + ".temp"
with PdfPages(temp_histogram_path) as pdf:
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

if not files_are_equal(output_paths["histogram"], temp_histogram_path):
    os.replace(temp_histogram_path, output_paths["histogram"])
    print(f"✅ File saved: {output_paths['histogram']}")
else:
    os.remove(temp_histogram_path)
    print(f"⚠️ No changes detected: {output_paths['histogram']}")

# 3️⃣ 📈 **Density Analysis PDF**
temp_density_path = output_paths["density_analysis"] + ".temp"
with PdfPages(temp_density_path) as pdf:
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

if not files_are_equal(output_paths["density_analysis"], temp_density_path):
    os.replace(temp_density_path, output_paths["density_analysis"])
    print(f"✅ File saved: {output_paths['density_analysis']}")
else:
    os.remove(temp_density_path)
    print(f"⚠️ No changes detected: {output_paths['density_analysis']}")