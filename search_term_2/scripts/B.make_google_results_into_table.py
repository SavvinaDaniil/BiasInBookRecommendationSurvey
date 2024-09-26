import os
os.system("clear")
import pickle as pkl
import pandas as pd


with open('search_term_2/datasets/google_results.pkl', 'rb') as handle:
    all_results = pkl.load(handle)
    
print(len(all_results))

# print(all_results)
results = [x for xs in all_results for x in xs]
print(len(results))
fr = results[0]
print(fr.keys())
print(fr['title'], fr['link'], [x['name'] for x in fr['publication_info']['authors']], fr['snippet'], fr['resources'])
print(fr['publication_info']['summary'])

for key in fr.keys():
    print(key, ":", fr[key])
    print('\n')
# print(all_results)

results = [x for x in results if x!='']
res_df = pd.DataFrame(columns = ['Title','Authors','Abstract','Link'])
for i in range(len(results)):
    result = results[i]
    try:
        res_df.at[i, 'Title'] = result['title']
    except:
        res_df.at[i, 'Title'] = 'missing'
    try:
        res_df.at[i, 'Authors'] = [x['name'] for x in result['publication_info']['authors']]
    except:
        res_df.at[i, 'Authors'] = 'missing'
    try:
        res_df.at[i, 'Abstract'] = result['snippet']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    try:
        res_df.at[i, 'Link'] = result['link']
    except:
        res_df.at[i, 'Link'] = 'missing'
# print(res_df)
res_df.to_csv('search_term_2/datasets/google_results_table.csv',index=False)