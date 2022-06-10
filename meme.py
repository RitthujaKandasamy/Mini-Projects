import cv2
import matplotlib.pyplot as plt


img = cv2.imread("image\\thanos.jpg")


# check image is working or not
print(type(img))


# change the color into RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# plot 
plt.figure(figsize=(10, 8))
plt.title("Thanos-RGB")
plt.imshow(rgb_img)
plt.show()


# create memes
cv2.putText(img, 'THANOS MEME', (450, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 20)
cv2.putText(img, 'IMPOSSIBLE', (200, 500), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 3)


# check with cv2 in window, press Q to stop
cv2.imshow('Thanos-Meme', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
