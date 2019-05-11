import cv2
from matrix_ops import MatrixOps
import numpy as np

ops = MatrixOps(600)

# image = np.array(ops.randomized_matrix())
# image = np.array(ops.vertical_ascending_matrix(10, 150))
image = np.array(ops.random_RGB_matrix())

while True:
    cv2.imshow('Image', image)
    if cv2.waitKey(1) &0xff == ord('q'):
        break

cv2.imwrite('outputs/output-{}.jpeg'.format(np.random.randint(1, 1000)), image)
cv2.destroyAllWindows()
