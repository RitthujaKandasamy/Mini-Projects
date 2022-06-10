import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("image\Fotolia_94207102_Subscription_Monthly_M.jpg")
image2 = cv2.imread("image\\bird.jpg")


# check images is working or not
print(type(image))
print(type(image2))


# change the color into RGB
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rgb_img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB) 


# plot again
plt.figure(figsize=(10, 8))
plt.title("RGB")
plt.subplot(1,2,1)
plt.imshow(rgb_img)
plt.subplot(1,2,2)
plt.imshow(rgb_img2)
plt.show()


# resize the image
rgb_img = cv2.resize(rgb_img, (640, 480))
rgb_img2 = cv2.resize(rgb_img2, (640, 480))


# merge 
lower_green = np.array([0, 40, 0]) 
upper_green = np.array([160, 255, 190])

mask = cv2.inRange(rgb_img, lower_green, upper_green)

rgb_img[mask != 0] = [0,0,0]
rgb_img2[mask == 0] = [0,0,0]

merged = cv2.add(rgb_img, rgb_img2)

plt.figure(figsize = (15, 10))
plt.imshow(merged)
plt.show()
