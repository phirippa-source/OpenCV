import cv2

img_file = './images/flower-240x320.jpe'
img = cv2.imread(img_file)

if img is not None:
    cv2.putText(img, "Plain", (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
    cv2.putText(img, "Simplex", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    cv2.putText(img, "Simplex", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(img, "Duplex", (10, 120), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 4)
    
    cv2.imshow('Image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file!')
