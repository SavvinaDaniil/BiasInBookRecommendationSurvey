import os
os.system("clear")
from tqdm import tqdm
from pybtex.database.input import bibtex
import pickle as pkl
import pandas as pd

# Short papers

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_2/acm_attempt/datasets/acm_short.bib")

res_df = pd.DataFrame(columns = ['Title','Authors','Link','Abstract','Venue', 'Year', 'Type'])
i=0
print(len(bibdata.entries))
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    a = bibdata.entries[bib_id].persons["author"]

    res_df.at[i, 'Title'] = b['title']
    
    res_df.at[i, 'Venue'] = b['booktitle']
    res_df.at[i, 'Year'] = b['year']
    res_df.at[i, 'Abstract'] = b['abstract']
    res_df.at[i, 'Link'] = b['url']
    author_list = []
    for author in a:
        fn = " ".join(author.first_names)
        ln = " ".join(author.last_names)
        final = " ".join([fn,ln])
        author_list.append(final)
    res_df.at[i, 'Authors'] = author_list
    i+=1
res_df['Type'] = 'Short'
short_df = res_df.copy()

# Research articles

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_2/acm_attempt/datasets/acm_research.bib")

res_df = pd.DataFrame(columns = ['Title','Authors','Link','Abstract','Venue', 'Year', 'Type'])
i=0
print(len(bibdata.entries))
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    a = bibdata.entries[bib_id].persons["author"]

    res_df.at[i, 'Title'] = b['title']
    try:
        res_df.at[i, 'Venue'] = b['booktitle']
    except:
        res_df.at[i, 'Venue'] = 'missing'
    res_df.at[i, 'Year'] = b['year']
    res_df.at[i, 'Abstract'] = b['abstract']
    try:
        res_df.at[i, 'Link'] = b['url']
    except:
        res_df.at[i, 'Link'] = 'missing'
    author_list = []
    for author in a:
        fn = " ".join(author.first_names)
        ln = " ".join(author.last_names)
        final = " ".join([fn,ln])
        author_list.append(final)
    res_df.at[i, 'Authors'] = author_list
    i+=1
res_df['Type'] = 'Research'
long_df = res_df.copy()

final_file = pd.concat([short_df, long_df], ignore_index=True)
final_file.to_csv('search_term_2/acm_attempt/datasets/acm_table.csv',index=False)
