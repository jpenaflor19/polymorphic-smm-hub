import streamlit as st
import google.generativeai as genai
import urllib.parse

# --- CONFIG ---
st.set_page_config(page_title="BNDA's SMM Buddy", page_icon="🚀", layout="centered")

# --- BRANDING ---
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
    /* Hide Streamlit Branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, width=180)
    st.markdown("### **SMM Control Center**")
    api_key = st.text_input("Gemini API Key", type="password", placeholder="Enter key...")
    st.markdown("---")
    workspace = st.selectbox("Switch Workspace", [
        "💼 Client Attraction (BNDA Main)", 
        "⭐ Recruitment (Hiring)", 
        "🎙️ Delegation Desk Show",
        "💬 Smart Messaging",
        "🎨 Instant AI Image",
        "📈 Trend & Hashtag Hub"
    ])
    st.success("System: Online 🟢")

# --- MAIN INTERFACE ---
st.image(BANNER_URL, use_column_width=True)

if not api_key:
    st.title("Ready to scale today?")
    st.write("Connect your Gemini API Key in the sidebar to unlock your Brand-Specific SMM Engine.")
else:
    genai.configure(api_key=api_key)
    try:
        model = genai.GenerativeModel('gemini-3-flash-preview')
    except:
        model = genai.GenerativeModel('gemini-1.5-flash')

    # --- WORKSPACE: CLIENT ATTRACTION ---
    if workspace == "💼 Client Attraction (BNDA Main)":
        st.header("💼 Client Attraction")
        sub_cat = st.radio("Focus:", ["DA Highlight", "Delegation Benefits", "Marketing Hook"])
        topic = st.text_input("What's the specific topic?", placeholder="e.g. Saving time for CEOs")
        if st.button("Generate Sales Content"):
            with st.spinner("Writing..."):
                prompt = f"Act as a Bottleneck marketing expert. Write a viral post about {topic} focusing on {sub_cat}. Highlight how our Distant Assistants (DAs) help business owners scale. Use a professional yet punchy tone."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: RECRUITMENT ---
    elif workspace == "⭐ Recruitment (Hiring)":
        st.header("⭐ Recruitment Engine")
        role = st.text_input("What role are we hiring for?", placeholder="e.g. Executive Assistant")
        if st.button("Generate Hiring Post"):
            with st.spinner("Drafting..."):
                prompt = f"Write a high-energy recruitment post for a {role} at Bottleneck. Focus on our amazing culture, the 'Distant but not Distant' lifestyle, and career growth. Include emojis and a clear CTA to apply."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: DELEGATION DESK ---
    elif workspace == "🎙️ Delegation Desk Show":
        st.header("🎙️ The Delegation Desk Hub")
        show_topic = st.text_input("Episode Topic:", placeholder="e.g. Managing Remote Teams")
        if st.button("Generate Show Promo"):
            with st.spinner("Creating promo..."):
                prompt = f"Write a social media promotional post for our online show 'The Delegation Desk'. The topic is {show_topic}. Make it sound educational, authoritative, and exciting."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: SMART MESSAGING ---
    elif workspace == "💬 Smart Messaging":
        st.header("💬 Smart Message Refiner")
        msg = st.text_area("Paste the customer inquiry or comment here:", placeholder="Paste text...")
        if st.button("Generate Response"):
            with st.spinner("Thinking..."):
                prompt = f"Act as Bottleneck's lead Community Manager. Draft a polite, helpful, and professional reply to this message: '{msg}'. Ensure it aligns with our brand voice."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)

    # --- WORKSPACE: INSTANT AI IMAGE ---
    elif workspace == "🎨 Instant AI Image":
        st.header("🎨 Instant Graphic Generator")
        st.write("Generate images for your posts instantly for free.")
        img_desc = st.text_input("Describe the image you need:", placeholder="e.g. A professional looking at a laptop in a futuristic office")
        if st.button("Create Graphic"):
            with st.spinner("Generating masterpice..."):
                encoded_prompt = urllib.parse.quote(img_desc)
                image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true"
                st.image(image_url, caption=f"AI Visual for: {img_desc}")
                st.success("Image generated! Right-click to 'Save Image As'.")

    # --- WORKSPACE: TRENDS ---
    elif workspace == "📈 Trend & Hashtag Hub":
        st.header("📈 Strategy Hub")
        niche = st.text_input("Industry Niche:", placeholder="e.g. Remote Work, Executive Coaching")
        if st.button("Research Strategy"):
            with st.spinner("Analyzing..."):
                prompt = f"Provide a hashtag strategy for the {niche} industry. List 30 hashtags (Big, Medium, Niche) and 3 content pillars for the month."
                res = model.generate_content(prompt)
                st.markdown(f'<div class="result-card">{res.text}</div>', unsafe_allow_html=True)
