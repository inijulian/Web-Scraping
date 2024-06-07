import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('hotwil_tokped.csv')

# Mengubah warna bar
store_counts = df['Lokasi'].value_counts().head(15)

# Membuat array warna
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple', 'red', 'blue', 'orange', 'grey', 'pink']

# Membuat array explode untuk mengeksplod potongan pertama
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0)

# Membuat grafik lingkaran
plt.figure(figsize=(10, 8))
plt.pie(store_counts, explode=explode, labels=store_counts.index, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribusi Lokasi Toko', fontsize=14, fontweight='bold')
plt.axis('equal')  # Untuk membuat grafik lingkaran yang sempurna

plt.show()
