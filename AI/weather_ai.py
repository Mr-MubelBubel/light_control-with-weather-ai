import numpy as np
import pandas as pd
import warnings

import matplotlib.pyplot as plt
import missingno as mso
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

data = pd.read_csv("../input/seattle-weather.csv")

warnings.filterwarnings('ignore', category=FutureWarning)

plt.figure(figsize=(12, 6))
axz = plt.subplot(1, 2, 2)
mso.bar(data.drop(["date"], axis=1), ax=axz, fontsize=12)

df = data.drop(["date"], axis=1)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

df.precipitation = np.sqrt(df.precipitation)
df.wind = np.sqrt(df.wind)

lc = LabelEncoder()
df["weather"] = lc.fit_transform(df["weather"])

x = ((df.loc[:, df.columns != "weather"]).astype(int)).values[:, 0:]
y = df["weather"].values

df.weather.unique()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=2)

warnings.filterwarnings('ignore')
xgb = XGBClassifier()
xgb.fit(x_train, y_train)
print("XGB Accuracy:{:.2f}%".format(xgb.score(x_test, y_test) * 100))

