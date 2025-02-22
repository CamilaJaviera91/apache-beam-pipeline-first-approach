# 🚀 Pipelines (First Approach)

## ➰ What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the next. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient processing.

## 🅱️ What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

# 👨‍💻 Preparing to code 

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

dt = load_linnerud()  
df = pd.DataFrame(dt.data, columns=dt.feature_names)

print(df)
```

---

# 🛠 Code Explanation 

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

- The **PCollection** undergoes a transformation where each value is checked to determine if it exceeds 10. This is implemented using **beam.Map** with a **lambda** function for efficiency.

6️⃣ **Output Results:** <br>

The results are printed to the console using **beam.Map(print)**.

7️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.

---

## 💻 pipeline_to_csv.py

### 👨‍💻 Explanation of the Code:

1️⃣ **Importing Libraries:** <br>

- **Apache Beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.
- **Pandas:** A powerful data manipulation library for handling structured data.
- **OS & Glob:** Used for file and directory management.

2️⃣ **Setting Up File PathsSetting Up File Paths:** <br>

- **os.getcwd()** fetches the current working directory.
- The download folder will be created inside this directory to store processed files.

3️⃣ **Load and Prepare Data:** <br>

- The **Linnerud dataset** is loaded and converted into a **Pandas DataFrame** for easier manipulation.

4️⃣ **Apache Beam Pipeline:** <br>

- **Pipeline Breakdown**
    1. **beam.Pipeline():** Initializes an Apache Beam pipeline.
    2. **beam.Create(df[['Chins']].to_dict(orient='records')):** 
        - Extracts the "Chins" column from the DataFrame.
        - Converts it into a PCollection (a distributed dataset in Apache Beam).
    3. **beam.Filter(lambda x: x['Chins'] > 10):**
        - Filters out all rows where "Chins" ≤ 10.
    4. **beam.Map(lambda x: f"{x['Chins']}"):**
        - Formats the filtered values into a string format suitable for writing to a CSV file.
    5. **beam.io.WriteToText(output_path, file_name_suffix='.csv', header='Chins'):**
        - Writes the output into a CSV file with a header.

5️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.

6️⃣ **Renaming the Output File:** <br>

- Finds the output file generated by Apache Beam (since Beam appends a suffix like -00000-of-00001.csv).
- Renames it to a standardized name chins_filtered.csv.
- Prints confirmation or an error message.

---

## pipeline_to_dataframa.py 💻

### 👨‍💻 Explanation of the Code:

1️⃣ **Importing Libraries:** <br>

- **Apache Beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.
- **Pandas:** A powerful data manipulation library for handling structured data.
- **OS & Glob:** Used for file and directory management.

2️⃣ **Setting Up File PathsSetting Up File Paths:** <br>

- **os.getcwd()** fetches the current working directory.
- The download folder will be created inside this directory to store processed files.

3️⃣ **Load and Prepare Data:** <br>

- The **Linnerud dataset** is loaded and converted into a **Pandas DataFrame** for easier manipulation.

3️⃣ **Loading and Transforming the Dataset** <br>

- Loads the **Linnerud dataset**, which contains exercise-related data with three features:
    - "Chins" (pull-ups)
    - "Situps" (sit-ups)
    - "Jumps" (jumps)
- Converts the **dataset** into a **Pandas DataFrame**.
- Transforms it into a **list of dictionaries** (data_list) to be used with **Apache Beam**.

