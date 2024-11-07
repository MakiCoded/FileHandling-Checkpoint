**Loan Prediction Analysis and Calculator 2.0**
**Project Overview**
**This repository contains two different projects:**

**Loan Prediction Analysis **- An analysis script in Jupyter Notebook for calculating statistical values from a loan dataset.
**Calculator 2.0** - A command-line calculator application implemented in Python, supporting basic and advanced operations.
**Project 1: Loan Prediction Analysis**
Overview
This Jupyter Notebook performs a basic statistical analysis on loan amount data from a CSV file, Loan_prediction_dataset.csv. The analysis includes calculating the minimum, mean, median, and standard deviation of loan amounts.

Requirements
Python 3.x
Jupyter Notebook
pandas and numpy libraries
Setup
Install the required libraries:
python
Copy code
!pip install pandas numpy
Open loan_prediction_analysis.ipynb in Jupyter Notebook.
Usage
Load the dataset by reading the Loan_prediction_dataset.csv file.
Extract and calculate statistics on the LoanAmount column.
Use the provided functions to get:
Minimum Loan Amount
Mean Loan Amount
Median Loan Amount
Standard Deviation of Loan Amount
Example calculations:

**python**
Copy code
all_loan_amount = []
for rows in loan_dataset[1:]:
    row_loan_amount = rows.split(",")[8]
    if row_loan_amount == "":
        continue
    all_loan_amount.append(int(row_loan_amount))

loan_array = np.array(all_loan_amount)
print(np.min(loan_array))
print(np.mean(loan_array))
print(np.median(loan_array))
print(np.std(loan_array))
Project 2: Calculator 2.0
Overview
Calculator 2.0 is a command-line calculator written in Python. It supports basic operations (+, -, *, /) as well as advanced operations, such as exponentiation, square root, and logarithm.

**Requirements**
Python 3.x
math module (standard Python library)
Setup
Save the calculator script as calculator_2.0.py.
Run the script using:
bash
Copy code
python calculator_2.0.py
Usage
Run the script and enter numbers and operation symbols as prompted.

Available operations:

+ : Addition
- : Subtraction
* : Multiplication
/ : Division
^ : Exponentiation
sqrt : Square Root
log : Logarithm (base 10)
Example interaction:

**mathematica**
Copy code
Enter the First Number: 10
Enter Operational Symbol (+, -, *, /, ^, sqrt, log): sqrt
The result is 3.1623
Code Structure

**Calculator Class:**
__init__: Initializes the basic operations in a dictionary.
add_operations: Adds advanced operations.
calculate: Handles calculations based on input symbols.
Advanced Operations:
exponentiation: Performs exponentiation (a^b).
square_root: Calculates the square root of a.
logarithm: Calculates the logarithm of a.
