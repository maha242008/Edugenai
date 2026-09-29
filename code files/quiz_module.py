import json

from gemini_client import generate_text
from models import QuizResponse


def generate_quiz(topic: str) -> QuizResponse:
    prompt = f"""
Create a short educational quiz about:

{topic}

Return ONLY valid JSON in this exact structure:

{{
  "questions": [
    {{
      "question": "Question text",
      "options": [
        "Option 1",
        "Option 2",
        "Option 3",
        "Option 4"
      ],
      "answer": "Option 1",
      "explanation": "Explanation"
    }}
  ]
}}

Rules:
- Create exactly 3 questions.
- Each question must have exactly 4 options.
- There must be exactly one correct answer.
- The "answer" must exactly match one of the options.
- Keep the questions educational and suitable for students.
"""

    raw = generate_text(prompt).strip()

    # Remove markdown code fences if Gemini adds them
    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    data = json.loads(raw)

    return QuizResponse(**data)