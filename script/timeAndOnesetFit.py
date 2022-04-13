import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt


path = "../data/reverb_time/train/reverb_timeAndOnset.csv"
df = read_csv(path)
data = df.values

reverbTime = data[:,[1,2]].T[0]
onset = data[:,[1,2]].T[1]

plt.scatter(onset, reverbTime)
plt.title("musdb18_train")
plt.xlabel("Onset Density")
plt.ylabel("Reverb Time (Seconds)")

#plt.show()

plt.savefig('../data/reverb_time/train/Reverb Time and Onset.png')
