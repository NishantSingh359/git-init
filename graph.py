import matplotlib.pyplot as plt
import numpy as np

x:np.ndarray = np.arange(1,11)
y:np.ndarray = np.random.randint(100, 500, 10)

plt.figure(figsize=(5,4))
plt.title("Bar Plot", fontdict=dict(size=15, color='gray'), loc='left')
plt.bar(x, y, color='red')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('gray')
plt.gca().spines['bottom'].set_color('gray')
plt.gca().minorticks_on()
plt.xticks(color='gray')
plt.yticks(color='gray')
plt.tick_params(color='gray')
plt.show()