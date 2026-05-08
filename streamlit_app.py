import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Polymorphic AI", layout="wide")

# --- UI STYLE ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3em; 
        background-color: #6200ea; 
        color: white; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🚀 SMM Hub")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    category = st.radio("Select Tool", ["✨ Magic Captions", "#️⃣ Hashtag Lab", "💬 Smart Reply"])
    st.info("Powered by Gemini 1.5 Flash")

# --- MAIN LOGIC ---
if not api_key:
    st.warning("Please enter your API Key in the sidebar to begin.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash')

    if category == "✨ Magic Captions":
        st.header("Magic Captions")
        topic = st.text_input("What is your post about?")
        if st.button("Generate"):
            with st.spinner("Writing..."):
                response = model.generate_content(f"Act as a viral SMM. Write 3 captions for: {topic}")
                st.success("Done!")
                st.write(response.text)

    elif category == "#️⃣ Hashtag Lab":
        st.header("Hashtag Lab")
        niche = st.text_input("Your niche (e.g. Vegan Bakery)")
        if st.button("Get Hashtags"):
            response = model.generate_content(f"Generate 30 hashtags for {niche} split by Low/Medium/High reach.")
            st.code(response.text)

    elif category == "💬 Smart Reply":
        st.header("Smart Reply")
        comment = st.text_area("Paste the comment:")
        if st.button("Draft Reply"):
            response = model.generate_content(f"Draft a polite, engaging reply to: {comment}")
            st.info(response.text)
