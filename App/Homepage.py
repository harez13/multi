import streamlit as st

st.set_page_config(layout="wide")

# Judul utama
st.title("Dampak kesehatan dan sumber polusi udara")

# Membuat dua kolom
col1, col2 = st.columns([1, 1])

# Kolom kiri - Faktor risiko kematian
with col1:
    st.subheader("Apa faktor risiko utama kematian di seluruh dunia?")
    st.markdown("Dari 62 juta orang yang meninggal setiap tahun (sampai tahun 2021), berdasarkan faktor risiko:")

    data_risiko = [
        ("1", "Tekanan darah tinggi", "10.9M"),
        ("2", "Polusi Udara (Luar Ruangan & Dalam Ruangan)", "8.1M"),
        ("3", "Merokok", "6.2M"),
        ("4", "Gula darah tinggi", "5.3M"),
        ("5", "Polusi partikel luar ruangan", "4.7M"),
        ("6", "Kegemukan", "4.7M"),
        ("7", "Kolesterol tinggi", "3.6M"),
        ("8", "Polusi udara dalam ruangan", "3.1M"),
        ("9", "Diet tinggi natrium", "1.9M"),
        ("10", "Konsumsi alkohol", "1.8M"),
        ("11", "Diet rendah buah", "1.7M"),
        ("12", "Diet rendah biji-bijian utuh", "1.5M"),
        ("13", "Berat badan lahir rendah", "1.5M"),
        ("14", "Asap rokok", "1.3M"),
    ]

    st.markdown("###")
    for i, faktor, jumlah in data_risiko:
        highlight = faktor.lower().startswith("polusi") or faktor.lower() == "asap rokok"
        st.markdown(f"<div style='padding:4px; background-color:{'#E6F0FA' if highlight else 'transparent'}'>"
                    f"<strong>{i}.</strong> {faktor} <span style='float:right'>{jumlah}</span></div>",
                    unsafe_allow_html=True)

    st.caption("Sumber: [IHME, Global Burden of Disease (2024)](https://www.healthdata.org/research-analysis/gbd)")

# Kolom kanan - Sumber Polusi PM2.5
with col2:
    st.subheader("Sumber Utama Polusi PM2.5")
    st.markdown("""
    Karena PM2.5, partikel debu halus dengan diameter hingga 2.5 mikrometer, dapat menembus jauh ke dalam paru-paru dan masuk ke aliran darah, 
    maka partikel ini menimbulkan risiko kesehatan yang signifikan. Sumbernya sangat bervariasi menurut lokasi, tetapi berikut ini adalah 
    sumber yang paling umum di seluruh dunia.
    """)

    sumber_pm25 = [
        ("🔥", "Pembakaran batu bara"),
        ("⛽", "Pembakaran bensin"),
        ("🚛", "Pembakaran diesel"),
        ("🪵", "Pembakaran kayu"),
        ("🏍️", "Pembakaran motor"),
        ("🏭", "Proses industri"),
        ("🔥", "Kebakaran"),
        ("🔁", "Konversi gas menjadi partikel"),
    ]

    cols = st.columns(2)
    for i, (ikon, nama) in enumerate(sumber_pm25):
        with cols[i % 2]:
            st.markdown(f"<div style='padding:12px; border:1px solid #ccc; border-radius:8px; margin-bottom:8px;'>"
                        f"<h3 style='margin:0'>{ikon}</h3><p style='margin:0'>{nama}</p></div>", unsafe_allow_html=True)

    st.caption("Sumber: AQMD Community in Action Guidebook")
