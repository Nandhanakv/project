import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])

y = np.array([3,8,1,10])

plt.bar(x,y,color = 'r',width=0.2)
plt.show()
