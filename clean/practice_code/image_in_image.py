

import cv2

# method = cv2.TM_SQDIFF_NORMED

# # Read the images from the file
# small_image = cv2.imread('pupil.png')
# large_image = cv2.imread('eyes.png')

# result = cv2.matchTemplate(small_image, large_image, method)

# # We want the minimum squared difference
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = small_image.shape[:2]

# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output',large_image)

# # The image is only displayed if we call this
# cv2.waitKey(0)


import cv2
import numpy as np


def image_overlay_second_method(img1, img2, location, min_thresh=0, is_transparent=False):
    h, w = img1.shape[:2]
    h1, w1 = img2.shape[:2]
    x, y = location
    roi = img1[y:y + h1, x:x + w1]

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, min_thresh, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img_fg = cv2.bitwise_and(img2, img2, mask=mask)
    dst = cv2.add(img_bg, img_fg)
    if is_transparent:
        dst = cv2.addWeighted(img1[y:y + h1, x:x + w1], 0.1, dst, 0.9, None)
    img1[y:y + h1, x:x + w1] = dst
    return img1

eyes_img = cv2.imread('eyes.png', cv2.IMREAD_UNCHANGED)
pupil_img = cv2.imread('pupil.png', cv2.IMREAD_UNCHANGED)
blue_img = cv2.imread('blue_eye.png', cv2.IMREAD_UNCHANGED)
green_eye = cv2.imread('green_eye.png', cv2.IMREAD_UNCHANGED)
result = cv2.matchTemplate(eyes_img, pupil_img, cv2.TM_CCOEFF_NORMED)
w = pupil_img.shape[1]
h = pupil_img.shape[0]
threshold = .40
yloc, xloc = np.where(result >= threshold)
for (x, y) in zip(xloc, yloc):
    img_rgb = image_overlay_second_method(eyes_img, green_eye, location=(x,y), min_thresh=0, is_transparent=True)
cv2.imwrite('result.png', img_rgb)