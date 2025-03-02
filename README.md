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

2️⃣ _Install Apache Beam with Google Cloud Support (Optional)_: 
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

2️⃣ Verify Installation:

```
import pandas as pd

print(pd.__version__)
```

### Install scikit-learn and call a Dataset

1️⃣ Install Using pip:

```
pip install scikit-learn
```

2️⃣ Verify Installation:

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

### ✅ Example Output:

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

### ✅ Example Output:

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

### ✅ Example Output:

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

### ✅ Example Output:

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

### ✅ Example Output:

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

## 💻 6. pipeline_group_plot.py

### 👨‍💻 Explanation of the Code:

- This code will categorize the 'Chins' data into four ranges:

    - 0-5
    - 5-10
    - 10-15
    - 15-20

- It will also display the results as a bar chart.

### ✅ Example Output:

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
0-5,2
5-10,2
10-15,1
15-20,1
```

- **Chart**

![Results](./images/pic4.png)

---

## 💻 7. pipeline_group_2.py

### 👨‍💻 Explanation of the Code:

- This code will perform two tasks, adding two new fields to the data:

    1. Categorize the 'Chins' field into four ranges.

        - 0-5
        - 5-10
        - 10-15
        - 15-20

    2. Recategorize the 'Chins' field to determine if it is above or below the average."

### ✅ Example Output:

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
12     105     37
```

- **Output .csv (Chins>10)**

```
Chins,Situps,Jumps,Chins_Range,Chins_vs_Avg
5.0,162.0,60.0,5-10,Below Average
2.0,110.0,60.0,0-5,Below Average
12.0,101.0,101.0,10-15,Above Average
12.0,105.0,37.0,10-15,Above Average
```

---