import os
os.system("clear")
from tqdm import tqdm
from RISparser import readris
import pickle as pkl
import pandas as pd

# Library trends 

filepath = 'search_term_3/LIS_venues/datasets/library_trends.ris'

entries_list = []
with open(filepath, 'r') as bibliography_file:
    entries = readris(bibliography_file)
    for entry in entries:
        entries_list.append(entry)

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for entry in entries_list:
    
    

    res_df.at[i, 'Title'] = entry['primary_title']
    
    res_df.at[i, 'Venue'] = entry['alternate_title3']
    res_df.at[i, 'Year'] = entry['year']
    try:
        res_df.at[i, 'Abstract'] = entry['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    res_df.at[i, 'Link'] = entry['url']
    res_df.at[i, 'Authors'] = entry['first_authors']
    i+=1

lib_trends_df = res_df.copy()



# Journal of Docu 1 

filepath = 'search_term_3/LIS_venues/datasets/journal_of_documentation_1.ris'

entries_list = []
with open(filepath, 'r') as bibliography_file:
    entries = readris(bibliography_file)
    for entry in entries:
        entries_list.append(entry)
print(entries_list[0].keys())

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for entry in entries_list:
    
    res_df.at[i, 'Title'] = entry['title']
    
    res_df.at[i, 'Venue'] = entry['secondary_title']
    res_df.at[i, 'Year'] = entry['year']
    
    try:
        res_df.at[i, 'Abstract'] = entry['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
        
    res_df.at[i, 'Link'] = entry['url']
    try:
        res_df.at[i, 'Authors'] = entry['authors']
    except:        
        res_df.at[i, 'Authors'] = 'missing'
        
    i+=1

jour_docu_1_df = res_df.copy()


# Journal of Docu 2

filepath = 'search_term_3/LIS_venues/datasets/journal_of_documentation_2.ris'

entries_list = []
with open(filepath, 'r') as bibliography_file:
    entries = readris(bibliography_file)
    for entry in entries:
        entries_list.append(entry)
print(entries_list[0].keys())

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for entry in entries_list:
    
    res_df.at[i, 'Title'] = entry['title']
    
    res_df.at[i, 'Venue'] = entry['secondary_title']
    res_df.at[i, 'Year'] = entry['year']
    
    try:
        res_df.at[i, 'Abstract'] = entry['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
        
    res_df.at[i, 'Link'] = entry['url']
    try:
        res_df.at[i, 'Authors'] = entry['authors']
    except:        
        res_df.at[i, 'Authors'] = 'missing'
        
    i+=1

jour_docu_2_df = res_df.copy()





final_file = pd.concat([lib_trends_df, jour_docu_1_df, jour_docu_2_df], ignore_index=True)
print(len(final_file))
print(final_file)
final_file.to_csv('search_term_3/LIS_venues/datasets/RIS_table.csv',index=False)
