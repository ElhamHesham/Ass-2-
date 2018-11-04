


get_ipython().run_line_magic('pylab', 'inline')

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns

# special matplotlib argument for improved plots
from matplotlib import rcParams
sns.set_style("whitegrid")
sns.set_context("poster")

from sklearn.datasets import load_boston
boston = load_boston()
boston.keys()
boston.data.shape
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
data['PRICE'] = boston.target

Z = data.LSTAT
W = data.PRICE

#mean of our inputs and outputs
z_mean = np.mean(Z)
w_mean = np.mean(W)

n = len(Z)

#using the formula to calculate the o1 and o0
a = 0
b = 0
for i in range(n):
    a += (Z[i] - z_mean) * (W[i] - w_mean)
    b += (Z[i] - z_mean) ** 2
B1 = a / b
B0 = w_mean - (B1 * z_mean)

#printing the coefficient
print('Coefficient of Boston dataset B0 = ' ,B1,'B1 = ', B0)


