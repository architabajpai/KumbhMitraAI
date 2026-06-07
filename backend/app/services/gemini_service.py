import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-3.5-flash"
)

SYSTEM_PROMPT = """
You are KumbhMitra.

You help pilgrims visiting Mahakumbh.

Features:
- Multilingual support
- Navigation guidance
- Event information
- Emergency assistance
- Accommodation support

Always respond in the same language as the user.
Dont use any emojis.
Maintain proper indentation and everything
Use bold where needed
"""

def ask_gemini(message, language):
    try:

        language_instruction = (
            "Respond only in Hindi."
            if language == "hi"
            else "Respond only in English."
        )

        prompt = f"""
    {SYSTEM_PROMPT}

    {language_instruction}

    User:
    {message}
    """

        response = model.generate_content(
            prompt
        )

        return response.text
    except Exception as e:
        print(e)

        return (
            "The AI service is temporarily unavailable due to API quota limits. "
            "Please try again shortly."
        )