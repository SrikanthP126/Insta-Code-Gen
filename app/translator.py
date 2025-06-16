from googletrans import Translator
from langdetect import detect

translator = Translator()

def detect_language(text: str) -> str:
    return detect(text)

def translate_to_english(text: str) -> str:
    return translator.translate(text, dest='en').text

def translate_from_english(text: str, target_lang: str) -> str:
    return translator.translate(text, dest=target_lang).text
