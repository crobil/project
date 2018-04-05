from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y = x*5

plt.xlim(2,3)
plt.ylim(5,20)
plt.plot(x,y,'r')
plt.xlabel('x line')
plt.ylabel('y line')
plt.title('matplotlib sample')
plt.show()
