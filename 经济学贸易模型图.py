import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#ss = pd.read_csv('data/Helium_10_test.csv')
#xls = pd.read_excel('ec.xlsx')
#print(ss)

nm_td = [0, 32]
nm_nr = [8, 0]
mn_td = [0, 48]
mn_nr = [24, 0]

plt.plot(nm_td, nm_nr)
plt.plot(mn_td, mn_nr)
plt.show()