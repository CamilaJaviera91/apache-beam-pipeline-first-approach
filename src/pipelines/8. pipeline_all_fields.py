import apache_beam as beam # Apache Beam for data processing pipeline
from sklearn.datasets import load_linnerud as dataset # Load the Linnerud dataset from scikit-learn
import pandas as pd # Pandas for handling data in DataFrame format

# Load the Linnerud dataset
dt = dataset()

# Convert the dataset into a Pandas DataFrame
df = pd.DataFrame(dt.data, columns=dt.feature_names)

# Define bins and labels for categorizing the data
bins = {
    'Chins': [0, 5, 10, 15, 20, 25, 30],
    'Situps': [0, 50, 100, 150, 200, 250, 300],
    'Jumps': [0, 25, 50, 75, 100, 125, 150]
}

labels = {
    'Chins': ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30'],
    'Situps': ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300'],
    'Jumps': ['0-25', '25-50', '50-75', '75-100', '100-125', '125-150']
}

# Categorize data into defined ranges
for feature in dt.feature_names:
    df[f'{feature} Range'] = pd.cut(df[feature], bins=bins[feature], labels=labels[feature], right=False)

df['User'] = [f'User {i+1}' for i in range(len(df))]

# Convert DataFrame to a list of dictionaries (each row becomes a dictionary)
data_list = df.to_dict(orient='records')

def add_comparison_fields(row, averages):
    """Adds a new field indicating whether the new field is above or below average."""
    for feature in averages:
        row[f'{feature}_vs_Avg'] = 'Above Average' if row[feature] > averages[feature] else 'Below Average'
    return row

def extract_values(row):
    """Extracts values from the dictionary and returns them as a comma-separated string."""
    return ', '.join(map(str, row.values()))

def run_pipeline(output_path):
    with beam.Pipeline() as pipeline:
        # Create a PCollection from the data list
        pcoll = pipeline | 'Create PCollection' >> beam.Create(data_list)

        # Create a PCollection of (feature, value) tuples
        feature_value_pairs = (
            pcoll
            | 'Create Feature-Value Pairs' >> beam.FlatMap(
                lambda row: [(feature, row[feature]) for feature in dt.feature_names]
            )
        )

        # Calculate the mean for each feature
        averages = (
            feature_value_pairs
            | 'Group by Feature' >> beam.GroupByKey()
            | 'Calculate Feature Means' >> beam.Map(
                lambda feature_values: (feature_values[0], sum(feature_values[1]) / len(feature_values[1]))
            )
        )

        # Apply the comparison for each element using the side input
        result_pcoll = (
            pcoll
            | 'Add Comparison Fields' >> beam.Map(
                lambda row, avgs: add_comparison_fields(row, avgs),
                beam.pvalue.AsDict(averages)
            )
            | 'Format Rows' >> beam.Map(extract_values)
        )

        # Write the results to a CSV file
        result_pcoll | 'Write Results' >> beam.io.WriteToText(
            output_path,
            shard_name_template='',
            header=','.join(df.columns) + ',Chins_vs_Avg,Situps_vs_Avg,Jumps_vs_Avg'
        )

        result_pcoll | 'Print Results' >> beam.Map(print)

    print(f"Pipeline completed. Data saved to {output_path}")

if __name__ == "__main__":
    # Define output file path
    output_path = './src/download/chins_filtered_7.csv'
    run_pipeline(output_path)