# ⚽ Dasbor Analisis & Prediksi FIFA 21

Sebuah aplikasi web interaktif yang dibangun dengan Streamlit untuk menganalisis data pemain FIFA 21 dan memprediksi nilai pasar (Market Value) mereka menggunakan model *Machine Learning* (Random Forest).

**Proyek ini dibuat untuk memenuhi Tugas Akhir mata kuliah Aplikasi Web.**

* **Oleh:** Rizal Haryaputra (23051130013)
* **Prodi:** Teknologi Informasi
* **Institusi:** Universitas Negeri Yogyakarta

---

## 🚀 Demo Langsung (Live Demo)

Anda dapat mengakses aplikasi yang sudah di-deploy di sini:

**[➡️ Buka Aplikasi Langsung](https://fifa-analytics.streamlit.app/)**

*(Catatan: Harap ganti tautan di atas dengan URL aplikasi Streamlit Cloud Anda setelah berhasil deploy)*

## ✨ Fitur Utama

Aplikasi ini terdiri dari 3 halaman utama dengan navigasi kustom menggunakan navbar yang responsif:

1. **🏠 Halaman Utama (`app.py`)**
   * *Landing page* modern dan responsif yang dibuat dengan HTML/CSS kustom di dalam Streamlit.
   * Menampilkan deskripsi proyek, fitur unggulan, dan info tentang proyek.
   * Tombol navigasi kustom untuk berpindah ke halaman lain.

2. **📈 Dashboard Analisis (`pages/1_Dashboard_Analisis.py`)**
   * Panel filter interaktif (tanpa sidebar) yang memungkinkan pengguna memfilter data berdasarkan:
     * Negara (Nationality)
     * Klub (Club)
     * Grup Posisi (Attackers, Midfielders, etc.)
     * Rentang Rating (Overall)
   * Menampilkan 4 Metrik KPI (Total Pemain, Rata-rata Rating, Umur, dan Nilai Pasar).
   * Visualisasi data interaktif menggunakan Plotly:
     * Distribusi Umur (Histogram)
     * Distribusi Rating OVA (Histogram)
     * Korelasi Rating vs Nilai Pasar (Scatter Plot)
     * Top 10 Pemain (Bar Chart)
   * Tabel data mentah yang sudah terfilter.

3. **🤖 Prediktor Nilai Pasar (`pages/2_Prediksi_Market_Value.py`)**
   * Memuat model *Machine Learning* **Random Forest Regressor** (`.pkl`) yang sudah dilatih.
   * Form input yang *user-friendly* untuk 4 fitur utama:
     * `Overall Rating (OVA)`
     * `Potential Rating (POT)`
     * `Best Overall Rating (BOV)`
     * `Gaji Mingguan (Wage)`
   * Menampilkan hasil estimasi nilai pasar pemain secara *real-time*.

---

## 🛠️ Teknologi yang Digunakan

* **Frontend/UI:** Streamlit
* **Analisis Data:** Pandas
* **Visualisasi Data:** Plotly Express
* **Machine Learning:** Scikit-learn (untuk `RandomForestRegressor`)
* **Serialisasi Model:** Joblib
* **Penyimpanan File Besar:** Git LFS (Large File Storage)
