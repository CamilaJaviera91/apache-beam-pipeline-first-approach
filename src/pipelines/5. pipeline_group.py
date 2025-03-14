import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define bins and labels for categorizing the 'Chins' data
bins   = [0, 5, 10, 15, 20, 25, 30]
labels = [0, 5, 10, 15, 20, 25]

# Create a new column 'Chins Range' by categorizing 'Chins' into defined ranges
df['Chins Range'] = pd.cut(df['Chins'], bins=bins, labels=labels, right=False)

# Extract the 'Chins Range' column as a list
data_list = df['Chins Range']


def run_pipeline(output_path):
    """Define the function to run the Apache Beam pipeline."""

    with beam.Pipeline() as pipeline:

        # Define the data processing steps
        data = (
            pipeline
            # Create a PCollection from the data_list
            | 'Create PCollection' >> beam.Create(data_list)

            # Count the occurrences of each unique element in the PCollection
            | 'Count Elements' >> beam.combiners.Count.PerElement()
            
            # Format the results as CSV strings
            | 'Format Results' >> beam.Map(lambda x: f'{x[0]},{x[1]}')
        )

        # Print results for debugging
        data | 'Print Results' >> beam.Map(print)
        
        # Write output to a single CSV file
        data | 'Write Results' >> beam.io.WriteToText(output_path, shard_name_template='', header='Chins_Range,Count')

if __name__ == "__main__":

    # Define output file path
    output_path = './src/download/chins_filtered_4.csv'
    
    # Run the pipeline with the specified output path
    run_pipeline(output_path)