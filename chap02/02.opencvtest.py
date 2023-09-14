import numpy as np
import cv2

green_color = (0, 255, 0)  # 초록색 (BGR 순서)
image = np.full((500, 800, 3), green_color, dtype=np.uint8)


cv2.imshow("202111432_KimMyeongJun",image)
cv2.waitKey(0)
cv2.destroyAllWindows()