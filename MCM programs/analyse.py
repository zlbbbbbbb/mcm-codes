import numpy as np
import matplotlib.pyplot as plt
import model4
import scipy.io as io
import pandas as pd

data = pd.read_csv("MySprinterManMfinal.csv")
#plt.plot(data["0"])

ans = model4.callsmooth_straight(0)(data["0"].values, np.ones(2))
