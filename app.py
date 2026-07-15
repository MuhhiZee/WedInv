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


# --- SISTEM LOCK UNDANGAN (SESSION STATE) ---
if "terbuka" not in st.session_state:
    st.session_state.terbuka = False

# FUNGSI UNTUK MEMBUKA UNDANGAN
def buka_undangan():
    st.session_state.terbuka = True


# ====================================================================
# TAMPILAN 1: JIKA UNDANGAN BELUM DIBUKA (SAMPUL AWAL BENAR-BENAR TERKUNCI)
# ====================================================================
if not st.session_state.terbuka:
    st.markdown(
        """
        <div class='cover' style='text-align: center; padding: 100px 20px; font-family: sans-serif;'>
            <h3 style='color: #666; font-weight: 300; letter-spacing: 2px;'>The Wedding Of</h3>
            <h1 style='font-size: 3.5rem; color: #C79A5D; margin: 15px 0;'>Andi & Siti</h1>
            <p style='margin-top: 40px; color: #888; font-size: 1.1rem;'>Kepada Yth. Bapak/Ibu/Saudara/i:</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<h2 style='text-align:center; color: #333;'>{guest}</h2>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Tombol asli Streamlit untuk mengubah state halaman dan memicu interaksi audio browser
    st.button("💌 Buka Undangan", on_click=buka_undangan, use_container_width=True)


# ====================================================================
# TAMPILAN 2: JIKA UNDANGAN SUDAH DIBUKA (KONTEN UTAMA BARU MUNCUL DI SINI)
# ====================================================================
else:
    # --- PROSES MEMUTAR AUDIO OTOMATIS SETELAH DIKLIK ---
    audio_file = "musik/wedding.mp3"
    try:
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        
        # Eksekusi pemutar audio Streamlit dengan Autoplay aktif (Lolos blokir karena dipicu st.button)
        st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)
        st.caption("🎵 Musik sedang diputar otomatis...")
    except FileNotFoundError:
        st.error("⚠️ File 'musik/wedding.mp3' tidak ditemukan. Pastikan folder dan nama file sudah benar.")

    # --- KONTEN UTAMA UNDANGAN ---
    st.markdown(
        """
        <div class='cover'>
            <h3>The Wedding Of</h3>
            <h1>Andi & Siti</h1>
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
