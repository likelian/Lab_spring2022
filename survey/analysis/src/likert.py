import plot_likert
import pandas as pd



csv_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/analysis/Unexperienced-Table 1.csv"

df = pd.read_csv(csv_path, encoding = 'unicode_escape', engine ='python')


plot_likert.plot_likert(df, plot_likert.scales.agree, plot_percentage=True)