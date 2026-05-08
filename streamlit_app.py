import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
st.set_page_config(page_title="BNDA's SMM Buddy", page_icon="🚀", layout="centered")

# --- YOUR GITHUB IMAGE LINKS ---
LOGO_URL = "https://github.com/jpenaflor19/polymorphic-smm-hub/blob/main/PNG%201.png?raw=true"
BANNER_URL = "https://github.com/jpenaflor19/polymorphic-smm-hub/blob/main/ME1.png?raw=true"

# --- CUSTOM CSS (GLASSMORPHISM & PREMIUM STYLING) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
    
    .stApp {{
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }}
    
    /* Result Card - Frosted Glass Effect */
    .result-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        color: #f0f0f0;
        line-height: 1.8;
    }}

    /* Glowing Action Button */
    .stButton>button {{
        background: linear-gradient(45deg, #00dbde, #fc00ff);
        border: none;
        color: white;
        font-weight: bold;
        border-radius: 15px;
        height: 3.5rem;
        width: 100%;
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 219, 222, 0.4);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, width=180)
    st.markdown("### **SMM Control Center**")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Enter key...")
    st.markdown("---")
    workspace = st.selectbox("Switch Workspace", [
        "📱 Viral Caption Writer", 
        "🎨 AI Graphic Designer", 
        "📈 Trend & Hashtag Hub", 
        "🤝 Smart Engagement"
    ])
    st.success("System: Fully Operational 🟢")

# --- MAIN INTERFACE ---
st.image(BANNER_URL, use_column_width=True)

if not api_key:
    st.title("Ready to scale, BNDA?")
    st.write("Your polymorphic AI assistant is waiting. Connect your Gemini API Key in the sidebar to unlock the full dashboard.")
else:
    genai.configure(api_key=api_key)
    # Using your specific Gemini 3 Flash Preview
    try:
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash')

    # --- WORKSPACE: CAPTIONS ---
    if workspace == "📱 Viral Caption Writer":
        st.header("✨ Viral Caption Writer")
        topic = st.text_input("Post Topic / Context", placeholder="e.g. Tips for scaling a business...")
        if st.button("Generate Content"):
            with st.spinner("AI is thinking..."):
                prompt = f"Act as a viral SMM expert. Create 3 engaging captions for: {topic}. Use hooks, emojis, and CTAs."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: GRAPHICS ---
    elif workspace == "🎨 AI Graphic Designer":
        st.header("🎨 AI Graphic Briefs")
        desc = st.text_input("What visual do you need?", placeholder="e.g. A futuristic office...")
        if st.button("Generate Visual Brief"):
            with st.spinner("Designing..."):
                prompt = f"Create a detailed AI image prompt for: {desc}. High-end cinematic style."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card"><b>Copy this to Midjourney/Canva:</b><br><br>{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: TRENDS ---
    elif workspace == "📈 Trend & Hashtag Hub":
        st.header("📈 Strategy Hub")
        niche = st.text_input("Niche / Industry")
        if st.button("Analyze Trends"):
            with st.spinner("Researching..."):
                prompt = f"Strategy for {niche}: 30 hashtags and 3 content ideas."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: ENGAGEMENT ---
    elif workspace == "🤝 Smart Engagement":
        st.header("🤝 Community Manager")
        comm = st.text_area("Paste Comment:")
        if st.button("Draft Reply"):
            with st.spinner("Thinking..."):
                res = model.generate_content(f"Draft a reply to: {comm}")
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)
