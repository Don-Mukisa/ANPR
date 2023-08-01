import cv2
import pytesseract
import serial
import numpy as np

# Set the Tesseract executable path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the serial connection
ser = serial.Serial('COM3', 9600)

# Function to read an image from the serial connection
def read_image():
    data = []
    for i in range(240): # height of the image
        row = []
        for j in range(320): # width of the image
            byte = ser.read()
            row.append(int.from_bytes(byte, byteorder='big'))
        data.append(row)
    img = np.array(data, dtype=np.uint8)
    return img

# Function to process image
def process_image(img):
    # Use OpenCV to process the image (e.g., grayscale, blur, edge detection)
    # This will depend on your specific requirements
    processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return processed_img

# Function to perform OCR with Tesseract
def perform_ocr(img):
    text = pytesseract.image_to_string(img)
    return text

# Main loop
while True:
    # Read an image from the serial connection
    img = read_image()

    # Process the image with OpenCV
    processed_img = process_image(img)

    # Perform OCR with Tesseract
    text = perform_ocr(processed_img)

    # Print the extracted text
    print(text)
