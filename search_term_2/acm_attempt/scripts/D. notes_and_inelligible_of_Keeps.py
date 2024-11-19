import os
os.system("clear")
import pandas as pd
eligible = pd.read_csv('search_term_2/acm_attempt/datasets/eligibility_checked_for_KEEPS.csv') 
print('All',len(eligible))
rel_col = eligible.columns[2]
print('Yes',len(eligible[eligible[rel_col]=='Yes']))
# print(len(eligible[eligible[rel_col]=='No']))
print('Keep',len(eligible[eligible[rel_col]=='Keep']))
print('Library',len(eligible[eligible[rel_col]=='Library']))
print('Survey',len(eligible[eligible[rel_col]=='Survey']))
print('No',len(eligible[eligible[rel_col]=='No']))
print('Old version',len(eligible[eligible[rel_col]=='Old version']))

eligible[eligible[rel_col]=='Yes'].to_csv('search_term_2/acm_attempt/datasets/keeps_clean_yes.csv', index=False)
eligible[eligible[rel_col]=='Keep'].to_csv('search_term_2/acm_attempt/datasets/keeps_clean_keeps.csv', index=False)
eligible[eligible[rel_col]=='Library'].to_csv('search_term_2/acm_attempt/datasets/keeps_clean_library.csv', index=False)

