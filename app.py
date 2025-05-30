import streamlit as st
from PIL import Image
from utils.ocr_utils import extract_text
from utils.lang_utils import detect_language
from utils.translate_utils import translate_to_english

st.set_page_config(page_title="Multilingual OCR & Translator", layout="centered")

st.title("🌐 Multilingual OCR + Language Detection + Translation")

uploaded_file = st.file_uploader("Upload an image with text", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text(image)

    st.subheader("📝 Extracted Text")
    st.write(extracted_text)

    with st.spinner("🌐 Detecting Language..."):
        lang_code = detect_language(extracted_text)

    st.subheader("🈶 Detected Language")
    st.write(lang_code)

    with st.spinner("🔄 Translating to English..."):
        translated = translate_to_english(extracted_text, source_lang=lang_code)

    st.subheader("🇬🇧 Translation in English")
    st.write(translated)
