import pandas as pd


from sklearn.datasets import load_iris
iris_raw = load_iris(as_frame=True)
iris_df = iris_raw.frame
iris_df["species"] = iris_df["target"].map(dict(enumerate(iris_raw.target_names)))
iris_df = iris_df.drop(columns=["target"])
iris_df.to_csv("iris.csv", index=False)

print("Q4: First 5 rows of iris.csv")
iris = pd.read_csv("iris.csv")
print(iris.head())

#Q5
import pandas as pd

iris = pd.read_csv("iris.csv")


iris_modified = iris.drop(index=4)
iris_modified = iris_modified.drop(iris_modified.columns[3], axis=1)

print("Q5: Iris data after deleting row 4 and column index 3")
print(iris_modified.head())