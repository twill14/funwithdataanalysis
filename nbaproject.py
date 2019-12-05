import matplotlib as matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path ='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'

df = pd.read_csv(path)

#print(df.head())

#print(df.dtypes)

#print(df.corr())

#df[['bore','stroke' ,'compression-ratio','horsepower']].corr()

sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)

sns.regplot(x="highway-mpg", y="price", data=df)


sns.boxplot(x="body-style", y="price", data=df)

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(10)