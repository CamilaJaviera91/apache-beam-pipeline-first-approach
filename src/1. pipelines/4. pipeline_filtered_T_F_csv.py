import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Convert DataFrame to a list of dictionaries (each row becomes a dictionary)
data_list = df.to_dict(orient='records')

def extract_values(row):
    """Extracts values from the dictionary and returns them as a comma-separated string."""
    return ', '.join(map(str, row.values()))

def add_new_field(row):
    """Adds a new boolean field 'Chins(>10)' indicating whether 'Chins' is greater than 10."""
    row['Chins(>10)'] = row['Chins'] > 10  # Create a new field based on condition
    return row

def run_pipeline(output_path):
    """Runs an Apache Beam pipeline to filter 'Chins' > 10 and save output to CSV."""
    
    with beam.Pipeline() as pipeline:
        # Create a PCollection from the data list
        pcoll = pipeline | 'Create PCollection' >> beam.Create(data_list)
        
        # Add new field
        result_pcoll = pcoll | 'Add New Field' >> beam.Map(add_new_field)

        # Extract only values
        result_pcoll = result_pcoll | 'Extract Values' >> beam.Map(extract_values)

        # Print results for debugging
        result_pcoll | 'Print Results' >> beam.Map(print)

        # Write output to a single CSV file
        result_pcoll | 'Write Results' >> beam.io.WriteToText(output_path, shard_name_template='', header='Chins,Situps,Jumps,Chins(>10)')

    print(f"Pipeline completed. Data saved to {output_path}.csv")

if __name__ == "__main__":

    # Define output file path
    output_path = './src/download/chins_filtered_3.csv'

    run_pipeline(output_path)