from deep_translator import GoogleTranslator

def translate_to_english(text, source_lang='auto'):
    try:
        translated = GoogleTranslator(source=source_lang, target='en').translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {e}"
