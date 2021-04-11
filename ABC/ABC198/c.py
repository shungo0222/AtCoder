import math
import numpy as np

r, x, y = map(int, input().split())
d = np.linalg.norm([x, y])
if r > d:
    print(2)
else:
    print(math.ceil(d/r))