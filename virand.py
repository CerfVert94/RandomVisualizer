import numpy as np
import cv2

uinfo = np.iinfo(np.uint16)
mask = 0xFF
half_size = 8
size = (uinfo.max + 1) >> half_size
rand_matrix = np.zeros([size, size], dtype = np.uint8)

n = 256 * size * size
for i in range(0, n) :
    rand = np.random.randint(uinfo.max)
    x = (rand & mask)
    y = ((rand >> half_size) & mask)
    rand_matrix[x,y] =  (rand_matrix[x,y] + 1) & 0xFF

cv2.imwrite(f"visualized_random_{n}.png", rand_matrix)
