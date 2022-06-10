import cv2
import matplotlib.pyplot as plt


ann_img = cv2.imread("image\dog.jpg")


# check image is working or not
print(type(ann_img))


# plot the image
plt.figure(figsize = (10, 8))
plt.title("Dog")
plt.imshow(ann_img)
plt.show()


# change the color into RGB
ann_rgb_img = cv2.cvtColor(ann_img, cv2.COLOR_BGR2RGB)


# plot again
plt.figure(figsize=(10, 8))
plt.title("Dog-RGB")
plt.imshow(ann_rgb_img)
plt.show()


# create the annotation with rectangle
cv2.rectangle(ann_img, (150, 50), (600, 600), (0, 0, 255), 4)
cv2.rectangle(ann_img, (150, 50), (280, 10), (0, 0, 255), cv2.FILLED)
cv2.putText(ann_img, 'Dog', (190, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))



# check with cv2 in window, press Q to stop
cv2.imshow('Dog-Annotation', ann_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)


