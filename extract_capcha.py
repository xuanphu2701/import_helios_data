import cv2
import numpy as np
import pytesseract

# Avoid installing tesseract in Program Files directory
BYTETESSERACT_LOCAL_PATH = r"C:\Tesseract-OCR\tesseract.exe"


def extract_capcha(img_path):
    """
    Extract the capcha from the capcha image
    Warning: Any capcha image change could make this function execute unexpectedly
    :param img_path:
    :return: extracted capcha in string
    """
    img = cv2.imread(img_path)

    # Cvt to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get binary-mask
    msk = cv2.inRange(hsv, np.array([1, 100, 100]), np.array([2, 255, 255]))

    krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
    dlt = cv2.dilate(msk, krn, iterations=1)
    thr = 255 - cv2.bitwise_and(dlt, msk)

    # OCR
    pytesseract.pytesseract.tesseract_cmd = BYTETESSERACT_LOCAL_PATH
    d = pytesseract.image_to_string(thr, config="--psm 10")
    return d