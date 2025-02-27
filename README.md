# 🚀 Pipelines (First Approach)

## ➰ What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the next. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient processing.

![Pipeline](./images/pic1.png)

## 🅱️ What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

![Apache](./images/pic2.png)

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

![Dataframe](./images/pic3.png)

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

# 🛠 Code Explanation - pipeline folder

## 💻 1. pipeline.py

### 👨‍💻 Explanation of the Code:

- This **code** will check if the **'Chins'** field meets the condition:
    - If **'Chins'** is **greater than 10**.
    - It will only display **'True'** or **'False'** if **'Chins'** meets the previous condition."

### 👣 Steps

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

8️⃣ **Example Output:**

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
15     250     80
```

- **Output .csv (Chins > 10)**

```
Chins
False
False
True
True
```


---

## 💻 2. pipeline_to_csv.py

### 👨‍💻 Explanation of the Code:

- This **code** will check if the **'Chins'** field meets the condition:
    - If **'Chins'** is **greater than 10**.
    - Only the **'Chins'** field will be displayed, along with whether it meets the previous condition.

### 👣 Steps

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


7️⃣ **Example Output:**

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
15     250     80
```

- **Output .csv (Chins > 10)**

```
Chins
12
15
```

---

## 💻 3. pipeline_to_dataframe.py

### 👨‍💻 Explanation of the Code:

- This **code** will check if the **'Chins'** field meets the condition:
    - If **'Chins'** is **greater than 10**.
    - It will display all fields if the **'Chins'** field meets the previous condition.

### 👣 Steps

1️⃣ **Importing Libraries:** <br>

- **Apache Beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.
- **Pandas:** A powerful data manipulation library for handling structured data.
- **OS & Glob:** Used for file and directory management.

2️⃣ **Load and Prepare Data:** <br>

- The **Linnerud dataset** is loaded and converted into a **Pandas DataFrame** for easier manipulation.

3️⃣ **Loading and Transforming the Dataset** <br>

- Loads the **Linnerud dataset**, which contains exercise-related data with three features:
    - "Chins" (pull-ups)
    - "Situps" (sit-ups)
    - "Jumps" (jumps)
- Converts the **dataset** into a **Pandas DataFrame**.
- Transforms it into a **list of dictionaries** (data_list) to be used with **Apache Beam**.

4️⃣ **Function: extract_values:**

- Takes a **dictionary** (a row of the dataset).
- Returns only the values (without column names).

5️⃣ **Defining the Apache Beam Pipeline**

- **Defines the function run_pipeline(output_csv_path), which runs the Apache Beam pipeline:**
    1. **beam.Create(data_list):** Converts the list of dictionaries into a PCollection (Apache Beam's data structure).
    2. **beam.Filter(lambda row:** row["Chins"] > 10): Filters rows where "Chins" is greater than 10.
    3. **beam.io.WriteToText(output_csv_path, file_name_suffix='.csv', header="Chins,Situps,Jumps"):** Saves the filtered data as a CSV file.

6️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.

7️⃣ **Example Output:**

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
15     250     80
```

- **Output .csv (Chins > 10)**

```
Chins,Situps,Jumps
12,101,101
15,250,80
```

---

## 💻 4. pipeline_filtered_T_F_csv.py 

### 👨‍💻 Explanation of the Code:

- This **code** will check if the **'Chins'** field meets the condition:
    - If **'Chins'** is **greater than 10**.
    - It will display all fields and add a new field (**Chins>10)** indicating whether the **'Chins'** field meets the previous condition:
        - **'True'** if it does.
        - **'False'** if it does not.

### 👣 Steps

1️⃣ **Importing Libraries:** <br>

- **Apache Beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.
- **Pandas:** A powerful data manipulation library for handling structured data.

2️⃣ **Load and Prepare Data:** <br>

- The **Linnerud dataset** is loaded and converted into a **Pandas DataFrame** for easier manipulation.

3️⃣ **Loading and Transforming the Dataset** <br>

- Loads the **Linnerud dataset**, which contains exercise-related data with three features:
    - "Chins" (pull-ups)
    - "Situps" (sit-ups)
    - "Jumps" (jumps)
- Converts the **dataset** into a **Pandas DataFrame**.
- Transforms it into a **list of dictionaries** (data_list) to be used with **Apache Beam**.

4️⃣ **Function: extract_values:**

- Takes a **dictionary** (a row of the dataset).
- Returns only the values (without column names).

5️⃣ **Function: add_new_field:**

- **True** if 'Chins' > 10.
- **False** otherwise.


6️⃣ **Defining the Apache Beam Pipeline:**

- Defines an Apache Beam pipeline.
- Creates a PCollection from data_list.
- Adds a new field (Chins(>10)) to indicate if "Chins" > 10.
- Extracts only values (removing field names).
- Prints the results for debugging.
- Writes output to a CSV file.

7️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.


8️⃣ **Example Output:**

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
15     250     80
```

- **Output .csv (Chins>10)**

```
Chins,Situps,Jumps,Chins(>10)
5,162,60,False
2,110,60,False
12,101,101,True
15,250,80,True
```

---

## 💻 5. pipeline_group.py

### 👨‍💻 Explanation of the Code:

- This code will help us group the **'Chins'** field into **4 ranges**:

    - 0-5
    - 5-10
    - 10-15
    - 15-20

### 👣 Steps

1️⃣ **Importing Libraries:** <br>

- **Apache Beam:** Used for building and running data processing pipelines.
- **load_linnerud:** A dataset from scikit-learn containing physiological and exercise data.
- **Pandas:** A powerful data manipulation library for handling structured data.

2️⃣ **Load and Prepare Data:** <br>

- The **Linnerud dataset** is loaded and converted into a **Pandas DataFrame** for easier manipulation.

3️⃣ **Categorize Data:** <br>

- Defines bins and labels to categorize the **'Chins'** data into specified ranges.
- **df['Chins Range']:** Creates a new column in the DataFrame that assigns each **'Chins'** value to its corresponding range.

4️⃣ **Extract 'Chins Range' Data:** <br>

- Extracts the **'Chins Range'** column as a **pandas** Series.

5️⃣ **Defining the Apache Beam Pipeline:** <br>

- Initializes a new Apache Beam pipeline.
- Converts the data_list into a PCollection, which is Beam's distributed data structure.
- Counts the occurrences of each unique element in the PCollection.
- Formats the output as a CSV string.
- Prints each element of the PCollection to the console.
- Writes the results to a text file at the specified output_path.

6️⃣ **Execute the Pipeline:** <br>

- The **run_pipeline** function is called within the ***if __name__ == '__main__':*** block to ensure the pipeline runs when the script is executed directly.

7️⃣ **Example Output:**

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
15     250     80
8      150     70
6      200     84
```

- **Output .csv**

```
Chins_Range,Count
0-5,2
5-10,2
10-15,1
15-20,1
```

---
