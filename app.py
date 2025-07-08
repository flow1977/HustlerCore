
import streamlit as st

LOGO_PATH = "logo.jpg"
GOLD = "#caa53b"

st.set_page_config(page_title="HustlerCore TestApp", layout="centered")

st.markdown(f"""
    <style>
        h1, h2, h3, h4 {{
            color: {GOLD};
            font-family: 'Arial Black', sans-serif;
        }}
        .reportview-container {{
            background-color: white;
        }}
        .stButton>button {{
            background-color: {GOLD};
            color: black;
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: bold;
        }}
    </style>
""", unsafe_allow_html=True)

st.image(LOGO_PATH, width=180)
st.markdown("## Dein Gegenschlag beginnt hier.")
st.markdown("**Diese Testversion zeigt, wie die KI später reagieren wird.**")

uploaded_file = st.file_uploader("📄 Behördenschreiben hochladen (PDF oder Bild)", type=["pdf", "jpg", "jpeg", "png"])
tone = st.radio("🗣️ Welche Tonlage soll der Antworttext haben?", ["Seicht", "Neutral", "Barsch"])

st.markdown("### 📃 Generierter Antworttext (Demo)")

if uploaded_file and tone:
    if tone == "Seicht":
        response = "Sehr geehrte Damen und Herren,\n\nich bitte freundlich um eine nochmalige Prüfung Ihres Schreibens..."
    elif tone == "Neutral":
        response = "Hiermit lege ich fristgerecht Widerspruch gegen den Bescheid vom 01.07.2025 ein..."
    else:
        response = "Diese Entscheidung entbehrt jeder Grundlage und widerspricht der gängigen Verwaltungspraxis..."

    st.text_area("Antwortvorschlag", value=response, height=200)
    st.download_button("⬇️ Antworttext als .txt speichern", data=response, file_name="antwort.txt")
else:
    st.info("Bitte Datei hochladen und Tonfall auswählen.")

st.markdown("---")
st.markdown("### 🔗 Folge HustlerBiz:")
st.markdown("""
- [📦 Zum Shop](https://hustlerbiz.de/)
- [📱 TikTok](https://www.tiktok.com/@hustlerbiz.de)
- [📸 Instagram](https://www.instagram.com/hustlerbizreal/)
- [📺 YouTube](https://www.youtube.com/@HustlerBizReal)
""")
