import os
os.system("clear")
import pandas as pd


RIS_table = pd.read_csv('search_term_3/LIS_venues/datasets/RIS_table.csv') 
BIB_table = pd.read_csv('search_term_3/LIS_venues/datasets/BIB_table.csv')
print(len(RIS_table))
print(len(BIB_table))

final_table = pd.concat([BIB_table, RIS_table], ignore_index=True)

final_table.to_csv('search_term_3/LIS_venues/datasets/LIS_venues_table.csv', index=False)
