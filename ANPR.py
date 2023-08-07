import cv2
import pytesseract
import serial
import numpy as np

# Set the Tesseract executable path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the serial connection
ser = serial.Serial('COM5', 9600)

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

#call read image function to get image from the serial port
img = read_image()

cv2.imshow("original image", img)
cv2.waitKey(0)