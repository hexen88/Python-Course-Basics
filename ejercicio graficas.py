import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lista = np.random.randn(1000)

plt.hist(lista)
plt.show()

sns.boxplot(lista)
plt.show()

