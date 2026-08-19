# README.md

# 📊 Data Analyzer and Transformer Program

## 👨‍💻 Author

**Shrey Shah**

---

## 📌 Project Description

The **Data Analyzer and Transformer Program** is a Python-based, menu-driven program that allows users to enter, analyze, filter, sort, and calculate statistics from **1D and 2D datasets**.

The program demonstrates important Python programming concepts such as:

* Functions
* Docstrings
* `match-case`
* `while` loops
* Lists
* Built-in functions
* Recursion
* Lambda functions
* `filter()`
* `map()`
* `sort()` and `sorted()`
* `**kwargs`
* Flattening 2D lists

---

## 🎯 Objectives

The main objectives of this project are:

1. To create a simple menu-driven Python program.
2. To analyze 1D and 2D datasets.
3. To calculate basic statistical values.
4. To demonstrate recursion using factorial.
5. To filter data using lambda functions.
6. To sort 1D and 2D datasets.
7. To use sample datasets for testing.
8. To demonstrate the use of `**kwargs`.
9. To use a `while` loop so that the menu continues until the user selects Exit.
10. To understand how Python built-in functions can be used for data analysis.

---

# 🛠️ Requirements

### Software Required

* Python **3.10 or newer**

The program uses the `match-case` statement, which was introduced in Python 3.10.

### External Libraries

No external libraries are required.

The project uses only standard Python features.

---

# 📋 Menu Options

The program provides the following menu:

```text
1. Data Analyzer input
2. Display basic statistics
3. Calculate factorial (Recursion)
4. Filter data through threshold function (Lambda function)
5. Sort data
6. Displaying dataset statistics
7. Exit
```

---

# 1️⃣ Data Analyzer Input

This option allows the user to either manually enter data or use predefined sample data.

## Manual Data

The user can select:

```text
A. 1D array
B. 2D array
```

### Example 1D Data

```text
1 2 3 4 5
```

The program stores it as:

```python
[1, 2, 3, 4, 5]
```

### Example 2D Data

```text
1 2 3
4 5 6
```

The program stores it as:

```python
[[1, 2, 3], [4, 5, 6]]
```

---

# 2️⃣ Sample Data

The program contains predefined sample datasets.

### Sample 1D Array

```python
arr2 = [1, 2, 3, 4, 5, 6]
```

### Sample 2D Array

```python
arr3 = [[1, 2, 3], [4, 5, 6]]
```

These datasets can be used to test the different functions without manually entering data.

---

# 3️⃣ Display Basic Statistics

This option calculates basic statistics using Python's built-in functions.

The program calculates:

* Length
* Sum
* Minimum value
* Maximum value
* Range
* Average

For example:

```text
Dataset: [1, 2, 3, 4, 5, 6]

Length is: 6
Sum is: 21
Minimum value is: 1
Maximum value is: 6
Range is: 5
Average is: 3.5
```

The following built-in functions are used:

```python
len()
sum()
min()
max()
```

---

# 4️⃣ Factorial Using Recursion

The program calculates the factorial of a number using **recursion**.

Example:

```text
Enter your number for factorial: 5

Factorial is: 120
```

The recursive calculation works like:

```text
5 × 4 × 3 × 2 × 1 = 120
```

The function uses:

```python
return n * factorial(n - 1)
```

The program also checks for negative numbers because factorial is not calculated for negative numbers in this project.

---

# 5️⃣ Filtering Using Lambda

This option filters values according to a threshold value.

The program uses:

```python
filter()
```

together with:

```python
lambda
```

### Example

Dataset:

```python
[1, 2, 3, 4, 5, 6]
```

Threshold:

```text
3
```

Output:

```python
[4, 5, 6]
```

The filtering condition is:

```python
lambda x: x > threshold
```

The program supports:

```text
oned
twod
sample1
sample2
```

---

# 6️⃣ Sorting

The sorting function allows the user to sort data in:

```text
1. Ascending order
2. Descending order
```

It supports:

```text
1 = Manual 1D
2 = Manual 2D
3 = Sample 1D
4 = Sample 2D
```

### Example

Original data:

```python
[5, 2, 8, 1, 4]
```

Ascending order:

```python
[1, 2, 4, 5, 8]
```

Descending order:

```python
[8, 5, 4, 2, 1]
```

The program demonstrates both:

```python
sort()
```

and:

```python
sorted()
```

For 2D data, `map()` and `lambda` are also used to sort individual rows.

---

# 7️⃣ Dataset Characteristics

This function displays the characteristics of the selected dataset.

The characteristics include:

```text
Length
Sum
Minimum value
Maximum value
Range
Average
```

For example:

```text
Dataset: [1, 2, 3, 4, 5, 6]

Length is: 6
Sum is: 21
Minimum value is: 1
Maximum value is: 6
Range is: 5
Average is: 3.5
```

The function uses `print()` to display the results instead of returning them.

---

# 📚 Flattening a 2D Array

A 2D array contains multiple rows.

For example:

```python
arr3 = [[1, 2, 3], [4, 5, 6]]
```

To calculate statistics easily, the program flattens it into:

```python
[1, 2, 3, 4, 5, 6]
```

This is called **flattening**.

The program uses:

```python
flat = sum(arr3, [])
```

After flattening:

```python
flat = [1, 2, 3, 4, 5, 6]
```

Now functions such as:

```python
sum(flat)
min(flat)
max(flat)
```

can be used easily.

---

# 🔑 Use of `**kwargs`

The `displaydatabasicstatics()` function demonstrates the use of `**kwargs`.

The function is defined as:

```python
def displaydatabasicstatics(**kwargs):
```

It allows additional named information to be passed to the function.

Example:

```python
displaydatabasicstatics(
    name="My Dataset",
    type="Current Dataset"
)
```

Inside the function, the values can be accessed using:

```python
kwargs["name"]
```

and:

```python
kwargs["type"]
```

This demonstrates how `**kwargs` can be used to pass multiple named arguments to a function.

---

# 🔄 While Loop

The main menu uses a `while` loop:

```python
while num != 7:
```

This means that the program continues running until the user enters:

```text
7
```

The basic structure is:

```python
num = int(input("Enter your choice: "))

while num != 7:

    match num:
        ...

    num = int(input("Enter your choice: "))
```

This allows the user to perform multiple operations without restarting the program.

---

# 🧠 Python Concepts Demonstrated

| Python Concept | Usage in Project                          |
| -------------- | ----------------------------------------- |
| Variables      | Storing data and user choices             |
| Lists          | Storing datasets                          |
| 1D Lists       | `oned`, `arr2`                            |
| 2D Lists       | `twod`, `arr3`                            |
| Functions      | Dividing the program into different tasks |
| Docstrings     | Describing every function                 |
| `while` loop   | Repeating the main menu                   |
| `match-case`   | Selecting menu options                    |
| `if-elif-else` | Making decisions                          |
| `len()`        | Finding dataset length                    |
| `sum()`        | Finding dataset sum                       |
| `min()`        | Finding minimum value                     |
| `max()`        | Finding maximum value                     |
| `sort()`       | Sorting lists                             |
| `sorted()`     | Creating sorted lists                     |
| `map()`        | Processing rows of 2D data                |
| `filter()`     | Filtering values                          |
| `lambda`       | Creating small functions                  |
| Recursion      | Calculating factorial                     |
| `**kwargs`     | Passing named information                 |
| Flattening     | Processing 2D data                        |

---

# ▶️ How to Run the Program

### Step 1: Install Python

Install Python 3.10 or a newer version.

### Step 2: Save the Python File

Save the program as:

```text
data_analyzer.py
```

### Step 3: Open Command Prompt

Open Command Prompt or Terminal in the project folder.

### Step 4: Run the Program

Use:

```bash
python data_analyzer.py
```

The program will display the menu.

---

# 🧪 Sample Data

The program contains the following sample data.

### Sample 1D

```python
[1, 2, 3, 4, 5, 6]
```

Statistics:

```text
Length = 6
Sum = 21
Minimum = 1
Maximum = 6
Range = 5
Average = 3.5
```

### Sample 2D

```python
[[1, 2, 3], [4, 5, 6]]
```

After flattening:

```python
[1, 2, 3, 4, 5, 6]
```

Statistics:

```text
Length = 2 rows
Sum = 21
Minimum = 1
Maximum = 6
Range = 5
Average = 3.5
```

---

# 📁 Project Structure

A simple project structure can be:

```text
Data-Analyzer/
│
├── data_analyzer.py
│
└── README.md
```

### `data_analyzer.py`

Contains the complete Python program.

### `README.md`

Contains information about the project, its objectives, features, requirements, and usage.

---

# ⭐ Main Features

The program provides:

* ✅ Manual 1D data input
* ✅ Manual 2D data input
* ✅ Sample 1D data
* ✅ Sample 2D data
* ✅ Basic statistics
* ✅ Factorial using recursion
* ✅ Data filtering
* ✅ Lambda functions
* ✅ Sorting
* ✅ 2D data flattening
* ✅ `map()` function
* ✅ `filter()` function
* ✅ `**kwargs`
* ✅ Docstrings
* ✅ Repeating menu using `while` loop
* ✅ Exit option

---

# 📌 Conclusion

The **Data Analyzer and Transformer Program** is a beginner/student-level Python project designed to demonstrate fundamental Python programming concepts through a practical data analysis application.

The project combines data input, statistical calculations, filtering, sorting, recursion, lambda functions, `**kwargs`, and loops into one menu-driven program.

It provides a simple way to understand how different Python concepts can work together to create a useful application.

---

## 👨‍💻 Author

**Shrey Shah**

### Project Name

**Data Analyzer and Transformer Program**

### Programming Language

**Python**
