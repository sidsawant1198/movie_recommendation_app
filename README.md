# 🎬 Movie Recommendation App

An AI-powered movie recommendation web app built with **Streamlit** and **Google Gemini**. Enter any movie you love and get 5 tailored recommendations instantly.

🔗 **Live Demo:** [movierecommendationapp101.streamlit.app](https://movierecommendationapp101.streamlit.app/)

---

## Features

- 🤖 AI recommendations powered by Google Gemini (`gemini-2.5-flash-lite`)
- ⚡ Clean, responsive UI built with Streamlit
- 🔒 Secure API key handling via environment variables
- 🛡️ Graceful error handling for missing keys or API failures

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI framework |
| Google Generative AI | Gemini LLM for recommendations |
| python-dotenv | Local API key management |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sidsawant1198/movie_recommendation_app.git
cd movie_recommendation_app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
# Windows
source .venv/Scripts/activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the project root:

```
GOOGLE_GEMINI_API=your_api_key_here
```

Get a free API key at [aistudio.google.com](https://aistudio.google.com).

### 5. Run the app

```bash
streamlit run app.py
```

---

## Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New app**
3. Select your repo, branch `main`, and set main file to `app.py`
4. Under **Advanced settings → Secrets**, add:
   ```
   GOOGLE_GEMINI_API = "your_api_key_here"
   ```
5. Click **Deploy**

---

## Project Structure

```
movie_recommendation_app/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .env                # API key (local only, not committed)
├── .gitignore
└── README.md
```

---

## License

MIT
