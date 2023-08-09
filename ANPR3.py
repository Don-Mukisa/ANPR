import cv2
import serial
import numpy as np
import imutils
import pytesseract

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
for i in range(10):
        #call read image function to get image from the serial port
        image = read_image()


        cv2.imshow("original image", image)
        cv2.waitKey(0)

#changing the image to gray scale
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("greyed image", gray_image)
#cv2.waitKey(0)

#reducing the noise in the greyscale image
#gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17) 
#cv2.imshow("smoothened image", gray_image)
#cv2.waitKey(0)

# read haarcascade for number plate detection
#cascade = cv2.CascadeClassifier('.\haarcascade_russian_plate_number.xml')

# Detect license number plates
#plates = cascade.detectMultiScale(gray_image, 1.2, 5)
#print('Number of detected license plates:', len(plates))


# loop over all plates
'''
for (x,y,w,h) in plates:
   
   # draw bounding rectangle around the license number plate
   cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
   gray_plates = gray_image[y:y+h, x:x+w]
   color_plates = image[y:y+h, x:x+w]
   
   # save number plate detected
   cv2.imwrite('Numberplate.jpg', gray_plates)
   #cv2.imshow('Number Plate', gray_plates)
   cv2.imshow('Number Plate Image', image)
   #cv2.waitKey(0)

#Extracting text from the cropped plate
if gray_plates is not None:
        #f_gray_plates = imutils.resize(gray_plates, width=321)
        #f_gray_plates = cv2.bilateralFilter(f_gray_plates, 11, 17, 17) 
        cv2.imshow("smoothened g image", gray_plates)
        
        plate = pytesseract.image_to_string(gray_plates, lang='eng')
        print("Number plate is:", plate)
        cv2.waitKey(0)
cv2.destroyAllWindows()'''