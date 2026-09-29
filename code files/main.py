from pathlib import Path
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import settings
from models import (
    AIResponse,
    LearningPathRequest,
    QuestionRequest,
    QuizRequest,
    QuizResponse,
    TextRequest,
)

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "EduGenie - Google Gemini Powered Learning Assistant"
    ),
)


app.mount(
    "/static",
    StaticFiles(
        directory=BASE_DIR / "static"
    ),
    name="static",
)


templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


@app.get(
    "/",
    response_class=HTMLResponse,
)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "app_name": settings.APP_NAME,
        },
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "gemini_configured": bool(
            settings.GEMINI_API_KEY
        ),
        "local_explainer_enabled": (
            settings.LOCAL_EXPLAINER_ENABLED
        ),
    }


@app.post(
    "/qa",
    response_model=AIResponse,
)
async def qa(request: QuestionRequest):

    try:
        result = answer_question(
            request.question
        )

        return AIResponse(
            result=result
        )

    except Exception as exc:
        return AIResponse(
            result=f"Error: {str(exc)}"
        )


@app.post(
    "/explain",
    response_model=AIResponse,
)
async def explain(request: TextRequest):

    try:
        result = explain_topic(
            request.text
        )

        return AIResponse(
            result=result
        )

    except Exception as exc:
        return AIResponse(
            result=f"Error: {str(exc)}"
        )


@app.post(
    "/quiz",
    response_model=QuizResponse,
)
async def quiz(request: QuizRequest):

    try:
        result = generate_quiz(
            request.text
        )

        return result

    except Exception as exc:
        # Convert errors into a valid response shape
        # so the frontend can display them.
        return {
            "title": "Quiz Error",
            "questions": [
                {
                    "question": str(exc),
                    "options": [
                        "Please try again",
                        "Check your API key",
                        "Check the input",
                        "Check the server logs",
                    ],
                    "answer": "Please try again",
                    "explanation": (
                        "The quiz could not be generated."
                    ),
                }
            ],
        }


@app.post(
    "/summarize",
    response_model=AIResponse,
)
async def summarize(request: TextRequest):

    try:
        result = summarize_text(
            request.text
        )

        return AIResponse(
            result=result
        )

    except Exception as exc:
        return AIResponse(
            result=f"Error: {str(exc)}"
        )


@app.post(
    "/learn/recommendations",
    response_model=AIResponse,
)
async def learning_recommendations(
    request: LearningPathRequest,
):

    try:
        result = get_learning_recommendations(
            request.topic,
            request.level,
        )

        return AIResponse(
            result=result
        )

    except Exception as exc:
        return AIResponse(
            result=f"Error: {str(exc)}"
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )