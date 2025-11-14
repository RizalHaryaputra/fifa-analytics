import streamlit as st
import base64
import os

# ---------------------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="FIFA 21 Analytics Dashboard",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------------------
# FUNGSI BANTUAN UNTUK GAMBAR LOKAL
# ---------------------------------------------------------------------
def get_img_as_base64(file_path):
    """
    Membaca file gambar lokal dan mengembalikannya sebagai string base64 
    agar bisa digunakan di dalam tag HTML <img>.
    """
    if not os.path.exists(file_path):
        return "" # Kembalikan string kosong jika file tidak ditemukan
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Membaca gambar lokal dan mengonversinya ke base64
img_path = "ilustrasi.png" 
img_base64 = get_img_as_base64(img_path)

# Jika gambar lokal tidak ada, gunakan placeholder online sebagai cadangan
if img_base64:
    hero_image_src = f"data:image/png;base64,{img_base64}"
else:
    # Placeholder jika gambar lokal tidak ditemukan.
    hero_image_src = "https://placehold.co/1200x600/e2e8f0/1e293b?text=Gambar+Tidak+Ditemukan+(Cek+Nama+File)"

# ---------------------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* GLOBAL STYLES */
* { font-family: 'Inter', sans-serif; margin-top: 0 !important; padding: 0; box-sizing: border-box; }
#MainMenu, footer, header { visibility: hidden; }
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
}
a { text-decoration: none !important; }

/* NAVBAR */
.navbar {
    position: fixed; top: 0; left: 0; right: 0;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    padding: 1rem 5%; /* Responsive padding */
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    z-index: 9999;
    display: flex; justify-content: space-between; align-items: center;
}
.navbar-logo {
    font-size: 1.5rem; font-weight: 800;
    background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.navbar-links { display: flex; gap: 2rem; }
.nav-link { color: #64748b; font-weight: 600; transition: .3s; font-size: 0.95rem; }
.nav-link:hover { color: #2563eb; }

/* HERO SECTION */
.hero-section {
    margin-top: 80px;
    padding: 6rem 2rem 4rem;
    text-align: center;
    display: flex; flex-direction: column; align-items: center;
}
.hero-badge {
    display: inline-block; background: #dbeafe; color: #1e40af;
    padding: 0.5rem 1.5rem; border-radius: 50px;
    font-weight: 600; font-size: 0.9rem; margin-bottom: 1.5rem;
    border: 1px solid #bfdbfe;
}
.hero-title {
    font-size: 4rem; font-weight: 900; color: #0f172a;
    line-height: 1.1; margin-bottom: 1.5rem; letter-spacing: -0.02em;
}
@media (max-width: 768px) { .hero-title { font-size: 2.5rem; } }
.hero-gradient {
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    color: #64748b; font-size: 1.25rem; max-width: 700px;
    margin: 0 auto 2.5rem; line-height: 1.6;
}
.hero-image-container {
    margin: 1rem auto;
    max-width: 800px;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.hero-image { width: 100%; display: block; }

/* BUTTONS */
.hero-buttons { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn {
    padding: 0.8rem 2rem; border-radius: 50px; font-weight: 600;
    transition: all 0.3s ease; display: inline-flex; align-items: center; gap: 0.5rem;
}
.btn-primary {
    background: linear-gradient(135deg, #2563eb, #4f46e5); color: white !important;
    box-shadow: 0 10px 25px -10px rgba(37, 99, 235, 0.6);
}
.btn-primary:hover { transform: translateY(-3px); box-shadow: 0 15px 30px -10px rgba(37, 99, 235, 0.7); }
.btn-secondary {
    background: white; color: #0f172a !important; border: 1px solid #e2e8f0;
}
.btn-secondary:hover { border-color: #2563eb; color: #2563eb !important; transform: translateY(-3px); }

/* SECTIONS */
.section-container { padding: 6rem 2rem; max-width: 1200px; margin: 0 auto; }
.section-title {
    text-align: center; font-size: 2.5rem; font-weight: 800;
    color: #0f172a; margin-bottom: 3rem; letter-spacing: -0.02em;
}

/* FEATURE CARDS */
.feature-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem; padding: 1rem;
}
.feature-card {
    background: white; padding: 2.5rem 2rem; border-radius: 24px;
    box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);
    text-align: center; transition: all 0.3s ease; border: 1px solid #f1f5f9;
    height: 100%; display: flex; flex-direction: column; align-items: center;
}
.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1);
    border-color: #e0e7ff;
}
.feature-icon {
    font-size: 3.5rem; margin-bottom: 1.5rem;
    background: #eef2ff; width: 80px; height: 80px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 20px;
}
.feature-title { font-size: 1.25rem; font-weight: 700; color: #1e293b; margin-bottom: 1rem; }
.feature-desc { color: #64748b; line-height: 1.6; }

/* FOOTER */
.footer {
    text-align: center; padding: 4rem 2rem; margin-top: 4rem;
    background: white; border: 1px solid #e2e8f0; border-radius: 20px;
}
.footer-logo {
    font-size: 1.4rem; font-weight: 800; margin-bottom: 1rem;
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.footer-text { color: #64748b; line-height: 1.8; }
.footer-link { color: #2563eb; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="navbar-logo">⚽ FIFA Analytics</div>
    <div class="navbar-links">
        <a href="/" class="nav-link" style="color: #2563eb";>Home</a>
        <a href="Dashboard_Analisis" target="_self" class="nav-link"">Dashboard</a>
        <a href="Prediksi_Market_Value" target="_self" class="nav-link">Prediksi</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------------------
# Kita menggunakan f-string di sini untuk memasukkan variabel hero_image_src yang sudah berisi base64 gambar lokal.
st.markdown(f"""
<div class="hero-section" id="home">
    <div class="hero-badge">📊 Tugas Akhir Aplikasi Web</div>
    <h1 class="hero-title">
        Jelajahi Data Pemain & <br>
        <span class="hero-gradient">Prediksi Nilai Pasar</span>
    </h1>
    <div class="hero-image-container">
        <img src="{hero_image_src}" alt="App Preview" class="hero-image">
    </div>
    <p class="hero-subtitle">
        Platform interaktif untuk menganalisis statistik lebih dari 17.000 pemain FIFA 21 
        dan memprediksi nilai pasar mereka menggunakan Machine Learning.
    </p>
    <div class="hero-buttons">
        <a href="Dashboard_Analisis" target="_self" class="btn btn-primary">🚀 Buka Dashboard</a>
        <a href="Prediksi_Market_Value" target="_self" class="btn btn-secondary">🤖 Coba Prediksi</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# FEATURES SECTION
# ---------------------------------------------------------------------
st.markdown("""
<div class="section-container" id="features">
    <h2 class="section-title">Fitur Unggulan</h2>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <h3 class="feature-title">Visualisasi Interaktif</h3>
            <p class="feature-desc">
                Jelajahi distribusi umur, rating, dan gaji pemain melalui grafik yang dinamis dan mudah dipahami.
            </p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3 class="feature-title">Prediksi Akurat</h3>
            <p class="feature-desc">
                Gunakan model Machine Learning kami untuk memperkirakan nilai pasar pemain berdasarkan statistik mereka.
            </p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3 class="feature-title">Filter Canggih</h3>
            <p class="feature-desc">
                Temukan pemain spesifik dengan filter mendetail berdasarkan klub, negara, posisi, dan rating overall.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# ABOUT SECTION
# ---------------------------------------------------------------------
st.markdown("""
<div class="section-container" id="about" style="background: white; border-radius: 30px; margin-top: 4rem; margin-bottom: 4rem;">
    <h2 class="section-title">Tentang Proyek Ini</h2>
    <div style="max-width: 800px; margin: 0 auto; text-align: center; color: #475569; line-height: 1.8; font-size: 1.1rem;">
        <p>
            Aplikasi ini dikembangkan sebagai proyek akhir untuk mata kuliah <b>Aplikasi Web</b>. 
            Kami memanfaatkan dataset komprehensif dari Kaggle yang berisi data ribuan pemain FIFA 21.
        </p>
        <p style="margin-top: 1.5rem;">
            Tujuan kami adalah mendemonstrasikan bagaimana data mentah dapat diolah menjadi 
            <i>insight</i> yang berharga melalui visualisasi data dan penerapan model prediksi sederhana.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------
st.markdown("""
<div class="footer">
    <div class="footer-logo">⚽ FIFA Analytics Dashboard</div>
    <div class="footer-text">
        Dibuat dengan ❤️ oleh <b>Rizal Haryaputra</b> (23051130013)<br>
        Program Studi <b>Teknologi Informasi</b> — Universitas Negeri Yogyakarta<br>
        <br>
        Data didukung oleh <a href="https://www.kaggle.com/code/paramarthasengupta/fifa-21-eda-and-visualization?select=fifa21_male2.csv" target="_blank" class="footer-link">Kaggle FIFA 21 Dataset</a>
    </div>
</div>
""", unsafe_allow_html=True)