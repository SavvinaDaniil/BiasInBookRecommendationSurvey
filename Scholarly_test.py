import os
os.system("clear")
from scholarly import scholarly

search_query = scholarly.search_pubs('allintitle: (book OR books OR author OR authors OR library OR libraries) (recommend OR recommended OR recommending OR recommends OR recommendation OR recommendations OR recommender OR recommenders OR "artificial intelligence" OR AI OR "machine learning") (ethics OR ethical OR responsible OR bias OR fair OR diverse OR diversity OR diversification OR fairness OR gender OR sex OR nationality OR ethnicity OR race OR religion)')
print(search_query)
# scholarly.pprint(next(search_query))

nr_results = search_query.total_results
pub_parser = search_query.pub_parser

print(nr_results)
# print(pub_parser.bibtex)
# print(help(pub_parser))
i = 0
while i<nr_results:
    result = next(search_query)['bib']
    print(result)
    i+=1