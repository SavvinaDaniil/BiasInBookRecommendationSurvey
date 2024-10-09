import os
os.system("clear")
from tqdm import tqdm
print('hi')
from scholarly import scholarly, ProxyGenerator
print('hi')
import pickle as pkl
import time

pg = ProxyGenerator() 
success = pg.FreeProxies()
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs('("book-crossing" OR "bookcrossing" OR "Librarything" OR "Amazon books" OR "Goodreads" OR "Goodbooks" )("bias") ("recommender")')
print('hi')

print(search_query)
# scholarly.pprint(next(search_query))

nr_results = search_query.total_results
# pub_parser = search_query.pub_parser

print(nr_results)
# print(pub_parser.bibtex)
# print(help(pub_parser))
i = 0
all_results = []
pbar = tqdm(total=nr_results)
while i<nr_results:
    current_result = next(search_query)
    
    info = current_result['bib']
    # print(info.keys())
    try:
        pub_url = current_result['pub_url']
        # print(pub_url)
    except:
        pub_url = 'missing'
    pbar.update(1)
    i+=1
    if i%100==0:
        with open('search_term_2/datasets/google_results.pkl', 'wb') as handle:
            pkl.dump(all_results, handle, protocol=pkl.HIGHEST_PROTOCOL)
        time.sleep(20) # hopefully it won't crash
        print('time passed')
    all_results.append(current_result)
pbar.close()

with open('search_term_2/datasets/google_results.pkl', 'wb') as handle:
    pkl.dump(all_results, handle, protocol=pkl.HIGHEST_PROTOCOL)