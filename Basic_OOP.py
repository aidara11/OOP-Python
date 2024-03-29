"""
Task1 (Basic OOP): Buatlah class MarketingDataETL yang memiliki tiga metode:

1. extract(): akan membaca data dari sebuah file CSV (Misalkan, marketing_data.csv)

2. transform(): akan melakukan pembersihan dan transformasi sederhana pada data (seperti mengubah format tanggal atau membersihkan nilai yang kosong)

3. store(): akan menyimpan data yang telah ditransformasi ke dalam struktur data DataFramet.
"""

import pandas as pd

class MarketingDataETL:
    def __init__(self):
        self.data = None

    def extract(self, filename):
        try:
            self.data = pd.read_csv(filename, sep=';')  # Menentukan delimiter sebagai titik koma
            print("Data berhasil diekstrak.")
        except FileNotFoundError:
            print("File tidak ditemukan. Mohon berikan nama file yang valid.")
        except Exception as e:
            print(f"Terjadi kesalahan saat ekstraksi: {e}")

    def transform(self):
        if self.data is not None:
            # Ubah format tanggal dari '03/01/23' menjadi '03-01-2023'
            self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date'], format='%d/%m/%y')
            # Menghapus baris yang memiliki nilai kosong
            self.data = self.data.dropna()
            print("Data berhasil diubah.")
        else:
            print("Tidak ada data untuk diubah. Mohon ekstrak data terlebih dahulu.")

    def store(self, output_filename):
        if self.data is not None:
            try:
                self.data.to_csv(output_filename, index=False)  # Tidak perlu menentukan delimiter karena titik koma (;) adalah nilai default
                print(f"Data yang telah diubah berhasil disimpan ke {output_filename}.")
            except Exception as e:
                print(f"Gagal menyimpan data: {e}. Mohon periksa nama file output Anda.")
        else:
            print("Tidak ada data untuk disimpan. Mohon ekstrak dan ubah data terlebih dahulu.")

# Contoh penggunaan:
etl = MarketingDataETL()
etl.extract("https://raw.githubusercontent.com/MrFarday/data/main/marketing_data.csv")
etl.transform()
etl.store("transformed_marketing_data.csv")

# Membaca file CSV yang telah disimpan
transformed_data = pd.read_csv("transformed_marketing_data.csv")

# Menampilkan beberapa baris pertama dari data yang telah diubah
print("Beberapa baris pertama data yang telah diubah:")
print(transformed_data.head())