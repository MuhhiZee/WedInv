import streamlit as st
import base64
from pathlib import Path

# --- Tambahkan Fungsi Musik Latar Tersembunyi ---
def play_background_music(audio_path):
    try:
        with open(audio_path, "rb") as f:
            audio_bytes = f.read()
        
        # Konversi file audio ke format base64 agar bisa dibaca HTML inline
        audio_base64 = base64.b64encode(audio_bytes).decode()
        audio_html = f"""
            <audio autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("File music/wedding.mp3 tidak ditemukan.")

# Panggil fungsi ini di bagian kode mana saja (misalnya setelah cover)
play_background_music("music/wedding.mp3")
# ------------------------------------------------


st.set_page_config(
    page_title="Undangan Pernikahan",
    page_icon="💍",
    layout="wide"
)

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Ambil nama tamu dari URL
guest = st.query_params.get("to", "Tamu Undangan")

# Cover
# Cover Image
st.image("images/cover.jpg", use_container_width=True)

st.markdown(
    f"""
    <div style="text-align:center; margin-top:-80px; padding-bottom:30px;">
        <h3 style="color:white;">Kepada Yth.</h3>
        <h1 style="color:white;">{guest}</h1>
        <p style="color:white;">Mohon maaf apabila ada kesalahan penulisan nama.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(f"### Kepada Yth.\n## {guest}")

st.divider()

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
src="https://maps.google.com/maps?q=makassar&t=&z=15&ie=UTF8&iwloc=&output=embed"
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
