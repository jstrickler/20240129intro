import pandas as pd

#   module.function()
df = pd.read_csv('DATA/titanic.csv')

print(df.head())
print()
print(df.info())