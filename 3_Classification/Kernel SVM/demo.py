import pandas as pd

dataset = pd.read_csv('Social_Network_Ads.csv')


row1 = dataset.iloc[:,:-1].values

print(row1)
