# Import necessary libraries
import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame for easier manipulation
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define the function to run the Apache Beam pipeline
def run_pipeline(output_path):

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

        # Print results for debugging purposes
        output_data | 'Print Results' >> beam.Map(print)

        # Write the output data to a CSV file in the specified output path
        output_data | 'Write Results' >> beam.io.WriteToText(output_path, shard_name_template='', header='Chins')

# Run the pipeline if the script is executed as the main program
if __name__ == '__main__':
    
    # Define output file path
    output_path = './download/chins_filtered_1.csv'
    
    run_pipeline(output_path)  # Execute the Apache Beam pipeline