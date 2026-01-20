import pandas as pd
import numpy as np

data = pd.read_csv("googleplaystore.csv")
print(data);
print(data['App']);
print(data.isnull().sum());
df=data.dropna();
print(df.isnull().sum());
avg=sum(df['Rating'])/len(df["Rating"]);
print(float(str(avg)[0:4]))