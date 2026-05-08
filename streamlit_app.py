import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Polymorphic SMM AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    .result-card {
        background-color: #161B22;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        color: #E6EDF3;
        line-height: 1.6;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (LOGO & SETTINGS) ---
with st.sidebar:
    # REPLACING THIS URL CHANGES YOUR LOGO
    st.image("https://i.postimg.cc/HW7zD6Zg/PNG-1.png", width=100) 
    st.title("SMM Studio Pro")
    api_key = st.text_input("Gemini API Key", type="password")
    st.markdown("---")
    category = st.selectbox("Tools", ["📱 Content Writer", "🎨 Image Prompt Gen", "📈 Trend Lab", "🤝 Community"])
    st.info("Status: Fully Operational 🟢")

# --- HEADER IMAGE ---
# This adds a professional banner at the top
st.image("https://i.postimg.cc/rpmGhjRd/ME1.png", use_column_width=True)

# --- LOGIC ---
if not api_key:
    st.title("Welcome to the Future of SMM")
    st.write("Connect your Gemini API Key in the sidebar to begin generating viral content.")
else:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash')

    if category == "📱 Content Writer":
        st.header("✨ Viral Caption Generator")
        topic = st.text_input("What's the post about?")
        if st.button("Generate Magic"):
            with st.spinner("Writing..."):
                res = model.generate_content(f"Write a viral social media caption for: {topic}. Include a hook and CTA.")
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    elif category == "🎨 Image Prompt Gen":
        st.header("🎨 AI Graphic Briefs")
        st.write("Describe your vision, and I'll write the prompt for your image generator.")
        desc = st.text_input("Describe the image idea:")
        if st.button("Create Prompt"):
            with st.spinner("Designing..."):
                res = model.generate_content(f"Write a highly detailed, professional AI image generation prompt for: {desc}. Style: Cinematic, High-Res.")
                st.markdown(f'<div class="result-card"><b>Copy this into Midjourney/Canva:</b><br><br>{res.text}</div>', unsafe_allow_html=True)

    elif category == "📈 Trend Lab":
        st.header("📈 Strategy & Hashtags")
        niche = st.text_input("Niche:")
        if st.button("Research"):
            res = model.generate_content(f"Strategy for {niche}")
            st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    elif category == "🤝 Community":
        st.header("🤝 Rapid Response")
        comm = st.text_area("Comment:")
        if st.button("Draft Reply"):
            res = model.generate_content(f"Draft a reply to: {comm}")
            st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)
