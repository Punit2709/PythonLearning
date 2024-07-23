import matplotlib.pyplot as plt

x = [15, 20, 25,30, 30, 35]
bunch =  [5, 8, 11, 14, 17, 20] ;
plt.hist(x, bins = bunch, color='m')
plt.show()