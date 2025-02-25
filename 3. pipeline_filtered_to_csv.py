# Import necessary libraries
import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format
import os  # OS module for file and directory operations
import glob  # Glob module to search for files with a specific pattern

# Get the current working directory
folder = os.getcwd()

# Create a new subfolder for storing the output
download_folder = os.path.join(folder, "download")
os.makedirs(download_folder, exist_ok=True)  # Ensure the folder exists

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Convert DataFrame to a list of dictionaries
data_list = df.to_dict(orient='records')

def extract_values(row):
    """Extracts values from the dictionary and returns them as a comma-separated string."""
    return ', '.join(map(str, row.values()))

def run_pipeline(output_csv_path):
    """Runs an Apache Beam pipeline to filter 'Chins' > 10 and save output to CSV."""
    
    with beam.Pipeline() as pipeline:
        filtered_data = (
            pipeline
            | 'Create Data' >> beam.Create(data_list)  # Convert DataFrame list to PCollection
            | 'Filter Chins > 10' >> beam.Filter(lambda row: row["Chins"] > 10)  # Keep only rows where "Chins" > 10
        )

        # Extract only values (omit field names)
        result_pcoll = filtered_data | 'Extract Values' >> beam.Map(extract_values)

        # Write output to CSV format
        result_pcoll | 'Write to CSV' >> beam.io.WriteToText(
        output_csv_path,
        file_name_suffix='.csv',
        num_shards=1,
        header="Chins,Situps,Jumps"
    )

        # Print results for debugging purposes
        result_pcoll | 'Print Results' >> beam.Map(print)

    print(f"Pipeline completed. Data saved to {output_csv_path}.csv")

if __name__ == '__main__':
    # Define output file path
    output_csv = os.path.join(download_folder, "chins_filtered")

    # Run Apache Beam pipeline
    run_pipeline(output_csv)

    # Rename the generated CSV file (optional step)
    generated_files = glob.glob(os.path.join(download_folder, "chins_filtered-*.csv"))
    if generated_files:
        final_path = os.path.join(download_folder, "chins_filtered_2.csv")
        os.rename(generated_files[0], final_path)
        print(f"File saved to: {final_path}")
    else:
        print("No output file found!")