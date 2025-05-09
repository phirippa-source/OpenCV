import cv2 as cv
import sys

cap = cv.VideoCapture(0)              # 카메라와 연결 시도
if not cap.isOpened():
  sys.exit('[fail] - Camera Connection')

while True:
  ret, frame = cap.read()
  if not ret:
    print('[fail] - no more frame')
    break
  cv.imshow('Webcam Display', frame)
  key = cv.waitKey(1)                  # 1[ms] 동안 키보드 입력 기다림
  if key == ord('q'):                  # 'q' 키가 눌리면 while 루프를 나감
    break
 
cap.release()                          #카메라와 연결 끊음
cv.destroyAllWindows()
