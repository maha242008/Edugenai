import os

from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()


class Settings(BaseModel):
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "EduGenie - AI Learning Assistant"
    )

    APP_VERSION: str = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    GEMINI_API_KEY: str = os.getenv(
        "GEMINI_API_KEY",
        ""
    )

    GEMINI_MODEL: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    )

    LOCAL_EXPLAINER_ENABLED: bool = os.getenv(
        "LOCAL_EXPLAINER_ENABLED",
        "false"
    ).lower() == "true"

    LOCAL_EXPLAINER_MODEL: str = os.getenv(
        "LOCAL_EXPLAINER_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    MAX_INPUT_LENGTH: int = int(
        os.getenv("MAX_INPUT_LENGTH", "12000")
    )


settings = Settings()