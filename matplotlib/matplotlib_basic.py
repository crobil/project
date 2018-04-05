from matplotlib import pyplot as plt 
import numpy as np
import matplotlib
matplotlib.use('Agg')                                                                                
x = np.arange(1,10)
y = x*5 
plt.plot(x,y)
plt.show()
