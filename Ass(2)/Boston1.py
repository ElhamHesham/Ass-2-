

get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd
import statsmodels.api as sm
df = pd.read_csv('Boston.csv', index_col=0)
df.head()
lm = sm.OLS.from_formula('MV ~ LSTAT', df)
result = lm.fit()
result.summary()

