
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean



csv_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/analysis/overall.csv"


df = pd.read_csv(csv_path, encoding = 'unicode_escape', engine ='python')

#print(df)


rating_dict = {
    "Very Poor" : 1,
    "Poor" : 2,
    "Fair" : 3,
    "Good" : 4,
    "Very Good" : 5
    }

rating_score_dict = {
    "Very Poor" : 0.0,
    "Poor" : 0.25,
    "Fair" : 0.5,
    "Good" : 0.75,
    "Very Good" : 1.0
    }


#random, baseline, CNN, human

model_dict = {
    "random" : "",
    "baseline" : ".1",
    "CNN" : ".2",
    "human" :  ".3"
}



def vote_to_score(effect):

    score_dict = {
        "random" : np.array([]),
        "baseline" : np.array([]),
        "CNN" : np.array([]),
        "human" : np.array([])
        }

    for rating in rating_dict.keys():
        for model in model_dict.keys():
            score = rating_score_dict[rating]
            score_dict[model] = np.concatenate((score_dict[model], np.full(int(df.iloc[rating_dict[rating]][effect+model_dict[model]]), score)))

    
    return pd.DataFrame(score_dict)



plot_path = "../plot/"

def plot(effect, counter):
    score_df = vote_to_score(effect)
    plot = sns.violinplot(ax=axes[counter], data=score_df, cut=0, inner = 'box', bw=0.35)
    plot = sns.boxplot(ax=axes[counter], data=score_df, showmeans=True,
            meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"blue", "markersize": "10"}, width=0.01)
    #sns.pointplot(data=score_df, estimator=mean, join = False, color="white", errorbar=None)
    if counter == 0:
        ax=axes[counter].set(ylabel='score')
    ax=axes[counter].set(title=effect)
    #plot = sns.boxplot(data=score_df)
    
    #fig = plot.get_figure()
    #fig.savefig(plot_path + effect + ".png")
    #plot.figure.savefig(plot_path + effect + ".png")


    #plt.savefig(plot_path + effect + ".png")
    #plt.clf()




effect_list = ["Level Balance", "Compression", "EQ", "Reverb", "Overall"]
fig, axes = plt.subplots(1, 5, figsize=(20, 4))
fig.subplots_adjust(hspace=0.125, wspace=1)

counter = 0
for effect in effect_list:
    plot(effect, counter)
    counter += 1

fig.tight_layout()
fig.savefig(plot_path + "rating.png")





