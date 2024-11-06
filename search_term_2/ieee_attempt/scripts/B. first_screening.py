import os
os.system("clear")
import pandas as pd
first_screening = pd.read_csv('search_term_2/ieee_attempt/datasets/first_screening.csv') 
print(len(first_screening))
rel_col = first_screening.columns[1]
print(len(first_screening[first_screening[rel_col]=='Yes']))
print(len(first_screening[first_screening[rel_col]=='No']))
print(len(first_screening[first_screening[rel_col]=='Keep']))

# first_screening[first_screening[rel_col]=='Yes'].to_csv('search_term_2/elsevier_attempt/datasets/first_screening_clean.csv', index=False)
# first_screening[first_screening[rel_col]=='Keep'].to_csv('search_term_2/elsevier_attempt/datasets/first_screening_clean_KEEPS.csv', index=False)