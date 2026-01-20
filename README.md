### TOPSIS Implementation in Python

**Author:** Saumya Kumari  
**Roll No:** 102303161  

This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method in Python.  
It includes a **published PyPI package**, **command-line execution**, a **Google Colab notebook**, and a **Flask-based web service**.

---

## PyPI Package

The Python package is published on PyPI at:

🔗 https://pypi.org/project/topsis-saumyakumari-102303161/1.0.2/

---

### Installation

Install the package using pip:

```bash
pip install Topsis-saumyakumari-102303161
```


---

### Methodology

* TOPSIS is a multi-criteria decision-making technique that ranks alternatives based on their distance from an ideal solution.
* The steps followed are:
* Read the decision matrix from a CSV file
* Normalize the criteria values
* Apply the given weights to each criterion
* Determine the positive and negative ideal solutions using impacts
* Calculate the Euclidean distance from both ideal solutions
* Compute the TOPSIS score
* Rank alternatives based on the score
* The alternative with the highest TOPSIS score is ranked the best

---

### Project Structure

Topsis_Assignment/
├── topsis_web_service/
│ ├── app.py/
│ └── templates/
│ └── index.html/
└── topsis_assignment1.ipynb   

---

##  Example

### 1. Prepare your Data (`new_data.csv`)

Create a CSV file with your data. The first column should be the name/ID of the alternative, and subsequent columns should be numeric criteria.

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|------|------|-----|------|-------|
| M1        | 0.86 | 0.74 | 6.9 | 30.4 | 9.73  |
| M2        | 0.81 | 0.66 | 3.1 | 52.5 | 14.27 |
| M3        | 0.82 | 0.67 | 3.2 | 64.7 | 17.35 |
| M4        | 0.76 | 0.58 | 4.2 | 34.1 | 9.91  |
| M5        | 0.82 | 0.67 | 6.9 | 61.3 | 17.42 |
| M6        | 0.88 | 0.77 | 5   | 35   | 10.41 |
| M7        | 0.72 | 0.52 | 6.6 | 30.1 | 9.49  |
| M8        | 0.67 | 0.45 | 5.7 | 55.3 | 15.53 |


### 2. Run the Command

Run the following command in your terminal:

```bash
topsis new_data.csv ""1,1,1,1,1" "+,+,-,+,+"" result.csv

```

### 3. Result Table (`result.csv`)

The program will generate a new file `result.csv` with two additional columns: **Topsis Score** and **Rank**.

| Fund Name | P1   | P2   | P3  | P4   | P5    | TOPSIS Score | Rank |
|-----------|------|------|-----|------|-------|--------------|------|
| M1        | 0.94 | 0.88 | 5.5 | 56.8 | 16.03 | 0.697876362  | 2    |
| M2        | 0.9  | 0.81 | 6.6 | 50.7 | 14.75 | 0.525908465  | 5    |
| M3        | 0.67 | 0.45 | 3.7 | 58.8 | 15.91 | 0.551137788  | 4    |
| M4        | 0.72 | 0.52 | 4   | 66.5 | 17.94 | 0.640894741  | 3    |
| M5        | 0.88 | 0.77 | 5.6 | 40.8 | 12.01 | 0.436665578  | 6    |
| M6        | 0.94 | 0.88 | 4.6 | 55.7 | 15.53 | 0.755691432  | 1    |
| M7        | 0.88 | 0.77 | 6.5 | 31.7 | 9.96  | 0.329293654  | 8    |
| M8        | 0.77 | 0.59 | 4.7 | 44.4 | 12.62 | 0.41404122   | 7    |

---

### Web Service

The topsis_web_service folder contains a Flask application that provides TOPSIS as a web service.
Users can:
* Upload a CSV file
* Enter weights and impacts
* Get ranked results directly through the browser


---

### Validation

The program validates:
* Correct number of weights and impacts
* Numeric values in criteria columns
* Valid impact symbols (+ or -)
* Proper CSV file format
* Errors are displayed if invalid input is provided.


---

### Dependencies

* Python 3.x
* pandas
* numpy
* flask

---

### Conclusion

This project provides a complete and structured implementation of the TOPSIS decision-making method.
It supports:
* PyPI package usage
* Command-line execution
* Data visualization through Colab
* Web-based interaction using Flask








