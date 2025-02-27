# Import necessary libraries
import apache_beam as beam  # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Convert DataFrame to a list of dictionaries
data_list = df.to_dict(orient='records')

def extract_values(row):
    """Extracts values from the dictionary and returns them as a comma-separated string."""
    return ', '.join(map(str, row.values()))

def run_pipeline(output_path):
    """Runs an Apache Beam pipeline to filter 'Chins' > 10 and save output to CSV."""
    
    with beam.Pipeline() as pipeline:
        filtered_data = (
            pipeline
            | 'Create Data' >> beam.Create(data_list)  # Convert DataFrame list to PCollection
            | 'Filter Chins > 10' >> beam.Filter(lambda row: row["Chins"] > 10)  # Keep only rows where "Chins" > 10
        )

        # Extract only values (omit field names)
        result_pcoll = filtered_data | 'Extract Values' >> beam.Map(extract_values)

        # Write output to CSV format
        result_pcoll | 'Write Results' >> beam.io.WriteToText(output_path, shard_name_template='', header='Chins,Situps,Jumps')

        # Print results for debugging purposes
        result_pcoll | 'Print Results' >> beam.Map(print)

    print(f"Pipeline completed. Data saved to {output_path}.csv")

if __name__ == '__main__':

    # Define output file path
    output_path = './download/chins_filtered_2.csv'

    # Run Apache Beam pipeline
    run_pipeline(output_path)