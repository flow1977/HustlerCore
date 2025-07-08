
import streamlit as st

# Branding-Konstanten
LOGO_PATH = "logo.jpg"
GOLD = "#caa53b"
BLACK = "#000000"

st.set_page_config(page_title="HustlerCore – Deine Schutzburg", layout="centered")

st.markdown(f"""
    <style>
        body {{
            background-color: white;
            font-family: 'Arial', sans-serif;
        }}
        h1, h2, h3 {{
            color: {GOLD};
            font-weight: 700;
        }}
        .stButton>button {{
            background-color: {GOLD};
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

st.image(LOGO_PATH, width=160)
st.markdown("### HustlerCore – Deine Schutzburg gegen Behördenwillkür")
st.markdown("**Diese Demo zeigt, wie deine Plattform funktionieren wird – selbstbewusst, klar, rechtssicher.**")

uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen", type=["pdf", "jpg", "jpeg", "png"])
tone = st.radio("🗣️ Tonalität der Antwort:", ["Seicht", "Neutral", "Barsch"])

st.markdown("#### 📄 Vorschau deines Antworttextes")

if uploaded_file and tone:
    if tone == "Seicht":
        response = "Sehr geehrte Damen und Herren,\n\nich bitte freundlich um nochmalige Prüfung Ihres Schreibens..."
    elif tone == "Neutral":
        response = "Hiermit lege ich fristgerecht Widerspruch gegen den Bescheid vom 01.07.2025 ein..."
    else:
        response = "Diese Entscheidung widerspricht der gängigen Rechtspraxis und ist inakzeptabel..."

    st.text_area("Antworttext", value=response, height=200)
    st.download_button("⬇️ Als .txt speichern", data=response, file_name="antwort.txt")
else:
    st.info("Bitte Datei hochladen und Tonalität wählen.")

st.markdown("---")
st.markdown("### 🔗 Folge HustlerBiz:")
st.markdown("""
- [🛒 Zum Shop](https://hustlerbiz.de/)
- [📱 TikTok](https://www.tiktok.com/@hustlerbiz.de)
- [📸 Instagram](https://www.instagram.com/hustlerbizreal/)
- [📺 YouTube](https://www.youtube.com/@HustlerBizReal)
""")
