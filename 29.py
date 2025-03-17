import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("sales")

x1 = np.array([0,1,2,3])
y1 = np.array([5,6,7,8])
plt.subplot(1,2,2)
plt.plot(x1,y1)
plt.title("income")
plt.show()

