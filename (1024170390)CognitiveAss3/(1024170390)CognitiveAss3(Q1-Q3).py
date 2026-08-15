import pandas as pd
data = {
"Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital_Status": ["Single", "Married", "Single", "Married", "Divorced",
                        "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable_Income": [125, 100, 70, 120, 95, 60, 220, 85, 75, 90],  # in K
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
 }
#Q1
print("Q1")
df = pd.DataFrame(data)
print("Full data frame is as follows:")
print(df)
print()
#Q2
print("Q2")
print(df.loc[[0,4,7,8]])
print()

print("Q3")
#Q3.1
print("Q3.1")
print(df.loc[3:7])
print()
#Q3.2
print("Q3.2")
print(df.iloc[4:9, 2:5])
print()
#Q3.3
print("Q3.3")
print(df.iloc[:, 1:4])
print()