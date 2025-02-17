# 🚀 Pipelines (First Approach)

## ➰ What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the next. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient processing.

## 🅱️ What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

### Install Apache Beam in Python

- To install Apache Beam in Python, follow these steps:

1️⃣ Install Using pip:

```
pip install apache-beam
```

2️⃣ _Install Apache Beam with Google Cloud Support (Optional)_: <br>
    - _This includes additional dependencies for Google Cloud Storage, Pub/Sub, and BigQuery_

```
pip install apache-beam[gcp]
```

3️⃣ Verify Installation:

```
import apache_beam as beam

print(beam.__version__)
```

## 📄 What's a DataFrame

✅ A **DataFrame** is a tabular structure for handling structured data in **Python**.<br>
✅ It is part of the **pandas library** and supports fast **data manipulation**.<br>
✅ It is widely used in **data science**, **analytics**, and **machine learning**.

### Install pandas

1️⃣ Install Using pip:

```
pip install pandas
```

2️⃣ Verify Installation: <br>

```
import pandas as pd

print(pd.__version__)
```

### Install scikit-learn and call a Dataset

1️⃣ Install Using pip: <br>

```
pip install scikit-learn
```

2️⃣ Verify Installation: <br>

```
import sklearn

print(sklearn.__version__)
```

3️⃣ Call a dataset to work with it: <br>

```
from sklearn.datasets import load_linnerud
```

4️⃣ Transform it into a DataFrame: <br>

```
from sklearn.datasets import load_linnerud

dt = dataset()
df = pd.DataFrame(dt.data, columns=dt.feature_names)

print(df)
```

---

## 💻 pipeline.py

### 👨‍💻 Explanation of the Code:

1️⃣ **Import Libraries:** <br>

- **apache_beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.    
- **pandas:** A powerful data manipulation library for handling structured data.

2️⃣ **Load and Prepare Data:** <br>

- The Linnerud dataset is loaded and converted into a Pandas DataFrame for easier manipulation.

3️⃣ **Define the Pipeline:** <br>

- A function run_pipeline is defined to encapsulate the pipeline logic.
- Within this function, a pipeline is created using the with statement, ensuring proper resource management.

4️⃣ **Create PCollection:** <br>

- The 'Chins' column from the DataFrame is converted to a list and then to a PCollection using beam.Create.

5️⃣ **Apply Transformation:** <br>

- A transformation is applied to the **PCollection** to check if each value is greater than 10. This is done using **beam.Map** with a **lambda** function.

6️⃣ **Output Results:** <br>

The results are printed to the console using **beam.Map(print)**.

7️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.