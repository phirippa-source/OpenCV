import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print('cap open failed!')
    exit()
else:
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("webcam", frame)
            if cv2.waitKey(1) != -1:
                break
        else:
            print("Can't read cap")
            break
        
    cap.release()
    cv2.destoryAllwindows()
