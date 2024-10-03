# import cv2
# import pytesseract
# from PIL import Image

# # If you have Tesseract installed in a non-default location, specify the path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def extract_text_from_image(image_path):
#     # Load the image using OpenCV
#     image = cv2.imread(image_path)

#     # Convert the image to gray scale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Use PIL to open the image and apply OCR
#     pil_image = Image.fromarray(gray)
#     text = pytesseract.image_to_string(pil_image)

#     return text

# # Example usage
# image_path = 'img4.jpg'
# extracted_text = extract_text_from_image(image_path)
# print(extracted_text)


# code2


# import cv2
# import pytesseract
# from PIL import Image

# # Function to extract text from image with preprocessing
# def extract_text_from_image(image_path):
#     # Load the image using OpenCV
#     image = cv2.imread(image_path)
    
#     # Check if the image was loaded correctly
#     if image is None:
#         raise ValueError(f"Image not found or unable to load: {image_path}")

#     # Convert the image to gray scale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian blur to the image to reduce noise
#     gray = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Use adaptive thresholding to enhance text
#     gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#     # Optionally, resize the image to improve OCR accuracy
#     gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#     # Use PIL to open the image and apply OCR
#     pil_image = Image.fromarray(gray)
#     text = pytesseract.image_to_string(pil_image)

#     return text

# # Example usage
# image_path = 'img2.jpg'  # Use the correct path to your image
# extracted_text = extract_text_from_image(image_path)
# print(extracted_text)


# code3
from flask import Flask, render_template, request, redirect, url_for
import cv2
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Route to handle the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and OCR processing
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded file to a temporary location
        image_path = os.path.join('static', file.filename)
        file.save(image_path)

        # Perform OCR on the image
        extracted_text = extract_text_from_image(image_path)

        # Remove the image after processing
        os.remove(image_path)

        return render_template('result.html', extracted_text=extracted_text)

def extract_text_from_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use PIL to open the image and apply OCR
    pil_image = Image.fromarray(gray)
    text = pytesseract.image_to_string(pil_image)

    return text

if __name__ == '__main__':
    app.run(debug=True)

