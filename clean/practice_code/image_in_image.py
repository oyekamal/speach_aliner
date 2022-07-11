

import cv2

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('pupil.png')
large_image = cv2.imread('eyes.png')

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

img_rgb  = cv2.imread('pupil.png')
template = cv2.imread('eyes.png') 
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .10
loc = np.where(res >= threshold)

# for pt in zip(*loc[::-1]):  # Switch collumns and rows
#     cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# cv2.imwrite('result.png', img_rgb)