import apache_beam as beam
from sklearn.datasets import load_linnerud as dataset
import pandas as pd

dt = dataset()
df = pd.DataFrame(dt.data, columns=dt.feature_names)

def run_pipeline():

    with beam.Pipeline() as pipeline:
        
        input_data = (
            pipeline
            | 'Create Data' >> beam.Create(df['Chins'].tolist())
        )
        
        output_data = (
            input_data
            | 'Greater than 10' >> beam.Map(lambda x: x > 10)
        )

        output_data | 'Collect Results' >> beam.Map(print)

if __name__ == '__main__':
    run_pipeline()