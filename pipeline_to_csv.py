# Import necessary libraries
import apache_beam as beam
from sklearn.datasets import load_linnerud as dataset
import pandas as pd
import os
import glob  # To dynamically find the generated file

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame for easier manipulation
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define the function to run the Apache Beam pipeline
def run_pipeline():
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

        # Write the output to a CSV file
        output_data | 'Write to CSV' >> beam.io.WriteToText('chins_filtered', file_name_suffix='.csv', header='Chins')

# Run the pipeline
if __name__ == '__main__':
    run_pipeline()

    # Find the generated CSV file and rename it
    generated_files = glob.glob('chins_filtered-*.csv')  # Find the file with Beam's suffix
    if generated_files:
        os.rename(generated_files[0], 'chins_filtered.csv')  # Rename to desired filename
        print(f"File renamed to: chins_filtered.csv")
    else:
        print("No output file found!")