import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("dataset.csv")

def label(x):
    if x >= 75:
        return "Safe"
    elif x >= 60:
        return "Warning"
    else:
        return "Critical"

data["risk"] = data["attendance"].apply(label)

X = data[["attendance"]]
y = data["risk"]

model = DecisionTreeClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained")