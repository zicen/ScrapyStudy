#coding=utf8
import pytesseract
from PIL import Image

image = Image.open('test.jpg')
text = pytesseract.image_to_string(image)
print text