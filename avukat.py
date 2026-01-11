import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="JurisAI | Hukuki Karar Destek", page_icon="⚖️", layout="wide")

# --- GÖRSEL TASARIM ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .report-card { padding: 25px; border-radius: 15px; background-color: white; border-left: 5px solid #1f77b4; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- YAN PANEL ---
with st.sidebar:
    st.title("⚖️ JurisAI v2.0")
    st.info("**Lisans Sahibi: Av. Merve Doğan**")
    menu = st.sidebar.radio("İşlem Seçiniz:", ["📊 Dava Analiz Merkezi", "📝 Akıllı Dilekçe Yazıcı"])
    st.markdown("---")
    st.write("© 2026 Hukuk Teknolojileri")

# --- MODÜL 1: ANALİZ ---
if menu == "📊 Dava Analiz Merkezi":
    st.title("📊 Stratejik Dava Analizi")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        hukuk_alani = st.selectbox("Hukuk Alanı", ["İş Hukuku", "Aile Hukuku", "Ceza Hukuku", "Ticaret Hukuku"])
        kanit_gucu = st.slider("Kanıt ve Delil Gücü (%)", 0, 100, 75)
        vaka_ozeti = st.text_area("Vaka Özeti", placeholder="Davanın temel dayanağını yazın...")
        
    with col2:
        # Hata veren kısım burasıydı, şimdi px ile tertemiz düzelttik
        risk_data = pd.DataFrame(dict(
            r=[kanit_gucu, 80, 70, 85, 90],
            theta=['Kanıt Gücü', 'Yargıtay Uyumu', 'Süreç Hızı', 'Kazanma İhtimali', 'Maliyet Verimi']
        ))
        fig = px.line_polar(risk_data, r='r', theta='theta', line_close=True, title="Stratejik Başarı Haritası")
        st.plotly_chart(fig, use_container_width=True)

# --- MODÜL 2: DİLEKÇE ---
else:
    st.title("📝 Akıllı Dilekçe Yazıcı")
    st.warning("Bu bir yapay zeka taslağıdır, avukat kontrolü gereklidir.")
    
    d_tipi = st.selectbox("Dilekçe Türü", ["İhtarname", "Dava Dilekçesi", "Cevap Dilekçesi"])
    taraf_ad = st.text_input("Müvekkil Ad Soyad")
    
    if st.button("Taslağı Oluştur"):
        st.markdown(f"""
        <div class='report-card'>
            <h3>{d_tipi.upper()} TASLAĞI</h3>
            <p><b>Tarih:</b> {datetime.now().strftime('%d/%m/%Y')}</p>
            <p><b>Sayın Hakimlik Makamına / Muhataba,</b></p>
            <p>{taraf_ad} vekili olarak aşağıda belirtilen hususların arzını talep ederiz...</p>
            <hr>
            <p align='right'><b>Av. Merve Doğan</b></p>
        </div>
        """, unsafe_allow_html=True)
