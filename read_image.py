import cv2

img_file = './images/AI.jpg'
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('Image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file!')
