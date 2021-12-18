import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def readPictureText(imagePath: str) -> str:
    image = cv2.imread(imagePath)
    return pytesseract.image_to_string(image, lang='eng').replace('\n', '')


imagePaths: list[str] = ['images/bozenka.jpg',
                         'images/ulani.jpg',
                         'images/kot.jpg',
                         'images/czerwone.jpg',
                         'images/ulica.jpg',
                         'images/man.png',
                         'images/street.jpg',]

for imagePath in imagePaths:
    print('----------------------------')
    print(imagePath)
    print(readPictureText(imagePath))
