# OOP-Python
Tugas Dibimbing.id MSIB Data Warehousing Day 15 - Belajar Git Materi OOP Python 

## Data
Data yang digunakan adalah data marketing di suatu toko yang terdiri dari 8 baris/amatan dan 4 kolom/variabel, yaitu:
1. costumer_id: berisi id costumer
2. purchase_date: tanggal costumer membeli produk
3. product_category: jenis produk yang dibeli oleh costumer
4. amount_spent: jumlah produk yang dibeli costumer

Setelah diperiksa, ternyata data tidak lengkap, terdapat data kosong pada kolom purchase_date.

## Class
Pada github kali ini terdiri dari 2 class di python
1. class MarketingDataETL
2. class TargetedMarketingETL

## Langkah-Langkah Git yang saya lakukan
1. git clone: saya melakukan git clone untuk menghubungkan repository dengan local (folder laptop pribadi)
2. git add: Menambah file baru bernama "Basic_OOP.py" ke dalam rangkaian git
3. git status: Melihat apakah file yang saya tambahkan sudah masuk ke rangkaian git
4. git add: Karena saya membuat class yang berisi mengekstrak, mentransformasi, dan menyimpan data yang telah ditransformasi dengan nama file "transformed_marketing_data.csv" sehingga saya menambahkan file tersebut dengan git add ke dalam rangkaian git
5. git commit: Menggunakan git commit -m "membangun kelas Marketing Data ETL" untuk menyetujui bahwa perubahan script saya sudah fix tapi baru di local laptop saja
6. git status: Ternyata sudah tidak ada lagi yang perlu dicommit (nothing to commit, working tree clean)
7. git push: saya melakukan ini untuk push file saya ke cloud agar dapat menyimpan kode di github
8. git checkout: Menggunakan git checkout -b add_targetmarketing untuk menambah kelas baru, supaya langsung pindah ke branch baru bernama add_targetmarketing (Switched to a new branch 'add_targetmarketing')
9. git status: untuk memeriksa kembali apa saja yang sudah dilakukan
10. git log: untuk melihat perubahan dari file saya
11. git status: sebelum commit code yang sudah ditambahkan, bisa lihat dulu sudah berada dalam brach mana (On branch add_targetmarketing)
12. git add . : untuk menambahkan class TargetedMarketingETL yang sudah dibuat
13. git commit: Menggunakan git commit -m "menambah kelas Targeted Marketing ETL" untuk menyetujui bahwa perubahan script saya sudah fix tapi baru di local laptop saja
14. git checkout main: pindah branch ke main lagi untuk menyelesaikan code
15. git checkout add_targetmarketing: untuk kembali lagi ke branch add_targetmarketing
16. git add: Menambahkan file baru bernama "Inheritance_Polymorphism.py" ke dalam rangkaian git
17. git log: untuk melihat histori commit saya
18. git status: untuk melihat kembali saya berada di brach mana
19. git add:  Karena saya membuat class TargetedMarketingETL yang berisi mentransformasi, segmentasi pelanggan, dan menyimpan data segmentasi pelanggan dengan nama file "segmented_marketing_data.csv" sehingga saya menambahkan file tersebut dengan git add ke dalam rangkaian git
20. git commit: Menggunakan git commit -m "menyimpan data segmentasi pelanggan" untuk menyetujui bahwa perubahan script saya sudah fix tapi baru di local laptop saja
21. git push: menggunakan git push origin add_targetmarketing sehingga di github ada brach baru bernama add_target marketing.


git status 
Untuk melihat status atau apa saja yang telah dilakukan

git commit -m "<descriptive_message>"
Untuk menyetujui bahwa file sudah siap diupload. Setelah dicommit dapat dilihat perbedaannya apa saja, file yang ditambahkan apa saja

git log
melihat perubahan dari file kita

git push
push ke cloud untuk menyimpan kode kita di github

Pull request
Memberi tahu orang lain bahwa kita sudah selesai coding, sudah dipush dan siap di merge pull

git branch
membuat branch baru

git checkout <branch_name>

git revert <commits> untuk mengundo, membuat commit baru dimana commit baru itu menjelaskan bahwa kita akan kembali ke commit sebelumnya. Tidak akan menghapus history commit sebelumnya tetapi dia akan melakukan state bahwa commit sekarang adalah versi yang lama.

git reset
akan menghapus segala perubahan yang ada di commit tersebut



Pertama saya membuat repository baru dengan nama OOP-Python
Lalu saya clone repository agar file dari repository agar bisa masuk ke laptop saya
