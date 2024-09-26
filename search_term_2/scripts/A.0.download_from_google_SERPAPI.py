import os
os.system("clear")
from tqdm import tqdm
print('hi')
import pickle as pkl
import time

from serpapi import search


api_key = 'a5ee825eb1aba2d50b23d7557158188a40a04778140327849fc13f399b31efed'
search_term = '("book-crossing" OR "bookcrossing" OR "Librarything" OR "Amazon books" OR "Goodreads" OR "Goodbooks" )("bias") ("recommender")'

i=0
full_results = []
pbar = tqdm(total=1611)
while i<1611: # I saw this manually, to be fixed!
    params = {
    "engine": "google_scholar",
    "q": search_term,
    "api_key": api_key,
    "num":str(10),
    "start":str(i)
    }
    
    searchh = search(params)
    results = searchh.as_dict()
    partial_results = results["organic_results"]
    
    i+=10
    pbar.update(10)
    full_results.append(partial_results)
pbar.close()
with open('search_term_2/datasets/google_results.pkl', 'wb') as handle:
    pkl.dump(full_results, handle, protocol=pkl.HIGHEST_PROTOCOL)
    
    
# Break them in two!!!! 