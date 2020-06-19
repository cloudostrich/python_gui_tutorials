import numpy as np
from gr.pygr import mlab

# Create example data
x = np.random.uniform(-1, 1, 100)
# Draw the histogram
mlab.histogram(x)
# Draw the histogram with 19 bins
mlab.histogram(x, num_bins=19, hold=True)

