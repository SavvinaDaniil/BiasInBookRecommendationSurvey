import os
os.system("clear")
import pandas as pd
retr_checked = pd.read_csv('datasets/retrievability_checked.csv') 
print(len(retr_checked))
rel_col = retr_checked.columns[3]
print(len(retr_checked[retr_checked[rel_col]=='Yes']))
print(len(retr_checked[retr_checked[rel_col]=='No']))

retr_checked[retr_checked[rel_col]=='Yes'].to_csv('datasets/only_retrievable.csv', index=False)
