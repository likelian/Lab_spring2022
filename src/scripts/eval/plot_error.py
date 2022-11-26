import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



fig, axes = plt.subplots(1, 6, figsize=(15, 4))

fig.subplots_adjust(hspace=0.125, wspace=1)


#######################

model_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/compression/error/loudness_range_error_list.json"
mean_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/compression/error/loudness_range_mean_error_list.json"

f = open(model_error_path)
data = json.load(f)
df = pd.DataFrame(data, columns = ['CNN'])

f = open(mean_error_path)
data = json.load(f)
df["mean"] = data


sns.boxplot(ax=axes[1], data=df).set(xlabel='',  ylabel='loudness range (dB)')
axes[1].set_title("Compression")

#######################

model_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/level/error/relative_loudness_error_list.json"
mean_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/level/error/relative_loudness_mean_error_list.json"

f = open(model_error_path)
data = json.load(f)
df = pd.DataFrame(data, columns = ['CNN'])

f = open(mean_error_path)
data = json.load(f)
df["mean"] = data

sns.boxplot(ax=axes[0], data=df).set(xlabel='',  ylabel='relative loudnesss (dB)')
axes[0].set_title("Level Balance")








#######################
#######################
#######################

#plt.tight_layout()
fig.savefig("error.png")
