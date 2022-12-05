
import csv
import pandas as pd



csv_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/analysis/overall.csv"


df = pd.read_csv(csv_path, encoding = 'unicode_escape', engine ='python')
print(df)


