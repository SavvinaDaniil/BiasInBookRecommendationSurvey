import os
os.system("clear")
import pandas as pd
elig_checked = pd.read_csv('datasets/eligibility_checked.csv') 
print(len(elig_checked))
rel_col = elig_checked.columns[4]
print(len(elig_checked[elig_checked[rel_col]=='Yes']))
print(len(elig_checked[elig_checked[rel_col]=='No']))

elig_checked[elig_checked[rel_col]=='Yes'].to_csv('datasets/only_eligible.csv', index=False)


