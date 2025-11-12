"""Handles communication with Gemini (Google Generative AI) API."""
import os
try:
    from google import generativeai as genai
except Exception:
    genai = None
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_response(prompt: str) -> str:
    """Return a text response from Gemini. If package not installed or key missing,
    returns an informative message."""
    if not API_KEY:
        return "Gemini API key not configured. Please set GEMINI_API_KEY in your .env file."

    if genai is None:
        return ("google-generativeai package not installed in this environment. "
                "Install it with `pip install google-generativeai` to enable Gemini calls.")

    try:
        genai.configure(api_key=API_KEY)
        # Using a simple text generation example — adjust model and params as needed.
        response = genai.generate_text(model='gemini-1.0', prompt=prompt, temperature=0.2, max_output_tokens=512)
        # The exact response shape may differ; adjust if required by the SDK version.
        text = response.text if hasattr(response, 'text') else str(response)
        return text.strip()
    except Exception as e:
        return f"⚠️ Error when calling Gemini API: {str(e)}"
