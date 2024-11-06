import os
os.system("clear")
from tqdm import tqdm
from pybtex.database.input import bibtex
import pickle as pkl
import pandas as pd


# Research articles

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_2/ieee_attempt/datasets/IEEE_tkde.bib")

res_df = pd.DataFrame(columns = ['Title','Authors','Link','Abstract','Venue', 'Year'])
i=0
# print(bibdata.entries)
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    a = bibdata.entries[bib_id].persons["author"]

    res_df.at[i, 'Title'] = b['title']
    try:
        res_df.at[i, 'Venue'] = b['journal']
    except:
        res_df.at[i, 'Venue'] = 'missing'
    res_df.at[i, 'Year'] = b['year']
    try:
        res_df.at[i, 'Abstract'] = b['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    try:
        res_df.at[i, 'Link'] = b['doi']
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


print(res_df)
res_df.to_csv('search_term_2/ieee_attempt/datasets/ieee_table.csv',index=False)
