import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt


path = "../data/reverb_time/train/reverb_timeAndBeat.csv"
df = read_csv(path)
data = df.values

reverbTime = data[:,[1,2]].T[0]
beat = data[:,[1,2]].T[1]

plt.scatter(beat, reverbTime)
plt.title("musdb18_train")
plt.xlabel("Beat Density")
plt.ylabel("Reverb Time (Seconds)")

#plt.show()

plt.savefig('../data/reverb_time/train/Reverb Time and Beat.png')
