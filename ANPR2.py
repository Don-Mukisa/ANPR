import cv2
import imutils
import pytesseract

# Set the Tesseract executable path 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#resizing the image
image = cv2.imread(r"C:\Users\DON\OneDrive\Desktop\TEST_IMAGES\download(2).png")
image = imutils.resize(image, width=320 )
cv2.imshow("original image", image)
cv2.waitKey(0)

#changing the image to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
cv2.waitKey(0)

#reducing the noise in the greyscale image
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17) 
cv2.imshow("smoothened image", gray_image)
cv2.waitKey(0)

#Detecting edges
edged = cv2.Canny(gray_image, 30, 200) 
cv2.imshow("edged image", edged)
cv2.waitKey(0)

#Contours from the edged image onto the original image 
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)
cv2.waitKey(0)

#sorting the contours
cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
screenCnt = None
image2 = image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
cv2.waitKey(0)

#Finding the contour with 4 sides
i=7
for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4: 
                screenCnt = approx

#cropping rectangular part identified as license plate
                x,y,w,h = cv2.boundingRect(c) 
                new_img=image[y:y+h,x:x+w]
                cv2.imwrite('./'+str(i)+'.png',new_img)
                i+=1
                break
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("image with detected license plate", image)
cv2.waitKey(0)

#Extracting text from the cropped plate
Cropped_loc = './7.png'
cv2.imshow("cropped", cv2.imread(Cropped_loc))
plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
print("Number plate is:", plate)
cv2.waitKey(0)
cv2.destroyAllWindows()