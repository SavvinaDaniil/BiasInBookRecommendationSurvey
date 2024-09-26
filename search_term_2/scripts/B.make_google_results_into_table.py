import os
os.system("clear")
import pickle as pkl
import pandas as pd


with open('search_term_2/datasets/google_results.pkl', 'rb') as handle:
    all_results = pkl.load(handle)

res_df = pd.DataFrame(columns = ['Title','Authors','Venue', 'Year', 'Abstract','Link'])
for i in range(len(all_results)):
    result = all_results[i]
    info = result['bib']
    res_df.at[i, 'Title'] = info['title']
    res_df.at[i, 'Authors'] = info['author']
    res_df.at[i, 'Venue'] = info['venue']
    res_df.at[i, 'Year'] = info['pub_year']
    res_df.at[i, 'Abstract'] = info['abstract']
    try:
        res_df.at[i, 'Link'] = result['pub_url']
    except:
        res_df.at[i, 'Link'] = 'missing'
        
print(res_df)
res_df.to_csv('search_term_2/datasets/google_results_table.csv',index=False)