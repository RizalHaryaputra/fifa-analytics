import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard Analisis - FIFA 21",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    #MainMenu, header, footer { visibility: hidden; }
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
    }

    /* NAVBAR FIXED TOP */
    .navbar {
        position: fixed; top: 0; left: 0; right: 0;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: 1rem 5%;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        z-index: 99999;
        display: flex; justify-content: space-between; align-items: center;
    }
    .navbar-logo {
        font-size: 1.5rem; font-weight: 800;
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .navbar-links { display: flex; gap: 2rem; }
    .nav-link { 
        color: #64748b; font-weight: 600; transition: .3s; 
        font-size: 0.95rem; text-decoration: none !important; 
    }
    .nav-link:hover { color: #2563eb; }
    
    .main-content { margin-top: 60px; }

    .dashboard-title {
        font-size: 2.5rem; font-weight: 800; color: #0f172a;
        margin-bottom: 0.5rem;
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .dashboard-subtitle { color: #64748b; font-size: 1.1rem; margin-bottom: 2rem; }

    /* --- KUNCI PERBAIKAN CARD --- */
    /* Target container yang punya border (st.container(border=True)) */
    [data-testid="stVerticalBlockBorderWrapper"] > div > [data-testid="stVerticalBlock"] {
        /* Ini menargetkan konten di dalam border wrapper */
    }

    /* Kita target wrapper-nya langsung untuk styling card */
    [data-testid="stVerticalBlockBorderWrapper"] > div {
        border-radius: 16px !important;
        border: 1px solid #f1f5f9 !important;
        background-color: white !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05) !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }

    /* Metric Styling */
    [data-testid="stMetric"] {
        background: white; padding: 1rem 1.5rem; border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
        text-align: center;
    }
    [data-testid="stMetricValue"] { font-size: 1.8rem; font-weight: 800; color: #2563eb; }
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
        <a href="Dashboard_Analisis" target="_self" class="nav-link" style="color: #2563eb;">Dashboard</a>
        <a href="Prediksi_Market_Value" target="_self" class="nav-link">Prediksi</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

# ---------------------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------------------
@st.cache_data
def load_data():
    DATA_PATH = "data/fifa21_male2.csv"
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        st.error(f"File tidak ditemukan di: {DATA_PATH}")
        return pd.DataFrame()

    def clean_currency(val):
        if isinstance(val, str):
            val = val.replace('€', '').replace('.', '')
            if 'M' in val: val = float(val.replace('M', '')) * 1000000
            elif 'K' in val: val = float(val.replace('K', '')) * 1000
            return float(val)
        return val

    for col in ['Value', 'Wage', 'Release Clause']:
        if col in df.columns: df[col] = df[col].apply(clean_currency)

    if 'Club' in df.columns: df['Club'] = df['Club'].fillna('Unknown')
    if 'Nationality' in df.columns: df['Nationality'] = df['Nationality'].fillna('Unknown')
    if 'BP' in df.columns: df['BP'] = df['BP'].fillna('Unknown')
    return df

df = load_data()
if df.empty: st.stop()

# ---------------------------------------------------------------------
# KONTEN DASHBOARD
# ---------------------------------------------------------------------
st.markdown('<h1 class="dashboard-title">📈 Dashboard Analisis Pemain</h1>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Eksplorasi interaktif data pemain FIFA 21. Gunakan filter di bawah untuk menyesuaikan analisis.</p>', unsafe_allow_html=True)

# --- FILTER ---
# Gunakan st.container(border=True) yang sudah kita styling ulang via CSS
with st.container(border=True):
    with st.expander("🔍 Klik di sini untuk Buka/Tutup Filter Data", expanded=True):
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            all_nationalities = sorted(df['Nationality'].astype(str).unique().tolist())
            selected_nationality = st.multiselect("🌐 Negara (Nationality)", all_nationalities)
        with f_col2:
            all_clubs = sorted(df['Club'].astype(str).unique().tolist())
            selected_club = st.multiselect("⚽ Klub (Club)", all_clubs)
        with f_col3:
            posisi_dict = {
                "Attackers": ['ST', 'CF', 'RW', 'LW', 'RF', 'LF', 'RS', 'LS'],
                "Midfielders": ['CAM', 'CDM', 'CM', 'LM', 'RM', 'LAM', 'RAM', 'LCM', 'RCM'],
                "Defenders": ['CB', 'LB', 'RB', 'LWB', 'RWB', 'LCB', 'RCB'],
                "Goalkeepers": ['GK']
            }
            selected_pos_group = st.multiselect("🏃 Posisi", list(posisi_dict.keys()))
        
        min_ova, max_ova = int(df['OVA'].min()), int(df['OVA'].max())
        selected_ova = st.slider("⭐ Rentang Rating (Overall)", min_ova, max_ova, (min_ova, max_ova))

# --- APPLY FILTERS ---
filtered_df = df.copy()
if selected_nationality: filtered_df = filtered_df[filtered_df['Nationality'].isin(selected_nationality)]
if selected_club: filtered_df = filtered_df[filtered_df['Club'].isin(selected_club)]
if selected_pos_group:
    pos_to_keep = []
    for group in selected_pos_group: pos_to_keep.extend(posisi_dict[group])
    filtered_df = filtered_df[filtered_df['BP'].isin(pos_to_keep)]
filtered_df = filtered_df[(filtered_df['OVA'] >= selected_ova[0]) & (filtered_df['OVA'] <= selected_ova[1])]

# --- KPI ---
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Pemain", f"{len(filtered_df):,}")
col2.metric("Rata-rata Rating", f"{filtered_df['OVA'].mean():.1f}")
col3.metric("Rata-rata Umur", f"{filtered_df['Age'].mean():.1f} Thn")
avg_val = filtered_df['Value'].mean()
val_formatted = f"€ {avg_val/1e6:.1f} M" if avg_val >= 1e6 else f"€ {avg_val/1e3:.0f} K"
col4.metric("Rata-rata Nilai", val_formatted)
st.markdown("<br>", unsafe_allow_html=True)

# --- GRAFIK ---
col_g1, col_g2 = st.columns(2)
with col_g1:
    with st.container(border=True):
        st.subheader("🎂 Distribusi Umur")
        fig_age = px.histogram(filtered_df, x="Age", nbins=20, color_discrete_sequence=['#3b82f6'])
        fig_age.update_layout(xaxis_title="Umur", yaxis_title="Jumlah", template="plotly_white", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_age, use_container_width=True)
with col_g2:
    with st.container(border=True):
        st.subheader("⭐ Distribusi Rating (OVA)")
        fig_ova = px.histogram(filtered_df, x="OVA", nbins=20, color_discrete_sequence=['#10b981'])
        fig_ova.update_layout(xaxis_title="Rating", yaxis_title="Jumlah", template="plotly_white", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_ova, use_container_width=True)

col_g3, col_g4 = st.columns([1.5, 1])
with col_g3:
    with st.container(border=True):
        st.subheader("💰 Hubungan Rating vs Nilai Pasar")
        fig_corr = px.scatter(filtered_df, x="OVA", y="Value", color="BP", hover_data=['Name', 'Club'], opacity=0.7)
        fig_corr.update_layout(template="plotly_white", xaxis_title="Rating (OVA)", yaxis_title="Nilai (€)", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig_corr, use_container_width=True)
with col_g4:
    with st.container(border=True):
        st.subheader("🏆 Top 10 Pemain")
        top_10 = filtered_df.nlargest(10, 'OVA').sort_values('OVA', ascending=True)
        fig_top = px.bar(top_10, x="OVA", y="Name", orientation='h', color="OVA", color_continuous_scale='viridis', text="OVA")
        fig_top.update_layout(xaxis_title="Rating", yaxis_title=None, template="plotly_white", plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', coloraxis_showscale=False, margin=dict(l=10, r=10, t=30, b=10))
        fig_top.update_traces(textposition='inside')
        st.plotly_chart(fig_top, use_container_width=True)

# --- TABEL DATA ---
with st.container(border=True):
    st.subheader("📋 Data Pemain (Terfilter)")
    with st.expander("Klik untuk melihat data tabel lengkap"):
        st.dataframe(filtered_df[['Name', 'Age', 'Nationality', 'Club', 'BP', 'OVA', 'Value', 'Wage']].style.format({"Value": "€{:,.0f}", "Wage": "€{:,.0f}"}), use_container_width=True, height=400)

st.markdown('</div>', unsafe_allow_html=True)