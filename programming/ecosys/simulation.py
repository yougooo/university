from animals import Fox
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

fox = Fox(30, 500, 50)
fox.time_line(fox)

coeff = np.polyfit(range(len(fox.rabbit_progress)), fox.rabbit_progress, 2)
plt.plot(np.polyval(coeff, range(len(fox.rabbit_progress))), 'green')
plt.plot(fox.rabbit_progress, 'go')

coeff1 = np.polyfit(range(len(fox.rabbit_progress)), fox.fox_progress, 2)
plt.plot(np.polyval(coeff1, range(len(fox.rabbit_progress))), 'red')
plt.plot(fox.fox_progress, 'ro')

plt.show()
