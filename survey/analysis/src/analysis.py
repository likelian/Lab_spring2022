
import csv
import pandas as pd



csv_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/results/Automatic Mixing Official_November 26, 2022_10.22.csv"


df = pd.read_csv(csv_path, encoding = 'unicode_escape', engine ='python')
print(df)


