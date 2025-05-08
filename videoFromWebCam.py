import cv2

cap = cv2.VideoCapture(0)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera', frame)
            if cv2.waitKey(1) != -1:
                break;
        else:
            print('no frame')
            break;
else:
    print(f"Can't open a webcam!")

cap.release()
cv2.destroyAllWindows()
