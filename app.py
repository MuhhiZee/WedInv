import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Undangan Pernikahan",
    page_icon="💍",
    layout="wide"
)

# Load CSS
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# Ambil nama tamu dari URL
guest = st.query_params.get("to", "Tamu Undangan")

# --- PROSES KONVERSI AUDIO KE BASE64 ---
audio_file = "music/wedding.mp3"
audio_base64 = ""

try:
    with open(audio_file, "rb") as f:
        audio_bytes = f.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
except FileNotFoundError:
    st.error("⚠️ File 'music/wedding.mp3' tidak ditemukan. Pastikan folder dan nama file sudah benar.")

# --- INJEKSI HTML, AUDIO, DAN JAVASCRIPT BYPASS BROWSER ---
# Musik disembunyikan dan dikontrol langsung via klik tombol "Buka Undangan" menggunakan Javascript murni
if audio_base64:
    js_audio_player = f"""
    <audio id="wedding_music" loop>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>

    <div id="envelope-container" style="text-align: center; padding: 60px 20px; font-family: sans-serif; background: #fff; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); margin-bottom: 30px;">
        <h3 style="color: #666; font-weight: 300; letter-spacing: 2px;">The Wedding Of</h3>
        <h1 style="font-size: 3rem; color: #C79A5D; margin: 10px 0 30px 0;">Andi & Siti</h1>
        <p style="color: #888;">Kepada Yth. Bapak/Ibu/Saudara/i:</p>
        <h2 style="color: #333; margin-bottom: 40px;">{guest}</h2>
        <button id="open-btn" style="background-color: #C79A5D; color: white; border: none; padding: 15px 40px; font-size: 16px; font-weight: bold; border-radius: 25px; cursor: pointer; box-shadow: 0px 4px 15px rgba(199, 154, 93, 0.4); transition: 0.3s;">
            💌 Buka Undangan
        </button>
    </div>

    <script>
    const audio = document.getElementById('wedding_music');
    const btn = document.getElementById('open-btn');
    const container = document.getElementById('envelope-container');

    btn.addEventListener('click', function() {{
        // Putar audio secara instan melalui interaksi fisik (Lolos Blokir Browser)
        audio.play().catch(function(error) {{
            console.log("Audio play failed:", error);
        }});
        // Sembunyikan amplop setelah dibuka
        container.style.display = 'none';
    }});
    </script>
    """
    st.components.v1.html(js_audio_player, height=380)

st.divider()

# --- ISI UTAMA UNDANGAN ---
# Tampilan isi konten di bawah ini akan otomatis terlihat sejak awal, 
# namun musik akan langsung aktif begitu tombol di atas diklik.

# Mempelai
col1, col2 = st.columns(2)

with col1:
    st.image("images/groom.jpg", width=250)
    st.subheader("Andi Pratama")
    st.write("Putra Pertama dari")
    st.write("Bapak Ahmad & Ibu Nur")

with col2:
    st.image("images/bride.jpg", width=250)
    st.subheader("Siti Rahma")
    st.write("Putri Pertama dari")
    st.write("Bapak Yusuf & Ibu Aminah")

st.divider()

# Jadwal
st.header("📅 Akad Nikah")

st.info("""
Hari : Minggu

Tanggal : 20 Desember 2026

Pukul : 09.00 WIB

Lokasi :
Gedung Serbaguna Makassar
""")

st.header("🎉 Resepsi")

st.success("""
Hari : Minggu

Tanggal : 20 Desember 2026

Pukul : 11.00 WIB

Lokasi :
Gedung Serbaguna Makassar
""")

st.divider()

# Countdown (Placeholder)
st.header("⏳ Countdown")
st.markdown(
"""
<h2 style='text-align:center;color:#C79A5D;'>
20 Desember 2026
</h2>
""",
unsafe_allow_html=True
)

st.divider()

# Galeri
st.header("📸 Galeri")

cols = st.columns(3)

gallery = [
    "images/gallery1.jpg",
    "images/gallery1.jpg",
    "images/gallery1.jpg"
]

for col, img in zip(cols, gallery):
    with col:
        st.image(img)

st.divider()

# Google Maps
st.header("📍 Lokasi")

st.components.v1.html("""
<iframe
src="https://google.com"
width="100%"
height="400"
style="border:0;"
loading="lazy">
</iframe>
""", height=420)

st.divider()

# RSVP
st.header("💌 RSVP")

nama = st.text_input("Nama")

kehadiran = st.selectbox(
    "Konfirmasi Kehadiran",
    [
        "Hadir",
        "Tidak Hadir",
        "Masih Ragu"
    ]
)

pesan = st.text_area("Ucapan")

if st.button("Kirim"):
    st.success("Terima kasih atas konfirmasinya!")

st.divider()

# Gift
st.header("🎁 Wedding Gift")

st.code("""
BCA
1234567890

a.n Andi Pratama
""")

st.caption("Terima kasih atas doa dan restunya ❤️")
