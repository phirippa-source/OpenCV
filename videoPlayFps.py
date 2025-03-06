import cv2

video_file = './avi/sample.avi'
cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)  
        else:
            break;
else:
    print(f"Can't open video{vidoe_file}!")

cap.release()
cv2.destroyAllWindows()
