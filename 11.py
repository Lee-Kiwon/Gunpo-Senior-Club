import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('a'):  # 왼쪽
        arduino.write(b'a')
        print(b'a')
    elif key == ord('d'):  # 오른쪽
        arduino.write(b'd')
        print(b'd')

cap.release()
cv2.destroyAllWindows()
