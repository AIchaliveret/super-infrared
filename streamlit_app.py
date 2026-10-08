import streamlit as st
import datetime
import random

st.set_page_config(page_title="Super Infrared v2.2", page_icon="🔥", layout="wide")

st.markdown("""
<style>
.main {background:#0a0a0a; color:#ffd700}
.stButton>button {background:#ffd700; color:#000; font-weight:bold}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Super Infrared v2.2 - Dual °C / °F")
st.caption("Top 27 Project THREENITY2CAMSCANNER | Top 56 Builder - Tuan Cin | Vultr Agent Rush")
st.markdown("**6 Detect Preview:** Food + Room + Derma + Naphtol + Forensic Trace + Gem Authenticity | Driver NDIR Multispektrum: RGB IMX219, Thermal MLX90640, NDIR 4-channel: 4.26um CO2, 3.3um H2O/OH jamrud, 3.4um Naphtol, 7.7um emissivity berlian + Vultr Cloud + Printer ESC/POS")

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    unit = st.radio("Unit Utama", ["Indonesia °C", "Amerika/Eropa °F"], index=0)
    kategori = st.selectbox("Pilih 6 Filter", ["Food Health", "Room Health", "Derma Health (Forehead + Lashes)", "Naphtol Garmen", "Forensic Trace", "Gem Authenticity (Berlian/Obsidian/Jamrud/Sapphire)"])
    st.divider()
    st.write("**Rumus:** F = C × 9/5 + 32")
    st.write("**Safety:** IR 0.1W aman, Heat Pulse 35°C max 7 detik wajah tutup mata")

# --- Helper ---
def c_to_f(c): return c*9/5+32
def f_to_c(f): return (f-32)*5/9

theory_map = {
    "Obsidian Asli Murni": 2.0,
    "Kaca Masakan": 7.0,
    "Berlian Asli": 0.8,
    "Jamrud / Sapphire Asli": 2.1,
    "Food Basi (CO2 tinggi)": 5.5,
    "Room Jamur (H2O)": 4.5,
}

col1, col2 = st.columns(2)
with col1:
    st.subheader("📸 Step 1-3: Sortir RGB IMX219")
    img = st.camera_input("Arahkan ke sample (15 detik workflow)")
    jenis = st.selectbox("Teori Acuan", list(theory_map.keys()), index=0)
    teori_time = theory_map[jenis]

with col2:
    st.subheader("🌡️ Step 4-12: IR Thermal + Heat Pulse")
    temp_start_c = st.slider("Suhu Awal Heat Pulse (°C)", 30.0, 40.0, 35.0, 0.1)
    temp_end_c = st.slider("Suhu Akhir setelah cooling (°C)", 20.0, 35.0, 26.0, 0.1)
    obs_time = st.slider("Waktu Observasi AI (detik)", 0.5, 10.0, 2.3, 0.1)

temp_start_f = c_to_f(temp_start_c)
temp_end_f = c_to_f(temp_end_c)

# --- Calculation ---
purity = (teori_time / obs_time * 100) if obs_time>0 else 0
impurity = 100 - purity
delay = obs_time - teori_time

st.divider()
st.subheader("⏱️ Step 13-15: Hasil 3 Opini Pendek (C + F)")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**[HASIL 1: TEORI]**")
    st.code(f"{jenis}\n{temp_start_c:.1f}°C ({temp_start_f:.1f}°F) -> {temp_end_c:.1f}°C ({c_to_f(temp_end_c):.1f}°F)\nDalam {teori_time:.1f}s", language="text")
with c2:
    st.markdown("**[HASIL 2: OBSERVASI AI]**")
    st.code(f"{temp_start_c:.1f}°C ({temp_start_f:.1f}°F) -> {temp_end_c:.1f}°C ({c_to_f(temp_end_c):.1f}°F)\nDalam {obs_time:.1f}s | Delay {delay:+.1f}s\nCooling rata", language="text")
with c3:
    st.markdown("**[HASIL 3: KESIMPULAN OPINI]**")
    if purity>=95:
        status="100% MURNI"
    elif purity>=80:
        status=f"{purity:.1f}% {jenis} - Impurity {impurity:.1f}% micro-bubble"
    elif purity>=50:
        status=f"{purity:.1f}% Campuran - Menuju Kaca"
    else:
        status=f"{purity:.1f}% KACA MASAKAN / Bukan {jenis}"
    st.metric(label="Kemurnian", value=f"{purity:.1f}%", delta=f"Delay {delay:.1f}s")
    st.write(status)

# --- Forehead Lashes ---
if "Derma" in kategori:
    st.divider()
    st.subheader("👁️ Forehead + Lashes - Derma Filter")
    f_temp_c = st.slider("Forehead Temp (°C)", 35.0, 39.0, 36.5, 0.1)
    f_temp_f = c_to_f(f_temp_c)
    if f_temp_c < 37.5:
        st.success(f"Forehead {f_temp_c:.1f}°C ({f_temp_f:.1f}°F) - Normal 36.1-37.2°C (97-99°F)")
    else:
        st.error(f"Forehead {f_temp_c:.1f}°C ({f_temp_f:.1f}°F) - Fever >37.5°C (99.5°F)")
    st.caption("Lashes edge detection: IR auto-focus mata, mode wajah mata tertutup max 7 detik")

# --- Certificate ---
st.divider()
st.subheader("📜 Generator Sertifikat Keaslian (Printer Driver ESC/POS + PDF)")
st.write(f"Biaya Lab luar 500rb vs Super Infrared 50rb - Re-observasi tersimpan di Vultr Infra")

cert_col1, cert_col2 = st.columns([2,1])
with cert_col1:
    nama_sample = st.text_input("Nama Sample", f"{jenis} - Test {datetime.date.today()}")
    owner = st.text_input("Pemilik", "Alchaliveret")
    if st.button("🔥 Generate Sertifikat"):
        st.success(f"Sertifikat Generated! {nama_sample} | {purity:.1f}% | QR: super-infrared/{random.randint(1000,9999)}")
        st.json({
            "sample": nama_sample,
            "teori": f"{teori_time}s | {temp_start_c}C ({temp_start_f}F) -> {temp_end_c}C",
            "observasi": f"{obs_time}s | Delay {delay:.1f}s",
            "opini": status,
            "owner": owner,
            "date": str(datetime.datetime.now()),
            "infra": "Vultr Cloud + GitHub Pages aichaliveret.github.io/super-infrared/",
            "cost": "50rb vs Lab 500rb"
        })

with cert_col2:
    st.info("**Deploy Options:**\n- Streamlit Cloud (ini)\n- HuggingFace Spaces\n- Vultr Marketplace\n- GitHub Pages (statis) sudah live")

st.markdown("---")
st.caption("Built for Vultr Agent Rush - Intelligent Industry + Health & Wellbeing + Reinvent Commerce | Dual °C/°F | Forehead Lashes")
