import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10, 14,12]

plt.plot(x,y, label='line 1')
plt.plot(x2, y2, label='line 2')
plt.xlabel('plot label')
plt.ylabel('y label')
plt.title('big title\n check it out')

plt.legend()
plt.show()
