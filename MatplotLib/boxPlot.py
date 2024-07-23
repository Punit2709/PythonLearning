import matplotlib.pyplot as plt
import numpy as np

test1 = np.random.normal(200, 50, 400);
test2 = np.random.normal(100, 50, 300);
test3 = np.random.normal(100, 30, 150);
test4 = np.random.normal(150, 40, 250);

data = [test1, test2, test3, test4]
plt.boxplot(data)
plt.show()