import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('hotwil_tokped.csv')

# Menghapus baris yang memiliki nilai NaN
df_cleaning = df.dropna()

print(df_cleaning.head(50))
