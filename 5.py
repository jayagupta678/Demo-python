import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.DataFrame({'C1': {'a': 1,'b': 15,'c': 9,'d': 7,'e': 2,'f': 2,'g': 6,'h': 5,'k': 5,'l': 8},
          'C2': {'a': 6,'b': 18,'c': 13,'d': 8,'e': 6,'f': 6,'g': 8,'h': 9,'k': 13,'l': 15}})

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

JG1 = sns.jointplot("C1", "C2", data=df, kind='reg')
JG2 = sns.jointplot("C1", "C2", data=df, kind='kde')

#subplots migration
f = plt.figure()
for J in [JG1, JG2]:
    for A in J.fig.axes:
        f._axstack.add(f._make_key(A), A)

#subplots size adjustment
f.axes[0].set_position([0.05, 0.05, 0.4,  0.4])
f.axes[1].set_position([0.05, 0.45, 0.4,  0.05])
f.axes[2].set_position([0.45, 0.05, 0.05, 0.4])
f.axes[3].set_position([0.55, 0.05, 0.4,  0.4])
f.axes[4].set_position([0.55, 0.45, 0.4,  0.05])
f.axes[5].set_position([0.95, 0.05, 0.05, 0.4])