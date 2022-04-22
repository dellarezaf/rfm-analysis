# Segmentasi Pelanggan menggunakan RFM score

RFM (Recency, Frequency, Monetary) merupakan metode marketing yang digunakan untuk mengelompokkan perilaku pelanggan berdasarkan 
  1. Recency : seberapa baru transaksi terakhir yang dilakukan ;
  2. Frequency : seberapa sering melakukan transaksi ; dan
  3. Monetary : seberapa banyak uang yang ditransaksikan.

Data yang **harus ada** agar bisa menggunakan metode ini adalah user_id. Hal ini dikarenakan metode RFM melakukan rekapitulasi Recency, Frequnecy dan Monetary per pelanggan sehingga data yang dihasilkan merupakan data aggregate per pelanggan. Setelah itu barulah dilakukan scoring untuk mengelompokkan masing-masing pelanggan ke dalam berbagai segment. Untuk deskripsi masing-masing segment dapat dilihat lebih detail [disini](https://runawayhorse001.github.io/LearningApacheSpark/rfm.html#load-and-clean-data).

Pada saat menjalankan file rfm.py perlu melakukan pengisian sebagai berikut.

* Masukkan directory file (csv) : (diisi dengan directory atau lokasi file yang akan digunakan **harus format .csv**)
* Masukkan nama kolom kode unik user : (diisi dengan nama kolom user id) --> CustomerID jika menggunakan contoh data di folder data
* Masukkan nama kolom parameter recency : (diisi dengan nama kolom yang berisi tanggal transaksi) --> InvoiceDate jika menggunakan contoh data di folder data
* Masukkan nama kolom parameter frequency : (diisi dengan nama kolom yang berisi transaction id) --> InvoiceNo jika menggunakan contoh data di folder data
* Masukkan nama kolom parameter monetary : (diisi dengan nama kolom yang berisi besar uang saat transaksi) --> TotalPrice jika menggunakan contoh data di folder data

Saat sudah selesai akan muncul perintah masukkan nama file untuk menyimpan hasil perhitungan. File disimpan dengan format .csv sehingga saat memasukkan nama file harap menggunakan .csv setelah nama file.

[^note:]
Tidak bisa menggunakan data yang belum dikalikan antara quantity dengan price
