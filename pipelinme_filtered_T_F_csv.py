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

# Convert DataFrame to a list of dictionaries (each row becomes a dictionary)
data_list = df.to_dict(orient='records')

def add_new_field(row):
    """Adds a new boolean field 'Chins(>10)' indicating whether 'Chins' is greater than 10."""
    row['Chins(>10)'] = row['Chins'] > 10  # Create a new field based on condition
    return row

def run_pipeline(output_csv_path):
    """Runs an Apache Beam pipeline to filter 'Chins' > 10 and save output to CSV."""
    
    with beam.Pipeline() as pipeline:
        # Create an initial PCollection from the data list
        pcoll = pipeline | 'Create PCollection' >> beam.Create(data_list)
        
        # Apply a transformation to add a new field based on the 'Chins' value
        result_pcoll = pcoll | 'Add New Field' >> beam.Map(add_new_field)
        
        # Print results for debugging purposes
        result_pcoll | 'Print Results' >> beam.Map(print)

        # Write output to CSV format
        result_pcoll | 'Write to CSV' >> beam.io.WriteToText(output_csv_path, file_name_suffix='.csv', header="Chins,Situps,Jumps,Chins(>10)")

    print(f"Pipeline completed. Data saved to {output_csv_path}.csv")

if __name__ == "__main__":

    # Define output file path
    output_csv = os.path.join(download_folder, "chins_filtered")

    run_pipeline(output_csv)

    # Rename the generated CSV file (optional step)
    generated_files = glob.glob(os.path.join(download_folder, "chins_filtered-*.csv"))
    if generated_files:
        final_path = os.path.join(download_folder, "chins_filtered_3.csv")
        os.rename(generated_files[0], final_path)
        print(f"File saved to: {final_path}")
    else:
        print("No output file found!")