import cv2

# image 파일 읽기
img = cv2.imread('카리나.jpg')
img = cv2.resize(img, (600, 400))

# imshow(윈도우 이름 출력할 영상데이터)
cv2.imshow('카리나', img)

# edge 선 추출하기
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

cv2.waitKet(0)

cv2.destroyAllWindoows()