# 🚀 Pipelines (First Approach)

## What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the next. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient processing.

## What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

### How to Install Apache Beam in Python

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