import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,3,3,5,6,3,6]

plt.scatter(x,y, label='scatter', color='k', marker='x', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('main title')
plt.legend()
plt.show()
