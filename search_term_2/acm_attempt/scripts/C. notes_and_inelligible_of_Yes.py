import os
os.system("clear")
import pandas as pd
eligible = pd.read_csv('search_term_2/acm_attempt/datasets/eligibility_checked_for_Yes.csv') 
print(len(eligible))
rel_col = eligible.columns[2]
print(len(eligible[eligible[rel_col]=='Yes']))
print(len(eligible[eligible[rel_col]=='No']))
print(len(eligible[eligible[rel_col]=='Keep']))

eligible[eligible[rel_col]=='Yes'].to_csv('search_term_2/acm_attempt/datasets/second_screening_clean.csv', index=False)
eligible[eligible[rel_col]=='Keep'].to_csv('search_term_2/acm_attempt/datasets/second_screening_clean_KEEPS.csv', index=False)

