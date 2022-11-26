import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



fig, axes = plt.subplots(1, 7, figsize=(16, 4))

fig.subplots_adjust(hspace=0.125, wspace=1)


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


######################

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


model_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/EQ/error/EQ_error_list.json"
mean_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/EQ/error/EQ_mean_error_list.json"

f = open(model_error_path)
data = json.load(f)
data_arr = np.array(data)
data_arr = np.where(data_arr > 30., 30., data_arr)
data_arr = np.where(data_arr < -30., -30., data_arr)

df = pd.DataFrame(data_arr[:100], columns = ['CNN'])

f = open(mean_error_path)
data = json.load(f)
df["mean"] = data[:100]


sns.boxplot(ax=axes[2], data=df).set(xlabel='',  ylabel='gain (dB)')
axes[2].set_title("EQ")



#######################

model_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/reverb/error/reverb_error_df.json"
mean_error_path = "/home/kli421/dir1/Lab_spring2022/results/final/reverb/error/reverb_mean_error_df.json"

f = open(model_error_path)
data = json.load(f)
model_df = pd.DataFrame(data)

f = open(mean_error_path)
data = json.load(f)
mean_df = pd.DataFrame(data)


"""
print(model_df.columns)

Index(['room_size', 'reverberation_time_s', 'lows_cutoff_frequency_hz',
       'lows_q_factor', 'lows_gain_db_s', 'highs_cutoff_frequency_hz',
       'highs_q_factor', 'highs_gain_db_s', 'fade_in_time_s', 'dry_wet'],
      dtype='object')
"""

#######

dry_wet_df = pd.DataFrame()
dry_wet_df['CNN'] = np.array(model_df["dry_wet"].values.tolist()) * 100.
dry_wet_df['mean'] = np.array(mean_df["dry_wet"].values.tolist()) * 100.



sns.boxplot(ax=axes[3], data=dry_wet_df).set(xlabel='',  ylabel='%')
axes[3].set_title("Dry/Wet Ratio")


#######

RT_df = pd.DataFrame()
RT_df['CNN'] = model_df["reverberation_time_s"].values.tolist()
RT_df['mean'] = mean_df["reverberation_time_s"].values.tolist()

sns.boxplot(ax=axes[4], data=RT_df).set(xlabel='',  ylabel='seconds')
axes[4].set_title("Reverb Time")


#######

FT_df = pd.DataFrame()
FT_df['CNN'] = model_df["fade_in_time_s"].values.tolist()
FT_df['mean'] = mean_df["fade_in_time_s"].values.tolist()

sns.boxplot(ax=axes[5], data=FT_df).set(xlabel='',  ylabel='seconds')
axes[5].set_title("Fade-In Time")

#######

room_size_df = pd.DataFrame()
room_size_df['CNN'] = model_df["room_size"].values.tolist()
room_size_df['mean'] = mean_df["room_size"].values.tolist()

sns.boxplot(ax=axes[6], data=room_size_df).set(xlabel='',  ylabel='index')
axes[6].set_title("Room Size")






#######################
#######################
#######################

#plt.tight_layout()
fig.savefig("error.png")
