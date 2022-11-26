import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


model_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/compression/error/loudness_range_error_list.json"
mean_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/compression/error/loudness_range_mean_error_list.json"


f = open(model_error_path)
data = json.load(f)
df = pd.DataFrame(data, columns = ['CNN'])


f = open(mean_error_path)
data = json.load(f)
df["mean"] = data

sns.set(rc={'figure.figsize':(3, 6)})
plot = sns.boxplot(data=df)
plot.set(xlabel='',  ylabel='loudness range (dB)')
plt.tight_layout()
fig = plot.get_figure()
fig.savefig("error.png")



