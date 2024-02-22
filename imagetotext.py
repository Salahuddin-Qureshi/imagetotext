#first install these two libraries in your system
pip install pytesseract
pip install Pillow


import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  

def extract_text_from_image(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.pytesseract.image_to_string(image)

    return text

# Example usage:
image_path = "image_path"
result_text = extract_text_from_image(image_path)

print("Text extracted from the image:")
print(result_text)
