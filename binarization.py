import cv2

# 임계값 설정하는 트랙바 만들기
def nothing(x):
    pass
cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)

# 초기 임계값 설정
cv2.setTrackbarPos('threshold', 'Binary', 120)






# 칼라
img_color = cv2.imread('red_ball.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Color', img_color)


# 흑백
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', img_gray)

# 트랙바 바로바로 출력 while
while(True):
    # 임계값 설정
    low = cv2.getTrackbarPos('threshold', 'Binary')

    # 이진화 (흑백이여야함) (THRESH_BINARY_INV 로 바꾸면 반전됨)
    ret,img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary', img_binary)

    # 추출된 것 보여주기
    img_result = cv2.bitwise_and(img_color, img_color, mask = img_binary)
    cv2.imshow('Result', img_result)

    # esc 누르면 종료
    if cv2.waitKey(1)&0xFF == 27:
        break


cv2.destroyAllWindows()