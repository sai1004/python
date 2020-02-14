"""

+=======================================+
| packages Required:                    |
|    pip3 install opencv-python qrcode  |
|    pip3 install qrcode[pil]           |
|                                       |
+=======================================+


"""

import cv2
import qrcode

# """"""""""""""" Generate QR Code """""""""""""""

# example data
data = "'Welcome To Simplified Python'"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

# """"""""""""""" Reading QR Code """""""""""""""

# read the QRCODE image
img = cv2.imread("site.png")

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
    # display the result
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
