import pandas as pd

df = pd.read_csv('hotwil_tokped.csv')
# Menghapus baris yang memiliki nilai NaN
df_cleaned = df.dropna()

# Pilih kolom yang diinginkan, misalnya 'key1', 'key2', 'key3'
selected_df = df_cleaned[['Nama Toko', 'Lokasi', 'Nama Produk', 'Harga Produk', 'Terjual', 'Rating']]

# Mengubah DataFrame menjadi JSON
json_data = selected_df.to_json(orient='records')
print(json_data)