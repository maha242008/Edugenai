from gemini_client import generate_text


def get_learning_recommendations(topic: str, level: str = "beginner") -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Create a personalized learning path for the following topic.

Topic:
{topic}

Student level:
{level}

Requirements:
- Start from the appropriate fundamentals.
- Progress from beginner concepts to more advanced concepts.
- Organize the learning path in a logical order.
- Mention what the student should learn at each stage.
- Suggest useful types of learning resources.
- Keep the explanation clear and student-friendly.
- Adapt the difficulty to the specified student level.
"""

    return generate_text(prompt)


# Alias used by some versions of the application
def create_learning_path(topic: str, level: str = "beginner") -> str:
    return get_learning_recommendations(topic, level)