# Import necessary libraries
import apache_beam as beam
from sklearn.datasets import load_linnerud as dataset
import pandas as pd
import os
import glob

# Get the current working directory (same folder as the script)
folder = os.getcwd()

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame for easier manipulation
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define the function to run the Apache Beam pipeline
def run_pipeline():
    output_path = os.path.join(folder, "chins_filtered")  # Path without extension

    # Create a pipeline using the DirectRunner (runs locally)
    with beam.Pipeline() as pipeline:
        
        # Create a PCollection from the 'Chins' column of the DataFrame
        input_data = (
            pipeline
            | 'Create Data' >> beam.Create(df[['Chins']].to_dict(orient='records'))
        )
        
        # Apply a transformation to filter values greater than 10
        output_data = (
            input_data
            | 'Filter Greater than 10' >> beam.Filter(lambda x: x['Chins'] > 10)
            | 'Format to CSV' >> beam.Map(lambda x: f"{x['Chins']}")
        )

        # Write the output to the current working folder
        output_data | 'Write to CSV' >> beam.io.WriteToText(output_path, file_name_suffix='.csv', header='Chins')

# Run the pipeline
if __name__ == '__main__':
    run_pipeline()

    # Find the generated CSV file and rename it
    generated_files = glob.glob(os.path.join(folder, "chins_filtered-*.csv"))
    if generated_files:
        final_path = os.path.join(folder, "chins_filtered.csv")
        os.rename(generated_files[0], final_path)  # Rename the file
        print(f"File saved to: {final_path}")
    else:
        print("No output file found!")