# chess-mate
# A computer vision program to interpret current chess piece positions and describe the board state using
# Forsyth-Edwards Notation (FEN).



import qrcode

import cv2
import numpy as np
from pyzbar.pyzbar import decode


def makeQRCode(data):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(str(data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.show()
    img.save("qrcodeimage.PNG", "PNG")



def scanQRCode(image):

    imgread = cv2.imread(image)

    for qrcode in decode(img):
        print(qrcode.data)




if __name__ == '__main__':

    makeQRCode("w_king")
    scanQRCode("qrcodeimage.PNG")
