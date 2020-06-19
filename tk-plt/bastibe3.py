import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib as mpl

fig, ax = plt.subplots()
line, = ax.plot(np.random.randn(100))

tstart = time.time()
num_plots = 0
##fig.show()
while time.time()-tstart < 1:
##    fig.show()
    line.set_ydata(np.random.randn(100))
    fig.show()
    fig.canvas.draw()
##    fig.show()
    fig.canvas.flush_events()
##    fig.show()
    num_plots += 1
print(num_plots)
