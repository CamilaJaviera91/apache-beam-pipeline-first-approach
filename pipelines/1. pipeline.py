import apache_beam as beam  # Apache Beam for data processing
from sklearn.datasets import load_linnerud as dataset  # Importing the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for data manipulation

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
            | 'Create Data' >> beam.Create(df['Chins'].tolist())  # Convert the 'Chins' column to a list and create a PCollection
        )
        
        # Apply a transformation to filter values greater than 10
        output_data = (
            input_data
            | 'Greater than 10' >> beam.Map(lambda x: x > 10)  # Check if each value is greater than 10
        )

        # Output the results by printing each element
        output_data | 'Collect Results' >> beam.Map(print)  # Print each element in the output_data PCollection

# Entry point of the script
if __name__ == '__main__':
    run_pipeline()  # Execute the pipeline