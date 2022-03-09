import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt


path = "../data/reverb_time/train/reverb_timeAndZeroCrossingRate.csv"
df = read_csv(path)
data = df.values

reverbTime = data[:,[1,2]].T[0]
zero_crossing_average = data[:,[1,2]].T[1]

plt.scatter(zero_crossing_average, reverbTime)
plt.title("musdb18_train")
plt.xlabel("zero_crossing_average")
plt.ylabel("Reverb Time (Seconds)")

#plt.show()

plt.savefig('../data/reverb_time/train/Reverb Time and Zero Crossing Rate.png')
