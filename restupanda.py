import pandas as pd
import matplotlib.pyplot as plt

# Membaca file excel (pastikan file di directory yang sama atau sesuaikan path-nya)
data = pd.read_excel('Dataset_Studi_Kasus.xlsx')  # Sesuaikan nama file

# Menampilkan beberapa baris pertama data
print("Beberapa baris pertama dari dataset:")
print(data.head())

# Menampilkan informasi umum tentang dataset
print("\nInformasi dataset:")
print(data.info())

# Menghitung statistik deskriptif
print("\nStatistik deskriptif:")
print(data.describe())

# Menghitung total pemasukan selama setahun
total_pemasukan = data['Pemasukan'].sum()
print(f"\nTotal pemasukan selama setahun: {total_pemasukan}")

# Menghitung rata-rata pemasukan per bulan
rata_rata_pemasukan = data['Pemasukan'].mean()
print(f"\nRata-rata pemasukan per bulan: {rata_rata_pemasukan}")

# Menyaring bulan dengan pemasukan di atas rata-rata
pemasukan_diatas_rata = data[data['Pemasukan'] > rata_rata_pemasukan]
print("\nBulan dengan pemasukan di atas rata-rata:")
print(pemasukan_diatas_rata)

# Mengurutkan data berdasarkan pemasukan terbesar
data_sorted = data.sort_values(by='Pemasukan', ascending=False)
print("\nBulan dengan pemasukan terbesar hingga terkecil:")
print(data_sorted)

# Menampilkan data pemasukan terendah dan tertinggi
pemasukan_terendah = data['Pemasukan'].min()
pemasukan_tertinggi = data['Pemasukan'].max()
print(f"\nPemasukan terendah: {pemasukan_terendah}")
print(f"Pemasukan tertinggi: {pemasukan_tertinggi}")

# Pembersihan dan transformasi data
# Misalnya: Mengganti nilai NaN dengan 0 atau membersihkan data duplikat
data_cleaned = data.fillna(0)  # Ganti NaN dengan 0
data_cleaned = data_cleaned.drop_duplicates()  # Menghapus data duplikat
print("\nData setelah pembersihan:")
print(data_cleaned)

# Membuat Pivot Table (Contoh: Sum Pemasukan per Bulan)
pivot_table = data_cleaned.pivot_table(values='Pemasukan', index='Bulan', aggfunc='sum')
print("\nPivot table (Total Pemasukan per Bulan):")
print(pivot_table)

# Ekspor data ke CSV
data_cleaned.to_csv('pemasukan_bulanan_cleaned.csv', index=False)
print("\nData diekspor ke 'pemasukan_bulanan_cleaned.csv'")

# Visualisasi dengan pandas (Contoh: Visualisasi Pemasukan per Bulan)
plt.figure(figsize=(10, 6))
plt.bar(data['Bulan'], data['Pemasukan'], color='skyblue')
plt.xlabel('Bulan')
plt.ylabel('Pemasukan')
plt.title('Pemasukan per Bulan')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pandas TimeSeries (Contoh: Jika kolom 'Bulan' adalah tanggal)
# Misal ada kolom tanggal, kita bisa memanfaatkan pandas timeseries
# data['Tanggal'] = pd.to_datetime(data['Bulan'], format='%Y-%m-%d')
# data.set_index('Tanggal', inplace=True)
# print("\nDataset dengan Pandas TimeSeries:")
# print(data.head())

# Menghitung Mean, Median, Standar Deviasi, Variansi
mean_pemasukan = data['Pemasukan'].mean()
median_pemasukan = data['Pemasukan'].median()
std_pemasukan = data['Pemasukan'].std()
var_pemasukan = data['Pemasukan'].var()

print(f"\nMean Pemasukan: {mean_pemasukan}")
print(f"Median Pemasukan: {median_pemasukan}")
print(f"Standar Deviasi Pemasukan: {std_pemasukan}")
print(f"Variansi Pemasukan: {var_pemasukan}")

# Operasi dasar dataframe: seleksi kolom, filter data, penambahan kolom baru
data_filtered = data[data['Pemasukan'] > 5000000]  # Filter pemasukan di atas 5 juta
data['Pemasukan_Kena_Pajak'] = data['Pemasukan'] * 0.1  # Penambahan kolom baru

print("\nData setelah filter dan penambahan kolom baru:")
print(data_filtered)
print("\nData dengan kolom baru 'Pemasukan_Kena_Pajak':")
print(data.head())

# Mengurutkan data berdasarkan kolom 'Pemasukan' secara ascending
data_sorted_ascending = data.sort_values(by='Pemasukan', ascending=True)
print("\nData diurutkan berdasarkan pemasukan (ascending):")
print(data_sorted_ascending)

# Fungsi slicing pada DataFrame
# Menyaring data dari baris ke-10 hingga ke-20
data_slice = data.iloc[10:21]  # Baris ke-10 sampai ke-20 (inclusive)
print("\nData dari baris ke-10 hingga ke-20:")
print(data_slice)

# Menyaring data berdasarkan kriteria tertentu
# Misalnya, data dari bulan tertentu
bulan_tentukan = 'Januari'
data_bulan_tertentu = data[data['Bulan'] == bulan_tentukan]
print(f"\nData untuk bulan {bulan_tentukan}:")
print(data_bulan_tertentu)

# Menyaring data berdasarkan beberapa bulan
bulan_tentukan = ['Januari', 'Februari']
data_bulan_tertentu_multiple = data[data['Bulan'].isin(bulan_tentukan)]
print(f"\nData untuk bulan {', '.join(bulan_tentukan)}:")
print(data_bulan_tertentu_multiple)
