import cv2

cap = cv2.VideoCapture(0)

limit = 0

while True:
    ret, img = cap.read()
    img = cv2.resize(img, (50, 50))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if limit < 2:
        print(img.shape)
        print(type(img))
        print(img)
        limit += 2

    cv2.imshow('Image', img)
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
