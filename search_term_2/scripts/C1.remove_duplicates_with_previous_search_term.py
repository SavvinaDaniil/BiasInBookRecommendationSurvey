import os
os.system("clear")
import pandas as pd
merged_current = pd.read_csv('search_term_2/datasets/clean_merged_results.csv')

merged_previous = pd.read_csv('search_term_1/datasets/clean_merged_results.csv')


print(merged_current.columns, merged_previous.columns)
print(len(merged_current), len(merged_previous))
# scopus = scopus[google.columns]



previous_titles = merged_previous.Title.unique()
print(previous_titles)
print(len(merged_current[merged_current.Title.isin(previous_titles)]))

removed_duplicates = merged_current[merged_current.Title.isin(previous_titles)==False]
print(len(removed_duplicates))

removed_duplicates.to_csv('search_term_2/datasets/clean_merged_results_new.csv', index=False)
