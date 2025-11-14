# ⚽ Dasbor Analisis & Prediksi FIFA 21

Sebuah aplikasi web interaktif berbasis **Streamlit** untuk menganalisis
data pemain FIFA 21 dan memprediksi **Market Value** menggunakan model
*Machine Learning* (Random Forest).

## 👤 Informasi Proyek

-   **Nama:** Rizal Haryaputra\
-   **NIM:** 23051130013\
-   **Prodi:** Teknologi Informasi\
-   **Institusi:** Universitas Negeri Yogyakarta\
-   **Kegunaan:** Tugas Akhir Mata Kuliah Aplikasi Web

------------------------------------------------------------------------

## 🚀 Demo Langsung

Akses aplikasi yang sudah di-deploy:\
➡️ **https://fifa-analytics.streamlit.app/**

------------------------------------------------------------------------

## ✨ Fitur Utama

### 🏠 1. Halaman Utama (`app.py`)

-   Landing page modern (HTML + CSS custom)
-   Navigasi halaman tanpa sidebar
-   Deskripsi aplikasi dan fitur

### 📈 2. Dashboard Analisis (`pages/1_Dashboard_Analisis.py`)

-   Filter interaktif:
    -   Negara
    -   Klub
    -   Grup posisi
    -   Rating (Overall)
-   KPI Cards:
    -   Total Pemain
    -   Rata-rata OVA
    -   Rata-rata Umur
    -   Rata-rata Market Value
-   Grafik Plotly:
    -   Histogram umur
    -   Histogram OVA
    -   Scatter OVA vs Market Value
    -   Top 10 pemain

### 🤖 3. Prediksi Market Value (`pages/2_Prediksi_Market_Value.py`)

-   Menggunakan model RandomForestRegressor
-   Input fitur:
    -   OVA
    -   POT
    -   BOV
    -   Wage (gaji/minggu)
-   Output estimasi Market Value pemain

------------------------------------------------------------------------

## 🛠️ Teknologi Yang Digunakan

-   Streamlit\
-   Pandas\
-   Plotly Express\
-   Scikit-learn\
-   Joblib\
-   Git LFS

------------------------------------------------------------------------

## 📁 Struktur Folder

    FIFA-Analytics-Dashboard/
    │── app.py
    │── requirements.txt
    │── ilustrasi.png
    │── data/
    │   └── fifa21_male2.csv
    │── models/
    │   └── random_forest_model.pkl
    │── pages/
        ├── 1_Dashboard_Analisis.py
        └── 2_Prediksi_Market_Value.py

------------------------------------------------------------------------

## 🏃 Cara Menjalankan di Lokal

### 1️⃣ Clone Repo

``` bash
git clone https://github.com/RizalHaryaputra/fifa-analytics.git
cd fifa-analytics
```

### 2️⃣ Instal Git LFS

``` bash
git lfs install
git lfs pull
```

### 3️⃣ Buat Virtual Environment

``` bash
python -m venv venv
venv/Scripts/activate
```

### 4️⃣ Instal Semua Dependensi

``` bash
pip install -r requirements.txt
```

### 5️⃣ Jalankan Streamlit

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 📊 Sumber Data

Dataset Kaggle: https://www.kaggle.com/code/paramarthasengupta/fifa-21-eda-and-visualization?select=fifa21_male2.csv

------------------------------------------------------------------------

## 📄 Lisensi

Proyek ini hanya untuk keperluan akademik.
