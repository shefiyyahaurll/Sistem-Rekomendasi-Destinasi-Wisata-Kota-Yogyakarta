# **Laporan Proyek Machine Learning - Shefiyyah Aurellia Wahyudi**<br>

## **Sistem-Rekomendasi-Destinasi-Wisata-Kota-Yogyakarta**

## **Project Overview**<br>
Pengunjung wisata di Kota Yogyakarta terus mengalami peningkatan setiap tahunnya, baik dari wisatawan domestik maupun asing. Hal ini menunjukkan bahwa Daerah Istimewa Yogyakarta merupakan destinasi yang sering dikunjungi oleh para wisatawan untuk berlibur. Provinsi ini memiliki banyak objek wisata yang unik dan menarik, seperti gunung, museum, bukit, pantai, goa, air terjun, budaya, dan tempat bersejarah. Oleh karena itu, pengembangan wisata di kota Yogyakarta perlu dilakukan untuk meningkatkan potensi pariwisata dan pendapatan daerah.[1]<br>
Pariwisata adalah salah satu sektor penting bagi perekonomian Indonesia. Keindahan alam dan keanekaragaman budaya merupakan nilai lebih yang dianggap dapat menarik para wisatawan. Salah satu kota yang terkenal di Indonesia akan tempat wisatanya adalah Yogyakarta. Menurut data statistik kepariwisataan DIY tahun 2017 sebanyak 25.950.793 wisatawan datang ke Yogyakarta. Berbagai jenis objek wisata mulai dari wisata alam hingga wisata keagamaan ada di Yogyakarta, sehingga banyak dikunjungi wisatawan domestik maupun wisatawan mancanegara.[2]<br>
Ketika akan berwisata tentu berbagai hal akan menjadi pertimbangan bagi wisatawan, salah satunya adalah membuat rencana perjalanan. Biasanya wisatawan menggunakan jasa agen wisata atau pramuwisata, namun ada juga wisatawan yang merencanakan sendiri tujuan wisatanya, sehingga memerlukan waktu yang lebih banyak untuk mengumpulkan informasi. Informasi yang begitu banyak kadang sering membuat wisatawan bingung dalam memilih tujuan wisatanya.[2] <br>
Berdasarkan masalah tersebut maka dibutuhkan sebuah sistem yang mampu memberikan rekomendasi tempat wisata. Sistem rekomendasi digunakan karena mampu memberikan penyaringan dari informasi yang sangat banyak (overload) di dunia maya untuk memberikan saran/rekomendasi pilihan objek wisata. Perkembangan jumlah informasi yang banyak di dunia maya menyebabkan sulitnya menemukan informasi yang tepat dan sesuai dengan selera/preferensi yang diinginkan wisatawan.[2]

## **Business Understanding**<br>


### Problem Statements

### Goals

#### Solution statements

## **Data Understanding**

## **Data Preparation**

## **Modeling**

## Evaluation<br>

Untuk melihat visualisasi proses training, plot metrik evaluasi dengan matplotlib<br>

![Teks alternatif](dataset/output.png)<br>

Proses training model cukup smooth dan model konvergen pada epochs dengan menggunakan callbacks untuk mencapai 'root_mean_squared_error' dan 'val_root_mean_squared_error' terbaik. Dari proses ini memperoleh nilai error akhir sebesar sekitar 0.3339 dan error pada data validasi sebesar 0.3560. Nilai tersebut cukup bagus untuk sistem rekomendasi.<br>


- Berhasil memberikan rekomendasi kepada user. Sebagai contoh, hasil di atas adalah rekomendasi untuk user dengan id 27. Dari output tersebut, kita dapat membandingkan antara Tempat wisata di Yogyakarta dengan rating tertinggi dari pengguna dan Top 10 Rekomendasi Tempat wisata di Yogyakarta dari Pengguna. <br>
- Beberapa Tempat wisata rekomendasi di Yogyakarta menyediakan kategori tempat wisata yang sesuai dengan rating user. Pengguna memperoleh 5 rekomendasi tempat wisata di Yogyakarta dengan kategori ‘Category' Taman Hiburam, 3 rekomendasi tempat wisata di Yogyakarta dengan kategori Budaya, dan 2 tempat wisata di Yogyakarta dengan kategori Cagar Alam.<br>


### **Referensi**<br>
[1]	A. Hanafi Ahmad, “Pengaruh Jumlah Kunjungan Wisatawan, Objek Wisata, Dan Retribusi Pariwisata Terhadap Pendapatan Asli Daerah,” J. Sos. Ekon. Bisnis, vol. 2, no. 1, pp. 50–61, 2022, doi: 10.55587/jseb.v2i1.34.<br>

[2]	A. S. N. S. Ningrum, “Content Based Dan Collaborative Filtering Pada Rekomendasi Tujuan Pariwisata Di Daerah Yogyakarta,” Telematika, vol. 16, no. 1, p. 44, 2019, doi: 10.31315/telematika.v16i1.3023.







