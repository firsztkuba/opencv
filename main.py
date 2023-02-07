import cv2

img = cv2.imread("image.jpg", 0)
img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Days Gone", img)
cv2.imwrite("Days Gone Grayscale.jpg", img)
cv2.waitKey(5000)
cv2.destroyAllWindows