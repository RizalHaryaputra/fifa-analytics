import streamlit as st
import pandas as pd
import joblib  # Gunakan joblib untuk memuat model scikit-learn
import os
import time

# ---------------------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Prediksi Market Value",
    page_icon="🤖",
    layout="centered",  # Layout "centered" lebih cocok untuk form
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------------------
# CUSTOM CSS (Sama seperti halaman lain)
# ---------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    :root {
        --primary-color: #2563eb;
        --secondary-color: #4f46e5;
        --bg-gradient-start: #f8fafc;
        --bg-gradient-end: #eef2ff;
        --card-bg: #ffffff;
        --text-primary: #0f172a;
        --text-secondary: #64748b;
    }

    * { font-family: 'Inter', sans-serif; }
    
    #MainMenu, header, footer { visibility: hidden; }
    .stApp {
        background: linear-gradient(135deg, var(--bg-gradient-start) 0%, var(--bg-gradient-end) 100%);
    }

    /* NAVBAR BERGAYA FROSTED GLASS */
    .navbar {
        position: fixed; top: 0; left: 0; right: 0;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 0.8rem 5%;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.03);
        border-bottom: 1px solid rgba(255, 255, 255, 0.3);
        z-index: 999999;
        display: flex; justify-content: space-between; align-items: center;
    }
    .navbar-logo {
        font-size: 1.4rem; font-weight: 800;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }
    .nav-link { 
        color: var(--text-secondary); font-weight: 600; transition: all 0.3s ease; 
        font-size: 0.9rem; text-decoration: none !important; padding: 0.5rem 1rem; border-radius: 8px;
    }
    .nav-link:hover, .nav-link.active { 
        color: var(--primary-color); background: rgba(37, 99, 235, 0.05);
    }
    
    .main-content { margin-top: 80px; } /* Jarak dari navbar */

    /* Judul Halaman Prediksi */
    .pred-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .pred-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* Styling Form sebagai Card Premium */
    [data-testid="stForm"] {
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        background: rgba(255, 255, 255, 0.8) !important; /* Sedikit transparan */
        backdrop-filter: blur(10px) !important;
        box-shadow: 
            0 4px 6px -1px rgba(0, 0, 0, 0.02), 
            0 10px 15px -3px rgba(0, 0, 0, 0.04),
            inset 0 0 0 1px rgba(255, 255, 255, 0.5) !important;
        padding: 2rem !important;
    }
    
    /* Styling tombol submit */
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
        color: #ffffff;
    }
    [data-testid="stFormSubmitButton"] > button:hover {
        opacity: 0.9;
        box-shadow: 0 10px 20px -10px rgba(37, 99, 235, 0.4);
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# NAVBAR
# ---------------------------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="navbar-logo">⚽ FIFA Analytics</div>
    <div class="navbar-links">
        <a href="/" target="_self" class="nav-link">Home</a>
        <a href="Dashboard_Analisis" target="_self" class="nav-link">Dashboard</a>
        <a href="Prediksi_Market_Value" target="_self" class="nav-link active" style="color: var(--primary-color);">Prediksi</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ---------------------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------------------
@st.cache_resource  # Gunakan cache_resource untuk memuat model
def load_model():
    """Memuat model Random Forest dari file .pkl"""
    # Path model Anda
    MODEL_PATH = "models/random_forest_model.pkl"
    
    if not os.path.exists(MODEL_PATH):
        st.error(f"File model tidak ditemukan di: {MODEL_PATH}")
        st.error("Pastikan file 'random_forest_model.pkl' ada di dalam folder 'models' proyek Anda.")
        return None
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat model: {e}")
        return None

model = load_model()

# ---------------------------------------------------------------------
# KONTEN HALAMAN PREDIKSI
# ---------------------------------------------------------------------
st.markdown('<h1 class="pred-title">🤖 Prediktor Nilai Pasar</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="pred-subtitle">
    Masukkan 4 atribut utama pemain di bawah ini untuk mendapatkan estimasi nilai pasar 
    (Value) menggunakan model Random Forest.
    </p>
    """, unsafe_allow_html=True
)

# Hanya tampilkan form jika model berhasil dimuat
if model:
    with st.form("prediction_form"):
        st.subheader("Atribut Kunci Pemain")
        
        # Buat 2 kolom agar rapi
        col1, col2 = st.columns(2)
        
        with col1:
            # Fitur 1: OVA
            ova = st.slider(
                "⭐ Overall Rating (OVA)", 
                min_value=40, max_value=99, value=75,
                help="Rating kemampuan pemain saat ini (skala 40-99)."
            )
            # Fitur 2: POT
            pot = st.slider(
                "📈 Potential Rating (POT)", 
                min_value=40, max_value=99, value=80,
                help="Potensi rating tertinggi yang bisa dicapai pemain (skala 40-99)."
            )
        
        with col2:
            # Fitur 3: BOV
            bov = st.slider(
                "🎯 Best Overall Rating (BOV)", 
                min_value=40, max_value=99, value=75,
                help="Rating terbaik pemain jika ditempatkan di posisi idealnya (skala 40-99)."
            )
            # Fitur 4: Wage
            wage = st.number_input(
                "💰 Gaji Mingguan (€)", 
                min_value=0, max_value=600000, value=50000, step=1000,
                help="Gaji mingguan pemain dalam Euro (misal: 50000 untuk €50K)."
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Tombol Submit
        submitted = st.form_submit_button("Prediksi Nilai Pasar", use_container_width=True)

    if submitted:
        with st.spinner('Model Random Forest sedang menganalisis...'):
            time.sleep(1) # Efek dramatis
            
            # 1. Siapkan data input untuk model
            # Pastikan urutan dan nama kolom SAMA PERSIS dengan saat Anda melatih model
            # Sesuai permintaan Anda: ['BOV', 'OVA', 'Wage', 'POT']
            try:
                input_data = pd.DataFrame(
                    [[bov, ova, wage, pot]],
                    columns=['BOV', 'OVA', 'Wage', 'POT'] 
                )
                
                # 2. Lakukan prediksi
                prediction = model.predict(input_data)
                result_value = prediction[0] # Ambil hasil prediksi pertama
                
                # 3. Tampilkan hasil
                st.markdown("<br>", unsafe_allow_html=True)
                st.success(f"### Estimasi Nilai Pasar: € {result_value:,.0f}")
                st.info(f"Input: OVA {ova}, POT {pot}, BOV {bov}, Gaji €{wage:,.0f}")
                st.balloons()
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat prediksi: {e}")
                st.error("Pastikan input Anda valid. Jika Anda menggunakan scaler, pastikan scaler juga dimuat dan diterapkan.")

else:
    st.warning("Form prediksi tidak dapat ditampilkan karena model gagal dimuat. Periksa log error di atas.")

st.markdown('</div>', unsafe_allow_html=True) # Penutup main-content