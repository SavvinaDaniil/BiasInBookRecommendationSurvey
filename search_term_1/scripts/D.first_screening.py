import os
os.system("clear")
import pandas as pd
first_screening = pd.read_csv('datasets/first_screening.csv') 
print(len(first_screening))
rel_col = first_screening.columns[1]
print(len(first_screening[first_screening[rel_col]=='Yes']))

first_screening[first_screening[rel_col]=='Yes'].to_csv('datasets/first_screening_clean.csv', index=False)

# scopus.columns = ['Authors', 'Title', 'Year', 'Venue', 'Link', 'Abstract']
# # print(google.columns, scopus.columns)
# scopus = scopus[google.columns]

# merged = pd.concat([google,scopus], axis=0, keys = ['Google','Scopus']).reset_index().drop('level_1',axis=1).rename(columns={'level_0':'Database'})
# print(len(merged))
# duplicate = merged[merged.duplicated(['Title'], keep = False)].sort_values('Title')
# print(len(duplicate))
# duplicate.to_csv('duplicates.csv', index=False)



# row_to_keep = duplicate.iloc[21] # we keep the michael ekstrand extended paper
# print(row_to_keep)
# removed_duplicates = merged.drop_duplicates(subset=['Title'], keep = 'first', ignore_index=True)

# removed_duplicates.loc[len(removed_duplicates)] = row_to_keep

# removed_duplicates.to_csv('clean_merged_results.csv', index=False)
# print(len(removed_duplicates))