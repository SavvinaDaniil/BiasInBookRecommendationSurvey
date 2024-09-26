import os
os.system("clear")
import pandas as pd
dups_checked = pd.read_csv('datasets/more_duplicates_checked.csv') 
print(len(dups_checked))
rel_col = dups_checked.columns[2]
print(len(dups_checked[dups_checked[rel_col]=='Yes']))
print(len(dups_checked[dups_checked[rel_col]=='No']))

dups_checked[dups_checked[rel_col]=='No'].to_csv('datasets/more_duplicates_removed.csv', index=False)

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