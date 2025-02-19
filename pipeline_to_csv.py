# Import necessary libraries
import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format
import os  # OS module for file and directory operations
import glob  # Glob module to search for files with a specific pattern

# Get the current working directory (same folder as the script)
folder = os.getcwd()

# Create a new subfolder inside the current working directory for storing the downloaded data
download = "download"
download = os.path.join(folder, download)  # Path to the download folder

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame for easier manipulation
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define the function to run the Apache Beam pipeline
def run_pipeline():
    # Define the output path where the filtered data will be saved
    output_path = os.path.join(download, "chins_filtered")  # Path without file extension

    # Create a pipeline using the DirectRunner (runs locally)
    with beam.Pipeline() as pipeline:
        
        # Create a PCollection from the 'Chins' column of the DataFrame
        input_data = (
            pipeline
            | 'Create Data' >> beam.Create(df[['Chins']].to_dict(orient='records'))  # Convert 'Chins' column to a PCollection
        )
        
        # Apply a transformation to filter values greater than 10 in the 'Chins' column
        output_data = (
            input_data
            | 'Filter Greater than 10' >> beam.Filter(lambda x: x['Chins'] > 10)  # Filter out rows where 'Chins' <= 10
            | 'Format to CSV' >> beam.Map(lambda x: f"{x['Chins']}")  # Format the data to a CSV-friendly string format
        )

        # Write the output data to a CSV file in the specified output path
        output_data | 'Write to CSV' >> beam.io.WriteToText(output_path, file_name_suffix='.csv', header='Chins')

# Run the pipeline if the script is executed as the main program
if __name__ == '__main__':
    run_pipeline()  # Execute the Apache Beam pipeline

    # After running the pipeline, find the generated CSV file and rename it
    generated_files = glob.glob(os.path.join(download, "chins_filtered-*.csv"))  # Search for CSV files in the output folder
    if generated_files:  # Check if any output files were found
        final_path = os.path.join(download, "chins_filtered.csv")  # Define the final path with a standardized name
        os.rename(generated_files[0], final_path)  # Rename the first generated file to the final path
        print(f"File saved to: {final_path}")  # Print confirmation message
    else:
        print("No output file found!")  # Print error message if no output file is generated