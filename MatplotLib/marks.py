import matplotlib.pyplot as plt

exam1 = [20, 18, 16, 19, 20, 17, 15]
exam2 = [12, 17, 15, 17, 20, 18, 17]

plt.plot(range(1, 8), exam1, 'r*--')
plt.plot(range(1, 8), exam2, 'm*--')

# plt.legend = ['Exam1', 'Exam2']
plt.legend()
plt.xlabel('Roll No')
plt.ylabel('Marks')
plt.title('Marks Chart')
plt.savefig('MatplotLib\Marks.png')
plt.show()
