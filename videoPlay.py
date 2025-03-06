import cv2

video_file = './avi/sample.avi'
cap = cv2.VideoCapture(video_file)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(33)   # sample.avi 파일이 30fps이라면 1/30, 약 33[ms]
        else:
            break;
else:
    print(f"Can't open video{vidoe_file}!")

cap.release()
cv2.destroyAllWindows()
