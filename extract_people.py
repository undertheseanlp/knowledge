from model.person import Person
import json
filepath = "data/nguoinoitieng/raw/nguoinoitieng_20180626.jl"
import pandas as pd

items = []
for line in open(filepath):
    item = json.loads(line.strip())
    items.append(item)
df = pd.DataFrame(items)
print("Job")
print(df["job"].value_counts())
print("location")
print(df["location"].value_counts())
print(0)