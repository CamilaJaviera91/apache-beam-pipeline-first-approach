import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

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

def run_pipeline():
    """Runs an Apache Beam pipeline to filter 'Chins' > 10 and save output to CSV."""
    
    with beam.Pipeline() as pipeline:
        # Create an initial PCollection from the data list
        pcoll = pipeline | 'Create PCollection' >> beam.Create(data_list)
        
        # Apply a transformation to add a new field based on the 'Chins' value
        result_pcoll = pcoll | 'Add New Field' >> beam.Map(add_new_field)
        
        # Print results for debugging purposes
        result_pcoll | 'Print Results' >> beam.Map(print)

if __name__ == "__main__":
    run_pipeline()C