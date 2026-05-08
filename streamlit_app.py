import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Polymorphic SMM AI", page_icon="🚀", layout="centered")

# --- CUSTOM CSS FOR "WOW" FACTOR ---
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
    }
    .stButton>button {
        background: linear-gradient(90deg, #6200ea, #d500f9);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px #6200ea; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Polymorphic AI")
    st.subheader("SMM Control Center")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Paste key here...")
    st.markdown("---")
    category = st.selectbox("Switch Module", ["📱 Content Writer", "📈 Trend Researcher", "🤝 Community Manager"])
    st.caption("Version 2.0 | Powered by Gemini 3 Flash")

# --- LOGIC ---
if not api_key:
    st.info("👋 Welcome! Please enter your API Key in the sidebar to unlock the dashboard.")
else:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash')

    # --- MODULE 1: CONTENT WRITER ---
    if category == "📱 Content Writer":
        st.title("✨ Content Writer")
        st.write("Generate high-converting captions that stop the scroll.")
        
        col1, col2 = st.columns(2)
        with col1:
            topic = st.text_input("Topic / Hook", placeholder="e.g. Why you need an Executive Assistant")
        with col2:
            tone = st.selectbox("Brand Tone", ["Viral/Punchy", "Professional", "Storytelling", "Minimalist"])
        
        if st.button("Generate Captions"):
            with st.spinner("Brainstorming viral ideas..."):
                prompt = f"Act as a top 1% Social Media Manager. Create 3 {tone} captions for: {topic}. Include emojis, a strong hook, and a Call to Action."
                response = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
                st.button("Reset", on_click=lambda: st.rerun)

    # --- MODULE 2: TREND RESEARCHER ---
    elif category == "📈 Trend Researcher":
        st.title("📈 Trend & Hashtag Lab")
        niche = st.text_input("Enter Niche", placeholder="e.g. Luxury Real Estate")
        if st.button("Analyze Niche"):
            with st.spinner("Scanning trends..."):
                prompt = f"Provide a hashtag strategy for {niche}. List 10 'Big' hashtags, 10 'Medium', and 10 'Niche'. Also, suggest 2 trending audio vibes."
                response = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)

    # --- MODULE 3: COMMUNITY MANAGER ---
    elif category == "🤝 Community Manager":
        st.title("🤝 Smart Engagement")
        comment = st.text_area("Customer Comment", placeholder="Paste the comment you want to reply to...")
        if st.button("Draft Perfect Reply"):
            with st.spinner("Analyzing sentiment..."):
                prompt = f"Draft 2 professional but friendly replies to this comment: '{comment}'. One should be short, one should be detailed."
                response = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
