import os
os.system("clear")
from tqdm import tqdm
import pickle as pkl
import pandas as pd


# Journal articles

art_df = pd.read_csv('search_term_2/springer_attempt/datasets/springer_articles.csv') 
relevant_columns = ['Item Title', 'Publication Title','URL', 'Authors', 'Publication Year', 'Content Type']
art_df = art_df[relevant_columns]
art_df.columns = ['Title', 'Venue','Link', 'Authors', 'Year', 'Type']
print(len(art_df))

# Conference papers

conf_df = pd.read_csv('search_term_2/springer_attempt/datasets/springer_conference_papers.csv') 
relevant_columns = ['Item Title', 'Publication Title','URL', 'Authors', 'Publication Year', 'Content Type']
conf_df = conf_df[relevant_columns]
conf_df.columns = ['Title', 'Venue','Link', 'Authors', 'Year', 'Type']
print(len(conf_df))

full_df = pd.concat([art_df, conf_df]).reset_index(drop=True)

venues_to_include = ['User Modeling and User-Adapted Interaction', 'Advances in Bias and Fairness in Information Retrieval', 'Advances in Information Retrieval', 'Data Mining and Knowledge Discovery']
print(len(full_df[full_df.Venue.isin(venues_to_include)].reset_index(drop=True)))


full_df[full_df.Venue.isin(venues_to_include)].reset_index(drop=True).to_csv('search_term_2/springer_attempt/datasets/springer_table.csv',index=False)
