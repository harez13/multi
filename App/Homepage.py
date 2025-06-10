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
        highlight = faktor.lower().startswith("all") or faktor.lower() == "kenapa"
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

    st.caption("Sumber: [AQMD Community in Action Guidebook](https://www.aqmd.gov/docs/default-source/aq-spec/star-grant/community-in-action-guidebook-on-air-quality-sensors-%28appendices-only%29.pdf)")


st.markdown("---")
st.subheader("Bagaimana polusi udara memengaruhi anak-anak?")

# Bagian atas: dampak terhadap anak-anak
col_a1, col_a2, col_a3 = st.columns(3)

with col_a1:
    st.markdown("### Masalah pernapasan")
    st.write("Meningkatnya kasus asma dan bronkitis")

with col_a2:
    st.markdown("### Penurunan fungsi paru-paru")
    st.write("Paparan jangka panjang dapat mengganggu perkembangan paru-paru")

with col_a3:
    st.markdown("### Perkembangan kognitif")
    st.write("Dampak potensial terhadap perkembangan otak dan prestasi akademik")

st.caption("Sumber: [EEA (European Environment Agency)](https://www.eea.europa.eu/en)")

# Bagian bawah: statistik global
st.markdown("###")
col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    st.markdown("### 99%")
    st.write("Populasi dunia tinggal di tempat-tempat yang kualitas udaranya melampaui batas pedoman tahunan WHO.")
    st.caption("Sumber: [World Health Organization](https://www.who.int)")

with col_b2:
    st.markdown("### 8,1 Juta")
    st.write("Kematian di seluruh dunia dapat disebabkan oleh polusi udara.")
    st.markdown("""
    - **4,7 juta**  
      Karena polusi udara partikulatif luar ruangan  
    - **3,1 juta**  
      Karena polusi udara dalam ruangan  
    - **0,5 juta**  
      Karena polusi ozon luar ruangan  
    """)
    st.caption("Sumber: [Health Effects Institute 2021 - Numbers for 2021](https://www.healtheffects.org/annual-report-2021)")

with col_b3:
    st.markdown("### 100/100,000")
    st.write("Orang-orang di seluruh dunia meninggal karena polusi udara.")
    st.markdown("""
    - **58/100,000**  
      Dari partikel luar ruangan  
    - **39/100,000**  
      Dari polusi udara dalam ruangan  
    - **6/100,000**  
      Dari polusi ozon luar ruangan  
    """)
    st.caption("Sumber: [IHME (Institute for Health Metrics and Evaluation) 2024](https://www.healthdata.org/)")

st.markdown("---")
st.markdown("#### Apa yang menyebabkan kualitas udara buruk?")
st.markdown(""" 
Polusi udara berasal dari sumber alami maupun buatan manusia.
Sumber alami mencakup debu, tanah, pasir yang terbawa angin, asap gunung berapi, dan material yang terbakar.
Sumber buatan manusia—seperti kendaraan bermotor, pembangkit listrik, pabrik, pembakaran bahan bakar, dan kegiatan pertanian—merupakan penyebab utama polusi udara di kota-kota dan lebih mudah dikendalikan melalui peraturan.

Kontribusi tiap sumber polusi berbeda-beda tergantung lokasi dan kebijakan setempat. Setiap wilayah memiliki campuran penyebab dan jenis polutannya sendiri, yang umumnya dikelompokkan sebagai berikut:
""")

st.markdown("##### Industri")
st.markdown(""" 
Industri mencakup polusi dari fasilitas seperti pabrik manufaktur, pertambangan, dan kilang minyak serta pembangkit listrik tenaga batu bara dan boiler untuk pembangkitan panas dan listrik.

Aktivitas industri merupakan sumber global utama nitrogen oksida (NOx), hidrogen sulfida, senyawa organik yang mudah menguap (VOC), dan materi partikulat, yang semuanya berkontribusi terhadap ozon dan kabut asap.
""")

st.markdown("#### Tingkat polusi udara yang tinggi dapat menyebabkan masalah kesehatan termasuk:")
st.markdown("""
- Efek jangka pendek: kesulitan bernapas, nyeri dada, mengi, batuk, ketidaknyamanan pernapasan umum, dan iritasi mata, hidung, dan tenggorokan.  
- Efek jangka panjang: kerusakan jaringan paru-paru, kanker, kematian dini, dan perkembangan penyakit pernapasan seperti asma, bronkitis, dan emfisema.
""")

st.markdown("#### Kelompok yang paling rentan terhadap dampak kesehatan buruk akibat polusi udara meliputi:")
st.markdown("""
- Penyakit jantung, seperti penyakit arteri koroner (CAD) atau gagal jantung kongestif  
- Penyakit paru-paru, seperti asma, emfisema, atau penyakit paru obstruktif kronik (PPOK)  
- Orang lanjut usia dan orang lanjut usia  
- Anak-anak di bawah usia 14 tahun  
- Wanita hamil  
- Pekerja luar ruangan  
- Atlet yang berolahraga di luar ruangan dengan giat
""")

st.markdown("#### Dampak kesehatan akibat polutan udara tertentu")

# Buat tabel 3 kolom seperti pada gambar
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    st.markdown("##### Ozon Tingkat Dasar")
    st.markdown("""
    - Penurunan fungsi paru-paru  
    - Asma yang memburuk  
    - Iritasi tenggorokan dan hidung  
    - Nyeri dada dan sesak napas  
    - Gejala mirip flu  
    - Kematian dini  
    - Kerentanan tinggi terhadap infeksi pernapasan  
    """)

with col2:
    st.markdown("##### Partikel Materi (PM) dan Asap Kebakaran Hutan")
    st.markdown("**Jangka pendek**")
    st.markdown("""
    - Detak jantung tidak teratur  
    - Nyeri dada  
    - Batuk  
    - Iritasi pada mata, hidung, dan tenggorokan  
    - Asma yang memburuk  
    - Penurunan fungsi paru-paru  
    """)

with col3:
    st.markdown("##### Partikel Materi (PM) dan Asap Kebakaran Hutan")
    st.markdown("**Jangka panjang**")
    st.markdown("""
    - Kerusakan jaringan paru-paru  
    - Kanker  
    - Perkembangan penyakit pernapasan seperti asma, bronkitis, dan emfisema  
    - Kematian dini  
    """)

st.caption("Sumber: IQAir (2024)")


