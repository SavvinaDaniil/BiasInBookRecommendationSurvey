import os
os.system("clear")
print('hi')
from scholarly import scholarly, ProxyGenerator
print('hi')
import pickle as pkl


pg = ProxyGenerator() 
success = pg.FreeProxies()
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs('allintitle: (book OR books OR author OR authors OR library OR libraries) (recommend OR recommended OR recommending OR recommends OR recommendation OR recommendations OR recommender OR recommenders OR "artificial intelligence" OR AI OR "machine learning") (ethics OR ethical OR responsible OR bias OR fair OR diverse OR diversity OR diversification OR fairness OR gender OR sex OR nationality OR ethnicity OR race OR religion)')
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
while i<nr_results:
    current_result = next(search_query)
    
    info = current_result['bib']
    # print(info.keys())
    try:
        pub_url = current_result['pub_url']
        print(pub_url)
    except:
        pub_url = 'missing'
    
    i+=1
    print(i)
    all_results.append(current_result)

with open('google_results.pkl', 'wb') as handle:
    pkl.dump(all_results, handle, protocol=pickle.HIGHEST_PROTOCOL)