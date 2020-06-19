import matplotlib.pyplot as plt

popn_ages = [24,25,65,43,46,37,8,2,75,34,99,53,22]

##ids = [x for x in range(len(popn_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,120]

plt.hist(popn_ages, bins, histtype='bar', rwidth=0.8, label='wat')

plt.xlabel('plot label')
plt.ylabel('y label')
plt.title('big title\n check it out')

plt.legend()
plt.show()
