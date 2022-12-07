from scipy.stats import mannwhitneyu
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean






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

def vote_to_score_dict(effect):

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

    
    return score_dict



plot_path = "../plot/"

def plot(effect, counter, isTop=False, isBottom=False):

    score_df = vote_to_score(effect)
    plot = sns.violinplot(ax=axes[counter], data=score_df, cut=0.1, inner = 'box', bw=0.35)
    plot = sns.boxplot(ax=axes[counter], data=score_df, showmeans=True,
            meanprops={"marker":"s","markerfacecolor":"white", "markeredgecolor":"blue", "markersize": "10"}, width=0.01)
    #sns.pointplot(data=score_df, estimator=mean, join = False, color="white", errorbar=None)
    if counter == 0:
        ax=axes[counter].set(ylabel='score')
    else:
        ax=axes[counter].set(yticklabels=[])
    
    
    


    if isTop:
        ax=axes[counter].set(title=effect)

    if not isBottom:
         ax=axes[counter].set(xticklabels=[])





effect_list = ["Level Balance", "Compression", "EQ", "Reverb", "Overall"]

csv_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/analysis/All-Table 1.csv"

df = pd.read_csv(csv_path, encoding = 'unicode_escape', engine ='python')


score_dict = vote_to_score_dict("Overall")

for model in model_dict.keys():
    for another_model in model_dict.keys():
        if model == another_model:
            continue
        
        U1, p = mannwhitneyu(score_dict[model], score_dict[another_model])

        print(" ")
        print(model)
        print(another_model)
        print(p)
        


        







#males = [1, 1, 1, 1]
#females = [2, 2, 2, 2]
#U1, p = mannwhitneyu(males, females)
#print(p)