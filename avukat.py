import streamlit as st
import pandas as pd
from datetime import datetime

# --- PROFESYONEL SAYFA YAPISI ---
st.set_page_config(page_title="JurisAI | Hukuki Karar Destek", page_icon="⚖️", layout="wide")

# --- GÖRSEL TASARIM ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .report-card { padding: 25px; border-radius: 15px; background-color: white; border-left: 5px solid #1f77b4; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .dilekce-kutu { padding: 40px; border: 1px solid #dcdcdc; background-color: #ffffff; font-family: 'Times New Roman', serif; line-height: 1.8; color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# --- YAN PANEL ---
with st.sidebar:
    st.title("⚖️ JurisAI v2.0")
    st.info("Lisans Sahibi: **Av. Merve Doğan**")
    menu = st.radio("İşlem Seçiniz", ["📊 Dava Analiz Merkezi", "📝 Akıllı Dilekçe Yazıcı"])
    st.markdown("---")
    st.write("© 2026 Hukuk Teknolojileri")

# --- MODÜL 1: ANALİZ ---
if menu == "📊 Dava Analiz Merkezi":
    st.title("📊 Stratejik Dava Analizi")
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        st.subheader("Dava Parametreleri")
        dava_tipi = st.selectbox("Hukuk Alanı", ["İş Hukuku", "Ticaret Hukuku", "Tazminat Hukuku", "Aile Hukuku"])
        kanit_skoru = st.slider("Kanıt ve Delil Gücü (%)", 0, 100, 75)
        st.text_area("Vaka Özeti", placeholder="Davanın temel dayanağını buraya yazın...")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with c2:
        # Profesyonel Radar Grafiği
        risk_data = pd.DataFrame(dict(
            r=[kanit_skoru, 85, 60, 90, 70],
            theta=['Kanıt Gücü', 'İçtihat Uyumu', 'Zaman Aşımı', 'Başarı Şansı', 'Süreç Hızı']))
        fig = px.line_polar(risk_data, r='r', theta='theta', line_close=True, title="Stratejik Başarı Haritası")
        fig.update_traces(fill='toself', line_color='#1f77b4')
        st.plotly_chart(fig, use_container_width=True)

# --- MODÜL 2: DİLEKÇE YAZICI ---
elif menu == "📝 Akıllı Dilekçe Yazıcı":
    st.title("📝 Otomatik Dilekçe Hazırlama")
    
    with st.container():
        st.markdown('<div class="report-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        muvekkil = c1.text_input("Müvekkil (Davacı) Ad Soyad")
        karsi_taraf = c2.text_input("Davalı Ad Soyad")
        mahkeme = st.text_input("Yetkili Mahkeme", value="İSTANBUL NÖBETÇİ ASLİYE HUKUK MAHKEMESİ")
        olay_detay = st.text_area("Olayın Özeti ve Talepleriniz", height=150)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("HUKUKİ TASLAĞI OLUŞTUR"):
        st.markdown("---")
        tarih = datetime.now().strftime('%d/%m/%Y')
        
        dilekce_icerik = f"""
        {mahkeme} SAYIN HAKİMLİĞİ'NE
        
        DAVACI: {muvekkil}
        VEKİLİ: Av. Merve Doğan
        DAVALI: {karsi_taraf}
        
        KONU: Haklı taleplerimizin iletilmesi ve davanın kabulü istemidir.
        TARİH: {tarih}
        
        AÇIKLAMALAR:
        1- Müvekkil ile davalı taraf arasındaki uyuşmazlık kapsamında; {olay_detay} hususları sübut bulmuştur.
        2- Yerleşik Yargıtay içtihatları ve ilgili yasal mevzuat uyarınca müvekkilin mağduriyetinin giderilmesi yasal bir zorunluluktur.
        
        HUKUKİ DELİLLER: Tanık, Bilirkişi, Yargıtay Kararları ve her türlü yasal delil.
        SONUÇ VE İSTEM: Fazlaya ilişkin haklarımız saklı kalmak kaydıyla; davanın kabulüne, yargılama giderleri ve vekalet ücretinin davalıya yükletilmesine karar verilmesini vekaleten arz ve talep ederiz.
        
        Davacı Vekili
        Av. Merve Doğan
        """
        st.markdown(f'<div class="dilekce-kutu">{dilekce_icerik.replace("\n", "<br>")}</div>', unsafe_allow_html=True)

        st.download_button("📥 Taslağı İndir (.txt)", dilekce_icerik, file_name=f"dilekce_{muvekkil}.txt")

