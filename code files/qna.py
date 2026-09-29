from gemini_client import generate_text
from prompts import qna_prompt


def answer_question(question: str) -> str:
    prompt = qna_prompt(question)
    return generate_text(prompt)