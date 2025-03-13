import apache_beam as beam # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset  # Load the Linnerud dataset from scikit-learn
import pandas as pd  # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define bins and labels for categorizing the 'Chins' data
bins = [0, 5, 10, 15, 20, 25, 30]
labels = ['0', '5', '10', '15', '20', '25']

# Create a new column 'Chins Range' by categorizing 'Chins' into defined ranges
df['Chins Range'] = pd.cut(df['Chins'], bins=bins, labels=labels, right=False)

# Convert DataFrame to a list of dictionaries (each row becomes a dictionary)
data_list = df.to_dict(orient='records')

def add_comparison_field(row, average_chins):
    """Adds a 'Chins_vs_Avg' field indicating whether 'Chins' is above or below average."""
    
    row['Chins_vs_Avg'] = 'Above Average' if row['Chins'] > average_chins else 'Below Average'
    return row

def extract_values(row):
    """Extracts values from the dictionary and returns them as a comma-separated string."""
    
    return ', '.join(map(str, row.values()))

def run_pipeline(output_path):
    
    with beam.Pipeline() as pipeline:
        
        # Create a PCollection from the data list
        pcoll = pipeline | 'Create PCollection' >> beam.Create(data_list)
        
        # Calculate the average of 'Chins'
        average_chins = (
            pcoll
            | 'Extract Chins' >> beam.Map(lambda row: row['Chins'])
            | 'Calculate Mean' >> beam.CombineGlobally(beam.combiners.MeanCombineFn())
        )

        # Apply the comparison for each element using the side input
        result_pcoll = (
            pcoll
            | 'Add Comparison Field' >> beam.Map(
                lambda row, avg_chins: add_comparison_field(row, avg_chins),
                beam.pvalue.AsSingleton(average_chins)  # Side input
            )
            | 'Format Rows' >> beam.Map(extract_values)
        )

        # Write the results to a CSV file
        result_pcoll | 'Write Results' >> beam.io.WriteToText(
            output_path,
            shard_name_template='',
            header='Chins,Situps,Jumps,Chins_Range,Chins_vs_Avg'
        )

        result_pcoll | 'Print Results' >> beam.Map(print)

    print(f"Pipeline completed. Data saved to {output_path}")

if __name__ == "__main__":

    # Define output file path
    output_path = './src/download/chins_filtered_6.csv'
    
    run_pipeline(output_path)