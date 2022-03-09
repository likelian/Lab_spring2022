import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt


path = "../data/reverb_time/train/reverb_timeAndSpectralFlux.csv"
df = read_csv(path)
data = df.values

reverbTime = data[:,[1,2]].T[0]
tempo = data[:,[1,2]].T[1]

plt.scatter(tempo, reverbTime)
plt.title("musdb18_train")
plt.xlabel("SpectralFlux")
plt.ylabel("Reverb Time (Seconds)")

#plt.show()

plt.savefig('../data/reverb_time/train/Reverb Time and SpectralFlux.png')
