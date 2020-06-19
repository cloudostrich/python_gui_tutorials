
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib as mpl

plt.ioff()
fig, ax = plt.subplots()
line, = ax.plot(np.random.randn(100))
plt.show(block=False)

tstart = time.time()
num_plots = 0
fig.canvas.draw()
while time.time()-tstart < 1:
    line.set_ydata(np.random.randn(100))
##    fig.canvas.draw()
    ax.draw_artist(ax.patch)
    ax.draw_artist(line)
    fig.canvas.update()
    fig.canvas.flush_events()
    num_plots += 1
print(num_plots)
