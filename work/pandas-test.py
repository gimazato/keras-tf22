import pandas as pd
import numpy as np

a = np.arange(24).reshape(6,4)
#a = [[1,2,3,4],[15,6,7,8]]
df = pd.DataFrame(a, columns=["c1", "c2", "c3", "c4"])
#df = pd.DataFrame(a)
print(df)

clist = [1, 3, 5]
df.iloc[clist, 2] = 111
print(df)
#df.iloc[]