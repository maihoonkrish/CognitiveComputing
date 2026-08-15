import pandas as pd


emp_data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

emp = pd.DataFrame(emp_data)
emp.to_csv("employees.csv", index=False)
emp = pd.read_csv("employees.csv")

# a) Shape
print("a) Shape (rows, columns):", emp.shape)

# b) Summary-dtypes+non-null counts
print("\nb) Summary info:")
emp.info()

# c) Descriptive statistics
print("\nc) Descriptive statistics:")
print(emp.describe())

# d) First 5 rows and last 3 rows
print("\nd) First 5 rows:")
print(emp.head())
print("\nLast 3 rows:")
print(emp.tail(3))

# e) Specific stats
print("\ne.i) Average salary:", emp["Salary"].mean())
print("e.ii) Total bonus paid:", emp["Bonus"].sum())
print("e.iii) Youngest employee's age:", emp["Age"].min())
print("e.iv) Highest performance rating:", emp["Rating"].max())

# f) Sort by Salary descending
print("\nf) Sorted by Salary (descending):")
print(emp.sort_values(by="Salary", ascending=False))

# g) Categorize by performance rating
def categorize(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

emp["Performance_Category"] = emp["Rating"].apply(categorize)
print("\ng) With Performance_Category column:")
print(emp[["Name", "Rating", "Performance_Category"]])

# h) Missing values
print("\nh) Missing values per column:")
print(emp.isnull().sum())

# i) Rename Employee_ID to ID
emp = emp.rename(columns={"Employee_ID": "ID"})
print("\ni) Columns after rename:", list(emp.columns))

# j) Filtering
print("\nj.i) More than 5 years experience:")
print(emp[emp["Years_of_Experience"] > 5])

print("\nj.ii) IT department:")
print(emp[emp["Department"] == "IT"])

# k) Add Tax column (10% of salary)
emp["Tax"] = emp["Salary"] * 0.10
print("\nk) With Tax column:")
print(emp[["Name", "Salary", "Tax"]])

# l) Save modified DataFrame to a new CSV
emp.to_csv("employees_modified.csv", index=False)
print("\nl) Saved to employees_modified.csv")