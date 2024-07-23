import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


y = [5, 8, 7, 9, 7, 8]

# adding Details to Graph
# plt.plot(x, y, color ='blue', marker='*', markeredgecolor = 'red', markersize =10)
# plt.plot(x, y, 'r*--')

# Title to Graph
plt.title('Heading 1', fontdict={ 'fontname':'Comic Sans MS', 'fontsize' : 20})

# Labeling the Axises
plt.xlabel('X-axis')
plt.ylabel('Y-axis')


# Legend of Graph
plt.legend(['single-element'])

# saving Graph
# plt.savefig('firstGraph.png', dpi = 300)

# ax = plt.axes()
# ax.set_xlim([-5, 50])
# ax.set_ylim([0, 10])

# ax.set_xticks([-5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
# ax.set_yticks([0, 5, 10])
plt.plot(x, y, 'r*--')
plt.show()




# mobile = pd.read_csv(r'MatplotLib\flipkart.csv')
# mobile.head()
# plt.plot(mobile.year, mobile.india,  'r*--', label='India')
# plt.plot(mobile.year, mobile.america,  'y*--', label='america')
# plt.plot(mobile.year, mobile.china,  'b*--', label='china')
