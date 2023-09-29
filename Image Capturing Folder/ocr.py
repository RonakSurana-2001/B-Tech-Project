import cv2
import pytesseract

def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

img=cv2.imread('C:\\Users\\user\\OneDrive\\Desktop\\testImage.jpg')

def get_gray_scale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

def thresholding(image):
    return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

img=get_gray_scale(img)
img=remove_noise(img)
img=thresholding(img)
print(ocr_core(img))