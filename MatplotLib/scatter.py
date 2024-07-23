import matplotlib.pyplot as plt
import numpy as np

test1 = np.random.normal(200, 50, 400);
test2 = np.random.normal(100, 50, 400);

plt.scatter(test1, test2)
plt.show()