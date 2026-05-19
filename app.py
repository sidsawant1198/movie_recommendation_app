import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ── Config ──────────────────────────────────────────────────────────────────
load_dotenv()

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
    <style>
        .main { max-width: 700px; margin: auto; }
        h1 { text-align: center; font-size: 2.4rem; }
        .subtitle {
            text-align: center;
            color: #888;
            margin-top: -12px;
            margin-bottom: 28px;
            font-size: 1rem;
        }
        .rec-box {
            background: #1e1e2e;
            border-radius: 12px;
            padding: 20px 24px;
            margin-top: 20px;
            border: 1px solid #333;
        }
    </style>
""", unsafe_allow_html=True)

# ── API Key ──────────────────────────────────────────────────────────────────
api_key = os.getenv("GOOGLE_GEMINI_API")
if not api_key:
    st.error("⚠️ Gemini API key not found. Add `GOOGLE_GEMINI_API` to your `.env` file or Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# ── UI ───────────────────────────────────────────────────────────────────────
st.title("Movie Recommender")
st.markdown('<p class="subtitle">Powered by Google Gemini AI</p>', unsafe_allow_html=True)

with st.form("recommend_form"):
    movie_input = st.text_input(
        "Enter a movie you love:",
        placeholder="e.g. Inception, The Dark Knight, Parasite...",
    )
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        submit = st.form_submit_button("Recommend →", use_container_width=True)

# ── Logic ─────────────────────────────────────────────────────────────────────
if submit:
    if not movie_input.strip():
        st.warning("Please enter a movie name first.")
    else:
        prompt = f"""You are a movie expert. The user loves the movie "{movie_input}".
Recommend 5 similar movies they would enjoy. For each movie include:
- Title and year
- One sentence on why it's similar
- Genre tags

Format it as a clean, readable list. Do not use excessive markdown."""

        try:
            with st.spinner("Finding movies you'll love..."):
                response = model.generate_content(prompt)

            st.success(f'Here are recommendations based on **"{movie_input}"**:')
            st.markdown(
                f'<div class="rec-box">{response.text}</div>',
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.error(f"Something went wrong: {e}")
