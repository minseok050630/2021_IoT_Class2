import cv2

#카메라 장치 열기
cap = cv2.VideoCapture('output.avi') # 카메라 장치 열기

if not cap.isnotOpened():
    print('Camera open failed')
    exit()

# 카메라 사진 찍기
# ret, frame = cap.read()
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg', frame)

while True:
    ret,frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break

#사용자 지원 해제
cap.release()
cv2.dsetroyAllWindows()
