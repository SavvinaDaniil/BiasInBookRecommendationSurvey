import os
os.system("clear")
from tqdm import tqdm
from pybtex.database.input import bibtex
import pickle as pkl
import pandas as pd

# Library Quarterly

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_3/LIS_venues/datasets/library_quarterly.bib")
print(len(bibdata.entries))
# print(bibdata.entries)

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    

    res_df.at[i, 'Title'] = b['title']
    
    res_df.at[i, 'Venue'] = b['journal']
    res_df.at[i, 'Year'] = b['year']
    try:
        res_df.at[i, 'Abstract'] = b['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    res_df.at[i, 'Link'] = b['URL']
    try:
        a = bibdata.entries[bib_id].persons["author"]
        author_list = []
        for author in a:
            fn = " ".join(author.first_names)
            ln = " ".join(author.last_names)
            final = " ".join([fn,ln])
            author_list.append(final)
        res_df.at[i, 'Authors'] = author_list
    except:
        res_df.at[i, 'Authors'] = 'missing'
    i+=1

lq_df = res_df.copy()
# print(lq_df)


# Cataloguing and Classification 1 TO FIX

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_3/LIS_venues/datasets/cataloguing_classification_1.bib")
print(len(bibdata.entries))
# print(bibdata.entries)

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    

    res_df.at[i, 'Title'] = b['title']
    
    res_df.at[i, 'Venue'] = b['journal']
    res_df.at[i, 'Year'] = b['year']
    try:
        res_df.at[i, 'Abstract'] = b['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    res_df.at[i, 'Link'] = b['URL']
    try:
        a = bibdata.entries[bib_id].persons["author"]
        author_list = []
        for author in a:
            fn = " ".join(author.first_names)
            ln = " ".join(author.last_names)
            final = " ".join([fn,ln])
            author_list.append(final)
        res_df.at[i, 'Authors'] = author_list
    except:
        res_df.at[i, 'Authors'] = 'missing'
    i+=1

cc_1_df = res_df.copy()
# print(cc_1_df)


# Cataloguing and Classification 2 

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_3/LIS_venues/datasets/cataloguing_classification_2.bib")
print(len(bibdata.entries))
# print(bibdata.entries)

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    

    res_df.at[i, 'Title'] = b['title']
    
    res_df.at[i, 'Venue'] = b['journal']
    res_df.at[i, 'Year'] = b['year']
    try:
        res_df.at[i, 'Abstract'] = b['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    res_df.at[i, 'Link'] = b['URL']
    try:
        a = bibdata.entries[bib_id].persons["author"]
        author_list = []
        for author in a:
            fn = " ".join(author.first_names)
            ln = " ".join(author.last_names)
            final = " ".join([fn,ln])
            author_list.append(final)
        res_df.at[i, 'Authors'] = author_list
    except:
        res_df.at[i, 'Authors'] = 'missing'
    i+=1

cc_2_df = res_df.copy()


# Collection management 

parser = bibtex.Parser()
bibdata = parser.parse_file("search_term_3/LIS_venues/datasets/collection_management.bib")
print(len(bibdata.entries))
# print(bibdata.entries)

res_df = pd.DataFrame(columns = ['Title','Link','Authors','Abstract','Venue', 'Year'])
i=0
for bib_id in bibdata.entries:
    b = bibdata.entries[bib_id].fields
    

    res_df.at[i, 'Title'] = b['title']
    
    res_df.at[i, 'Venue'] = b['journal']
    res_df.at[i, 'Year'] = b['year']
    try:
        res_df.at[i, 'Abstract'] = b['abstract']
    except:
        res_df.at[i, 'Abstract'] = 'missing'
    res_df.at[i, 'Link'] = b['URL']
    try:
        a = bibdata.entries[bib_id].persons["author"]
        author_list = []
        for author in a:
            fn = " ".join(author.first_names)
            ln = " ".join(author.last_names)
            final = " ".join([fn,ln])
            author_list.append(final)
        res_df.at[i, 'Authors'] = author_list
    except:
        res_df.at[i, 'Authors'] = 'missing'
    i+=1

col_man_df = res_df.copy()
# print(col_man_df)

final_file = pd.concat([lq_df, cc_1_df, cc_2_df, col_man_df], ignore_index=True)
print(len(final_file))
print(final_file)
final_file.to_csv('search_term_3/LIS_venues/datasets/BIB_table.csv',index=False)
