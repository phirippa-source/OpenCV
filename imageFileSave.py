import cv2

img_file = './images/AI.jpg'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow(img_file, img)

gray_file = './images/AI_gray.jpg'
cv2.imwrite(gray_file, img)

cv2.waitKey()
cv2.destroyAllWindows()
