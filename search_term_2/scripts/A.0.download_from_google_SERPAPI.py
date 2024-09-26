import os
os.system("clear")
from tqdm import tqdm
print('hi')
import pickle as pkl
import time

from serpapi import search


api_key = 'e3ac379eb8bd81de4f791693d487b41cd075c29feaa8cd7ceb49b860ed8fc264'
search_term = '("book-crossing" OR "bookcrossing" OR "Librarything" OR "Amazon books" OR "Goodreads" OR "Goodbooks" )("bias") ("recommender")'

i=990
full_results = []
pbar = tqdm(total=1611, initial = 990)
while i<1611: # I saw this manually, to be fixed!
    params = {
    "engine": "google_scholar",
    "q": search_term,
    "api_key": api_key,
    "num":str(20),
    "start":str(i)
    }
    
    searchh = search(params)
    results = searchh.as_dict()
    try:
        
        partial_results = results["organic_results"]
    except:
        partial_results = ['']
    
    i+=20
    pbar.update(20)
    full_results.append(partial_results)
    if i%100==0:
        with open('search_term_2/datasets/google_results_2.pkl', 'wb') as handle:
            pkl.dump(full_results, handle, protocol=pkl.HIGHEST_PROTOCOL)

with open('search_term_2/datasets/google_results_2.pkl', 'wb') as handle:
    pkl.dump(full_results, handle, protocol=pkl.HIGHEST_PROTOCOL)
    
pbar.close()    