import matplotlib.pyplot as plt

winMatche = [2, 3, 1, 5, 1]
names = ['Aus', 'Eng', 'Nz', 'Ind', 'Pak']

explodeName = [0, 0, 0, 0.02, 0]
plt.pie(winMatche, labels=names, explode= explodeName, shadow=True, autopct='%1.1f%%')
plt.legend()
plt.show()
