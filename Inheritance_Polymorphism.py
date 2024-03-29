from Basic_OOP import MarketingDataETL

class TargetedMarketingETL(MarketingDataETL):
    def __init__(self):
        super().__init__()

    def transform(self):
        super().transform()  # Memanggil metode transform() dari kelas induk
        self.segment_customers()

    def segment_customers(self):
        if self.data is not None:
            # Contoh logika segmentasi sederhana: mengelompokkan pelanggan berdasarkan total pengeluaran dalam kategori produk tertentu
            hasil_segmentasi = self.data.groupby('product_category')['amount_spent'].sum()
            print("Segmentasi pelanggan berdasarkan total pengeluaran per kategori produk:")
            print(hasil_segmentasi)
        else:
            print("Tidak ada data untuk disegmentasikan. Mohon ekstrak dan ubah data terlebih dahulu.")

# Contoh penggunaan:
etl = TargetedMarketingETL()
etl.extract("https://raw.githubusercontent.com/MrFarday/data/main/marketing_data.csv")
etl.transform()
etl.store("segmented_marketing_data.csv")
