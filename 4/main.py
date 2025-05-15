import pandas as pd
import numpy as np

df = pd.read_csv("./fitness_tracker_dataset_dirty.csv", encoding="utf-8")

df.drop_duplicates(inplace=True)

df.info()

df[df[["heart_rate", "calories_burned"]].isna().astype(int).sum(axis=1) > 0]

df.dropna(inplace=True)

users_med = df.groupby("user_id")["heart_rate"].transform("median")
users_med

df["user_id"].unique()

x = df["heart_rate"]
cond = (df["heart_rate"] >= 40) & (df["heart_rate"] <= 200)
df["heart_rate"] = x.where(cond, users_med)

filt = df["heart_rate"] != x
x[filt]
df[filt]

df["timestamp"] = pd.to_datetime(df["timestamp"])

df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour

df.sort_values(by=["timestamp"])
df["steps_this_hour"] = df.groupby(["user_id", "date"])["cumulative_steps"].diff().fillna(0)

df["steps_this_hour"] = df["steps_this_hour"].apply(lambda x: max(x, 0))

def fun(x):
    if (x < 100):
        return "low"
    if (x < 1000):
        return "medium"
    return "high"

df["activity_intensity"] = df["steps_this_hour"].apply(fun)

df["heart_rate"] = df["heart_rate"].round(2)
df["calories_burned"] = df["calories_burned"].round(2)

out = [
    "user_id",
    "timestamp",
    "cumulative_steps",
    "heart_rate",
    "calories_burned",
    "activity_type",
    "date",
    "hour",
    "steps_this_hour",
    "activity_intensity"
]

df[out].sort_values(by=["user_id", "timestamp"]).to_csv("res.csv", sep=",", index=False)
