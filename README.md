# 🌧️ Dashboard Curah Hujan Kota Bandung

Dashboard interaktif untuk visualisasi dan analisis data curah hujan bulanan di Kota Bandung menggunakan Streamlit.

## 📋 Deskripsi

Dashboard ini menampilkan data **curah hujan bulanan** berdasarkan dataset resmi Kota Bandung. Aplikasi ini memungkinkan pengguna untuk:

- Memfilter data berdasarkan tahun dan bulan
- Melihat statistik ringkas (jumlah bulan, total curah hujan, rata-rata bulanan)
- Memvisualisasikan data dalam bentuk grafik line chart
- Menampilkan data mentah dalam format tabel

## 🚀 Fitur

- ✅ Filter berdasarkan tahun
- ✅ Filter multi-select berdasarkan bulan
- ✅ Statistik ringkas (jumlah bulan, total, dan rata-rata curah hujan)
- ✅ Visualisasi grafik line chart interaktif
- ✅ Tabel data mentah yang dapat di-filter
- ✅ UI yang user-friendly dengan Streamlit

## 📦 Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda telah menginstall:

- Python 3.7 atau lebih tinggi
- pip (Python package manager)

## 🔧 Instalasi

1. **Clone atau download repository ini**

2. **Masuk ke direktori dashboard**
   ```bash
   cd dashboard_hujan
   ```

3. **Buat virtual environment (opsional, tetapi direkomendasikan)**
   ```bash
   python -m venv venv
   ```

4. **Aktifkan virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies**
   ```bash
   pip install streamlit pandas matplotlib
   ```

   Atau jika sudah ada file `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Cara Menjalankan

1. **Pastikan Anda berada di direktori `dashboard_hujan`**
   ```bash
   cd dashboard_hujan
   ```

2. **Jalankan aplikasi Streamlit**
   ```bash
   streamlit run app.py
   ```

3. **Buka browser dan akses URL yang ditampilkan** (biasanya `http://localhost:8501`)

## 📁 Struktur Proyek

```
dataset/
├── dashboard_hujan/
│   ├── app.py                          # File utama aplikasi Streamlit
│   ├── curah_hujan_kota_bandung.csv    # Dataset curah hujan
│   └── venv/                           # Virtual environment (jika ada)
└── README.md                           # File ini
```

## 📊 Format Data

Dataset `curah_hujan_kota_bandung.csv` memiliki struktur sebagai berikut:

| Kolom | Deskripsi |
|-------|-----------|
| `id` | ID unik untuk setiap record |
| `kode_provinsi` | Kode provinsi (32 = Jawa Barat) |
| `nama_provinsi` | Nama provinsi |
| `bps_kode_kabupaten_kota` | Kode BPS untuk kabupaten/kota |
| `bps_nama_kabupaten_kota` | Nama kabupaten/kota |
| `bulan` | Nama bulan (JANUARI, FEBRUARI, dst.) |
| `jumlah_curah_hujan` | Jumlah curah hujan dalam mm |
| `satuan` | Satuan pengukuran (MM) |
| `tahun` | Tahun pengukuran |

## 🛠️ Teknologi yang Digunakan

- **Streamlit** - Framework untuk membuat aplikasi web interaktif
- **Pandas** - Library untuk manipulasi dan analisis data
- **Matplotlib** - Library untuk visualisasi data

## 📝 Penggunaan

1. **Pilih Tahun**: Gunakan dropdown untuk memilih tahun yang ingin dianalisis
2. **Pilih Bulan**: Gunakan multi-select untuk memilih satu atau lebih bulan
3. **Lihat Statistik**: Statistik ringkas akan otomatis terupdate berdasarkan filter
4. **Analisis Grafik**: Grafik line chart akan menampilkan pola curah hujan per bulan
5. **Eksplorasi Data**: Scroll ke bawah untuk melihat tabel data mentah


## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik (Semester 7).

## 👤 Author

Dibuat untuk memenuhi Tugas Besar Mata Kuliah Data Sains

## 🙏 Acknowledgments

- Data curah hujan dari dataset resmi Kota Bandung
- Streamlit untuk framework yang powerful dan mudah digunakan

---

**Catatan**: Pastikan file `curah_hujan_kota_bandung.csv` berada di direktori yang sama dengan `app.py` agar aplikasi dapat berjalan dengan baik.

