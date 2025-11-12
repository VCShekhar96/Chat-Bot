# 🤖 Chat-Bot (Gemini API)

**AI ChatBot** — a Flask-based web chatbot that uses **Gemini (Google Generative AI)** for natural language responses.
The project is ready for local development and deployment (Render / Railway / Heroku).

## Features
- Dark-themed, futuristic chat UI with typing animation
- Gemini API integration via `google-generativeai` SDK
- Simple modular design (`main.py`, `api_handler.py`)
- Ready for deployment with `Procfile` and `requirements.txt`

## Quickstart (Local)
1. Clone or extract the project.
2. Create a `.env` file from the included `.env.example` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python main.py
   ```
5. Open `http://localhost:5000` and click **Start Chatting**.

## Deployment
- Ensure `GEMINI_API_KEY` is set in your deployment environment variables.
- Render / Railway / Heroku will pick up the `Procfile` and `requirements.txt`.
- Recommended start command (if needed): `gunicorn main:app`

## Author
**V Chandrashekhar**  
[LinkedIn](https://www.linkedin.com/in/vchandrashekhar96)

## License
MIT License
