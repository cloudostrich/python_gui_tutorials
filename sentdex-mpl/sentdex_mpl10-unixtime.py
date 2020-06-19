import datetime as dt
import time
import numpy as np

print(time.time())

eg = time.time()
print(eg)

print(dt.datetime.fromtimestamp(eg))

dateconv = np.vectorize(dt.datetime.fromtimestamp)
print(dateconv)
