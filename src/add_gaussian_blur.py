import os
import cv2

src_dir = '../input/sharp'
images = os.listdir(src_dir)
dst_dir = '../input/gaussian_blurred'

for i in range(len(images)):
    img = cv2.imread(f"{src_dir}/{images[i]}", cv2.IMREAD_COLOR)
    blur = cv2.GaussianBlur(img, (63, 63), 0)
    cv2.imwrite(f"{dst_dir}/{images[i]}", blur)

print('done')
