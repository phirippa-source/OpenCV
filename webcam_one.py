import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
  print("Web cam open ok~!")
else:
  print(f"Can't open a webcam!")

cap.release()
print('bye~')
