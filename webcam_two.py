import cv2 as cv
import sys

cap = cv.VideoCapture(0)
if not cap.isOpened():
  sys.exit('[fail] - Camera Connection')

# cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

while True:
  ret, frame = cap.read()
  if not ret:
    print('error')
    break
  cv.imshow('Webcam Display', frame)
  
  if cv.waitKey(1) == ord('q'):
    break
 
cap.release()
cv.destroyAllWindows()
