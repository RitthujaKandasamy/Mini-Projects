import cv2
import matplotlib.pyplot as plt



qr_img = cv2.imread("image\qr.jpg")

# check qr_code is working or not
print(type(qr_img))


# plot the image
plt.figure(figsize = (10, 8))
plt.title("QR-Code")
plt.imshow(qr_img)
plt.show()


# read the qr-code
decoder = cv2.QRCodeDetector()
data, points, _ = decoder.detectAndDecode(qr_img)
if points is not None:
    print('Decoded data: ', data)



# check with cv2 in window, press Q to stop
cv2.imshow('Detected QR code', qr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
