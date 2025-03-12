# 🚀 Pipelines (First Approach)

## ➰ What's a pipeline?

✅ Sequence of **data** processing **steps**, where the **output** of one step becomes the **input** for the **next**. <br>
✅ Commonly used in **data engineering**, **machine learning**, and **software development** to automate **workflows** and ensure efficient **processing**.

![Pipeline](./src/images/pic1.png)

## 🅱️ What's Apache-Beam?

✅ **Apache Beam** is a framework for **batch** and **streaming data processing**. <br>
✅ It provides a **unified API** that can run on multiple execution engines. <br>
✅ Works well with **Google Cloud Dataflow**, **Apache Flink**, and **Apache Spark**. <br>
✅ Supports **Python**, **Java**, and **Go** for pipeline development.

![Apache](./src/images/pic2.png)

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

![Dataframe](./src/images/pic3.png)

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

# 🛠 Code Explanation - 'pipeline' folder

## 💻 1. pipeline.py

### 👨‍💻 Explanation of the Code:

- This **code** will check if the **'Chins'** field meets the condition:
    - If **'Chins'** is **greater than 10** (Chins > 10)
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

    | Chins |
    |-------|
    |  0-5  |
    |  5-10 |
    | 10-15 |
    | 15-20 |
    | 20-25 |
    | 25-30 |

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

![Results](./src/images/pic4.png)

---

## 💻 7. pipeline_group_2.py

### 👨‍💻 Explanation of the Code:

- This code will perform two tasks, adding two new fields to the data:

    1. Categorize the 'Chins' field into four ranges.

        | Chins |
        |-------|
        |  0-5  |
        |  5-10 |
        | 10-15 |
        | 15-20 |
        | 20-25 |
        | 25-30 |

    2. Recategorize the 'Chins' field to determine if it is above or below the average.

### ✅ Example Output:

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
12     105     37
```

- **Output .csv**

```
Chins,Situps,Jumps,Chins_Range,Chins_vs_Avg
5.0,162.0,60.0,5-10,Below Average
2.0,110.0,60.0,0-5,Below Average
12.0,101.0,101.0,10-15,Above Average
12.0,105.0,37.0,10-15,Above Average
```

---

## 💻 8. pipeline_all_fields.py

### 👨‍💻 Explanation of the Code:

- This code will perform two tasks, adding two new fields to the data:

    1. Categorize the 'Chins', 'Situps' and 'Jumps' fields into four ranges.

    | Chins     | Situps      | Jumps |
    |-----------|-------------|-------|
    |  0-5  (0) |  0-50  (0)  |  0-25 |
    |  5-10 (5) | 50-100 (50) | 25-50 |
    | 10-15 (10)|100-150 (100)| 50-75 |
    | 15-20 (15)|150-200 (150)|75-100 |
    | 20-25 (20)|200-250 (200)|100-125|
    | 25-30 (25)|250-300 (250)|125-150|

    2. Recategorize the 'Chins', 'Situps' and 'Jumps' field to determine if it is above or below the average.

### ✅ Example Output:

- **Original Dataset**

```
Chins  Situps  Jumps
5      162     60
2      110     60
12     101     101
12     105     37
```

- **Output .csv**

```
Chins,Situps,Jumps,Chins Range,Situps Range,Jumps Range,User,Chins_vs_Avg,Situps_vs_Avg,Jumps_vs_Avg
5.0,162.0,60.0,5,150,50,User 1,1,0,1
2.0,110.0,60.0,0,100,50,User 2,1,1,1
12.0,101.0,101.0,10,100,100,User 3,0,1,0
12.0,105.0,37.0,10,100,25,User 4,0,1,1
13.0,155.0,58.0,10,150,50,User 5,0,0,1
```

---

# 🛠 Code Explanation - 'machine_learning' folder

## 💻 1. eda.py

### 👨‍💻 Explanation of the Code:

- This code will allow us to analyze the available information to determine what type of analysis we can perform afterward.

- Three analyses (so far) will be conducted:

    1. Dataset report.
    2. Histograms.
    3. Density analysis.

- Finally, the reports will be downloaded as a PDF file.

### ✅ Example Output:

- I will not display the outputs, as they are saved as images and can be accessed from the **'downloads'** folder.

## 💻 2. advanced_statistical_analysis.py

### 👨‍💻 Explanation of the Code:

- In this code, we will perform two analyses using three variables: 'Chins', 'Jumps', and 'Situps':

1. Hypothesis testing
2. Clustering

- More may be added in the future. For now, this analysis is conducted to test how it works.

### ✅ Example Output:

#### hypothesis_testing:

```
Mean Situps: 135.0
Mean Jumps: 53.75
T-statistic: 42.5296
P-value: 0.0000
We reject the null hypothesis: the means are significantly different.
```

```
Mean Jumps: 53.75
Mean Chins: 7.5
T-statistic: 16.8558
P-value: 0.0000
We reject the null hypothesis: the means are significantly different.
```

```
Mean Chins: 7.5
Mean Situps: 135.0
T-statistic: -57.3606
P-value: 0.0000
We reject the null hypothesis: the means are significantly different.
```

#### clustering:

```
Iteration 0 - Silhouette Score: 0.55

Iteration 1 - Silhouette Score: 0.49

Iteration 2 - Silhouette Score: 0.53
```

---

## 💻 3. mae_mse.py

### 👨‍💻 Explanation of the Code:

- This code will determinate the values of **MSE** and **MAE**.

### ✅ Example Output:

#### mse_mae

```
MSE for Situps Range and Jumps Range: 189.8777
MAE for Situps Range and Jumps Range: 10.6886
```

```
MSE for Jumps Range and Chins Range: 17.6324
MAE for Jumps Range and Chins Range: 3.0729
```

```
MSE for Chins Range and Situps Range: 2265.5290
MAE for Chins Range and Situps Range: 46.8652
```

---

## 💻 4. linear_regression.py

### 👨‍💻 Explanation of the Code:

- This code will determine the values of MSE, and with that, we can create the linear regression model.

### ✅ Example Output:

#### linear_regression

```
Regression between 'Situps Range' (X) and 'Jumps Range' (y):
Coef: [0.35509138]
Intercept: [4.50391645]
R2: 0.5581028260779296
MSE: 189.87769191963963
```

```
Regression between 'Jumps Range' (X) and 'Chins Range' (y):
Coef: [0.06666667]
Intercept: [4.47916667]
R2: -0.02588383838383823
MSE: 17.63237847222222
```

```
Regression between 'Chins Range' (X) and 'Situps Range' (y):
Coef: [7.99373041]
Intercept: [65.67398119]
R2: -0.3181259832530947
MSE: 2265.5290337162564
```

---

## 💻 5. decision_tree.py

### 👨‍💻 Explanation of the Code:

- The code builds decision trees by using each column in **selected_columns** as a feature and the **next column** as a label, training the model on 70% of the data and testing on 30%. 
- It evaluates accuracy and visualizes the tree for each pair. 
- The process repeats in a circular manner for all selected columns.

### ✅ Example Output:

#### decision_tree

```
Decision tree between 'Situps Range' (X) and 'Jumps Range' (y)
X_train shape: (14, 1)
y_train shape: (14,)
Unique classes in y_train: [ 25  50 100 125]
Accuracy: 0.50
```

```
Decision tree between 'Jumps Range' (X) and 'Chins Range' (y)
X_train shape: (14, 1)
y_train shape: (14,)
Unique classes in y_train: [ 0  5 10 15]
Accuracy: 0.33
```

```
Decision tree between 'Chins Range' (X) and 'Situps Range' (y)
X_train shape: (14, 1)
y_train shape: (14,)
Unique classes in y_train: [ 50 100 150 200 250]
Accuracy: 0.00
```

---