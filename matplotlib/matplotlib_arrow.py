from matplotlib import pyplot as plt
import numpy as np

from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10)
y = x*5

plt.plot(x,y)
plt.annotate('annotate',xy=(2,10),xytext=(5,20),arrowprops={'color':'green'})
plt.show()

