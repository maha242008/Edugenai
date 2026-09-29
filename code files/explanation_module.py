from gemini_client import generate_text


def explain_topic(topic: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following topic in a simple and student-friendly way.

Topic:
{topic}

Requirements:
- Start with a simple definition.
- Explain the main idea clearly.
- Use a simple real-world example.
- Break difficult concepts into smaller points.
- Avoid unnecessary technical jargon.
"""

    return generate_text(prompt)