import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
st.set_page_config(page_title="SMM Studio Pro", page_icon="🚀", layout="centered")

# --- YOUR BRANDING LINKS ---
LOGO_URL = "https://i.postimg.cc/HW7zD6Zg/PNG-1.png"
BANNER_URL = "https://i.postimg.cc/rpmGhjRd/ME1.png"

# --- CUSTOM CSS (DARK SAAS THEME) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    .stApp {{ background-color: #0E1117; color: #FFFFFF; }}
    
    /* Result Card Styling */
    .result-card {{
        background-color: #161B22;
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #30363D;
        margin-top: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        color: #E6EDF3;
        line-height: 1.7;
    }}
    
    /* Glowing Button */
    .stButton>button {{
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        color: white;
        border: none;
        padding: 15px;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, width=150)
    st.title("BNDA's SMM Buddy")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Enter key to unlock...")
    st.markdown("---")
    category = st.selectbox("Switch Workspace", [
        "📱 Viral Caption Writer", 
        "🎨 AI Graphic Designer", 
        "📈 Trend & Hashtag Hub", 
        "🤝 Smart Engagement"
    ])
    st.success("System: Online 🟢")

# --- MAIN INTERFACE ---
st.image(BANNER_URL, use_column_width=True)

if not api_key:
    st.title("Welcome to the Future of SMM")
    st.write("Your polymorphic AI assistant is ready. Please enter your API Key in the sidebar to start building.")
else:
    genai.configure(api_key=api_key)
    try:
        # Using the Gemini 3 Flash Preview as seen in your Studio
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash')

    # --- WORKSPACE: CAPTIONS ---
    if category == "📱 Viral Caption Writer":
        st.header("✨ Viral Caption Writer")
        topic = st.text_input("Post Topic / Context", placeholder="e.g. Benefits of hiring a Virtual Assistant")
        if st.button("Generate Content"):
            with st.spinner("Processing with Gemini 3..."):
                prompt = f"Act as a viral SMM expert. Create 3 engaging captions for: {topic}. Include hooks, emojis, and CTAs."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)
                st.button("Copy Text (Manual Select)", help="Highlight text above to copy")

    # --- WORKSPACE: GRAPHICS ---
    elif category == "🎨 AI Graphic Designer":
        st.header("🎨 AI Graphic Briefs")
        desc = st.text_input("What visual do you need?", placeholder="e.g. A futuristic office with a robot assistant")
        if st.button("Generate Visual Brief"):
            with st.spinner("Designing prompt..."):
                prompt = f"Create a professional DALL-E/Midjourney prompt for: {desc}. Make it cinematic and high-end."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: TRENDS ---
    elif category == "📈 Trend & Hashtag Hub":
        st.header("📈 Strategy Hub")
        niche = st.text_input("Niche / Industry", placeholder="e.g. SaaS, E-commerce, Real Estate")
        if st.button("Research Trends"):
            with st.spinner("Analyzing niche..."):
                prompt = f"Give me 30 categorized hashtags and 3 content pillars for the {niche} niche."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: COMMUNITY ---
    elif category == "🤝 Smart Engagement":
        st.header("🤝 Community Manager")
        comm = st.text_area("Customer Comment", placeholder="Paste comment here...")
        if st.button("Draft Reply"):
            with st.spinner("Thinking..."):
                prompt = f"Draft a polite and helpful reply to this: {comm}"
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)
