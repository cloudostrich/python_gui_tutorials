import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [2,3,6,4,7]

x2 = [1,3,5,7,9]
y2 = [1,4,7,3,9]

plt.bar(x,y, label='bar 1', color='b')
plt.bar(x2,y2, label='bar2', color='r')

plt.xlabel('plot label')
plt.ylabel('y label')
plt.title('big title\n check it out')

plt.legend()
plt.show()
