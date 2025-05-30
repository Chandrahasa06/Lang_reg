import easyocr
from PIL import Image
import numpy as np

# Readers grouped by compatible scripts
latin_reader = easyocr.Reader(['en', 'fr', 'es'], gpu=False)  # Latin script
devanagari_reader = easyocr.Reader(['en', 'hi', 'mr', 'ne'], gpu=False)  # Devanagari
arabic_reader = easyocr.Reader(['en', 'ar', 'fa', 'ur', 'ug'], gpu=False)  # Arabic

def extract_text(image, script='latin'):
    img_array = np.array(image)

    # Choose reader based on script
    if script == 'devanagari':
        reader = devanagari_reader
    elif script == 'arabic':
        reader = arabic_reader
    else:
        reader = latin_reader

    results = reader.readtext(img_array)
    extracted = ' '.join([text for (_, text, _) in results])
    return extracted
