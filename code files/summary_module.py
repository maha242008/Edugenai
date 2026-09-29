from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Summarize the following text clearly and accurately.

Text:
{text}

Requirements:
- Keep the important points.
- Remove unnecessary repetition.
- Use simple student-friendly language.
- Use short paragraphs or bullet points when helpful.
- Do not add information that is not present in the original text.
"""

    return generate_text(prompt)