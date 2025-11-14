⚽ Dasbor Analisis & Prediksi FIFA 21Sebuah aplikasi web interaktif yang dibangun dengan Streamlit untuk menganalisis data pemain FIFA 21 dan memprediksi nilai pasar (Market Value) mereka menggunakan model Machine Learning (Random Forest).Proyek ini dibuat untuk memenuhi Tugas Akhir mata kuliah Aplikasi Web.Oleh: Rizal Haryaputra (23051130013)Prodi: Teknologi InformasiInstitusi: Universitas Negeri Yogyakarta🚀 Demo Langsung (Live Demo)Anda dapat mengakses aplikasi yang sudah di-deploy di sini:[➡️ Buka Aplikasi Langsung]([https://[!! GANTI DENGAN LINK STREAMLIT CLOUD ANDA !!]](https://fifa-analytics.streamlit.app/))(Catatan: Harap ganti tautan di atas dengan URL aplikasi Streamlit Cloud Anda setelah berhasil deploy)📸 Tangkapan LayarHalaman Utama (Landing Page)Dashboard AnalisisHalaman Prediksi![Halaman Utama]([GANTI DENGAN URL SCREENSHOT APP.PY])![Dashboard Analisis]([GANTI DENGAN URL SCREENSHOT DASHBOARD])![Halaman Prediksi]([GANTI DENGAN URL SCREENSHOT PREDIKSI])(Tips: Ambil screenshot aplikasi Anda, unggah ke tab "Issues" di repositori GitHub Anda, lalu salin dan tempel tautan gambar tersebut ke dalam tanda [] di atas untuk menampilkannya di sini).✨ Fitur UtamaAplikasi ini terdiri dari 3 halaman utama dengan navigasi kustom menggunakan navbar yang responsif:🏠 Halaman Utama (app.py)Landing page modern dan responsif yang dibuat dengan HTML/CSS kustom di dalam Streamlit.Menampilkan deskripsi proyek, fitur unggulan, dan info tentang proyek.Tombol navigasi kustom untuk berpindah ke halaman lain.📈 Dashboard Analisis (pages/1_Dashboard_Analisis.py)Panel filter interaktif (tanpa sidebar) yang memungkinkan pengguna memfilter data berdasarkan:Negara (Nationality)Klub (Club)Grup Posisi (Attackers, Midfielders, etc.)Rentang Rating (Overall)Menampilkan 4 Metrik KPI (Total Pemain, Rata-rata Rating, Umur, dan Nilai Pasar).Visualisasi data interaktif menggunakan Plotly:Distribusi Umur (Histogram)Distribusi Rating OVA (Histogram)Korelasi Rating vs Nilai Pasar (Scatter Plot)Top 10 Pemain (Bar Chart)Tabel data mentah yang sudah terfilter.🤖 Prediktor Nilai Pasar (pages/2_Prediksi_Market_Value.py)Memuat model Machine Learning Random Forest Regressor (.pkl) yang sudah dilatih.Form input yang user-friendly untuk 4 fitur utama:Overall Rating (OVA)Potential Rating (POT)Best Overall Rating (BOV)Gaji Mingguan (Wage)Menampilkan hasil estimasi nilai pasar pemain secara real-time.🛠️ Teknologi yang DigunakanFrontend/UI: StreamlitAnalisis Data: PandasVisualisasi Data: Plotly ExpressMachine Learning: Scikit-learn (untuk RandomForestRegressor)Serialisasi Model: JoblibPenyimpanan File Besar: Git LFS (Large File Storage)📁 Struktur Folder ProyekFIFA-Analytics-Dashboard/
│
├── 📄 app.py                   (Halaman Utama / Landing Page)
├── 📄 requirements.txt         (Daftar library untuk deploy)
├── 🖼️ ilustrasi.png            (Gambar untuk landing page)
│
├── 📁 data/
│   └── 📄 players_21.csv       (Dikelola oleh Git LFS)
│
├── 📁 models/
│   └── 📄 random_forest_model.pkl (Model 111MB, dikelola oleh Git LFS)
│
└── 📁 pages/
    ├── 📄 1_Dashboard_Analisis.py
    ├── 📄 2_Prediksi_Market_Value.py
    └── 📄 3_Metodologi_Proyek.py
🏃 Menjalankan Proyek Secara LokalUntuk menjalankan aplikasi ini di komputer Anda, ikuti langkah-langkah berikut:PENTING: Proyek ini menggunakan Git LFS untuk file model dan data yang besar.Clone Repositori:git clone [https://github.com/RizalHaryaputra/nama-repo-anda.git](https://github.com/RizalHaryaputra/nama-repo-anda.git)
cd nama-repo-anda
Instal Git LFS:Anda harus menginstal Git LFS di komputer Anda untuk mengunduh file model (.pkl) dan data (.csv).# Instal LFS (hanya perlu sekali per komputer)
git lfs install

# Tarik file besar dari LFS
git lfs pull
Jika Anda tidak melakukan git lfs pull, file model Anda hanya akan berupa file teks penunjuk kecil dan aplikasi akan error.Buat Virtual Environment (Sangat Direkomendasikan):# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
Instal Semua Kebutuhan (Libraries):Pastikan Anda memiliki file requirements.txt dari proyek ini.pip install -r requirements.txt
Jalankan Aplikasi Streamlit:streamlit run app.py
Aplikasi akan otomatis terbuka di browser Anda.📊 Sumber DataKaggle: FIFA 21 Complete Player DatasetData yang digunakan telah dibersihkan (pre-processed) dari dataset di atas.
