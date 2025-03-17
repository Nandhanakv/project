import matplotlib.pyplot as plt
import numpy as np

x= np.random.randint(100, size=(100))
y= np.random.randint(100 ,size=(100))
sizes = np.random.randint(1000, size=(100))
colors = 90 * np.random.randint(100, size=(100))

plt.scatter(x,y,s=sizes,c=colors,alpha=0.5,cmap='nipy_spectral')
plt.colorbar()
plt.show()
