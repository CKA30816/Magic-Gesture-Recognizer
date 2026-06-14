import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "keras_model.h5"
LABELS_PATH = BASE_DIR / "models" / "labels.txt"

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
HF_API_KEY = os.getenv("HF_API_KEY", "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")
GROQ_TEXT_MODEL = os.getenv("GROQ_TEXT_MODEL", "llama-3.1-8b-instant")
HF_IMAGE_MODEL = os.getenv("HF_IMAGE_MODEL", "black-forest-labs/FLUX.1-schnell")
HF_PROVIDER = os.getenv("HF_PROVIDER", "auto")

APP_TITLE = "Gesture-Triggered AI Magic"
APP_ICON = "🪄"
MAX_SPELL_LOG = 8
CAMERA_HELP = "Show one clear hand sign, then click Take Photo."
