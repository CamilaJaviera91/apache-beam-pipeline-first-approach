# Import necessary libraries
import apache_beam as beam  # Apache Beam for data processing
from sklearn.datasets import load_linnerud as dataset  # Linnerud dataset from scikit-learn
import pandas as pd  # pandas for data manipulation

# Load the Linnerud dataset
dt = dataset()
# Convert the dataset into a pandas DataFrame with appropriate column names
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define bins and labels for categorizing the 'Chins' data
bins = [0, 5, 10, 15, 20, 25, 30]
labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30']
# Create a new column 'Chins Range' by categorizing 'Chins' into defined ranges
df['Chins Range'] = pd.cut(df['Chins'], bins=bins, labels=labels, right=False)

# Extract the 'Chins Range' column as a list
data_list = df['Chins Range']

# Define the function to run the Apache Beam pipeline
def run_pipeline(output_path):
    # Initialize the Apache Beam pipeline
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
        # Print each result to the console
        data | 'Print Results' >> beam.Map(print)
        # Write the results to a text file at the specified output path
        data | 'Write Results' >> beam.io.WriteToText(output_path, shard_name_template='')

# Check if the script is being run directly
if __name__ == "__main__":
    # Define the output file path
    output_path = './download/chins_filtered_4.csv'
    # Run the pipeline with the specified output path
    run_pipeline(output_path)