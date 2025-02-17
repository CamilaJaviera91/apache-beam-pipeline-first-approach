# 🚀 Pipelines (First Approach)

## What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the next. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient processing.

## What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

### Install Apache Beam in Python

- To install Apache Beam in Python, follow these steps:

1. Install the Basic Apache Beam Package

```
pip install apache-beam
```

2. _Install Apache Beam with Google Cloud Support (Optional)_
    - _This includes additional dependencies for Google Cloud Storage, Pub/Sub, and BigQuery_

```
pip install apache-beam[gcp]
```

3. Verify Installation

```
import apache_beam as beam

print(beam.__version__)
```

## What's a DataFrame

✅ A **DataFrame** is a tabular structure for handling structured data in **Python**.<br>
✅ It is part of the **pandas library** and supports fast **data manipulation**.<br>
✅ It is widely used in **data science**, **analytics**, and **machine learning**.

### Install pandas

```
pip install pandas
```

### Install scikit-learn and call a Dataset

1. Install Using pip:

```
pip install scikit-learn
```

2. Verify Installation

```
import sklearn

print(sklearn.__version__)
```

3. Call a dataset to work with it.

```
from sklearn.datasets import load_linnerud
```

4. Transform it into a DataFrame.

```
from sklearn.datasets import load_linnerud

dt = dataset()
df = pd.DataFrame(dt.data, columns=dt.feature_names)

print(df)
```