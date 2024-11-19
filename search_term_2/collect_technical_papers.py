import os
os.system("clear")
import pandas as pd

# Let's find file per venue. First we start with the yes's. 

# Elsevier: there should be 5

elsevier = pd.read_csv('search_term_2/elsevier_attempt/datasets/first_screening_clean.csv') 
# print(len(elsevier)) # check
# print(elsevier.columns)


# IEEE: there should be 1

ieee = pd.read_csv('search_term_2/ieee_attempt/datasets/first_screening_clean.csv') 
# print(len(ieee)) # check
# print(ieee.columns)


# Springer: there should be 10

springer = pd.read_csv('search_term_2/springer_attempt/datasets/first_screening_clean.csv') 
# print(len(springer)) # check
# print(springer.columns)


# ACM: there should be 35. But in parts

# part 1: there should be 2. (these are the ones which were wrongly keeps)

acm_1 = pd.read_csv('search_term_2/acm_attempt/datasets/keeps_clean_yes.csv') 
# print(len(acm_1)) # check
# print(acm_1.columns)


# part 2: there should be 33. (these are the ones which were yes)

acm_2 = pd.read_csv('search_term_2/acm_attempt/datasets/second_screening_clean.csv') 
# print(len(acm_2)) # check
# print(acm_2.columns)


# Now we need to combine them.
dfs = [elsevier, ieee, springer, acm_1, acm_2]

final_df = pd.concat(dfs, ignore_index = True).fillna('missing')
final_df = final_df[['Title', 'Notes','Link','Venue','Year','Authors','Type', 'Abstract']]

# Save final df
final_df.to_csv('search_term_2/technical_papers.csv', index=False)
# print(final_df)



# Now we do the keeps.


# Elsevier: there should be 1

elsevier = pd.read_csv('search_term_2/elsevier_attempt/datasets/first_screening_clean_KEEPS.csv') 
# print(len(elsevier)) # check
# # print(elsevier.columns)


# IEEE: there should be 2

ieee = pd.read_csv('search_term_2/ieee_attempt/datasets/first_screening_clean_KEEPS.csv') 
# print(len(ieee)) # check
# print(ieee.columns)


# Springer: there should be 1

springer = pd.read_csv('search_term_2/springer_attempt/datasets/first_screening_clean_KEEPS.csv') 
# print(len(springer)) # check
# print(springer.columns)


# ACM: there should be 35. But in parts

# part 1: there should be 26. (these are the ones which were correctly keeps)

acm_1 = pd.read_csv('search_term_2/acm_attempt/datasets/keeps_clean_keeps.csv') 
# print(len(acm_1)) # check
# print(acm_1.columns)


# part 2: there should be 9. (these are the ones which were wrongly yes)

acm_2 = pd.read_csv('search_term_2/acm_attempt/datasets/second_screening_clean_KEEPS.csv') 
# print(len(acm_2)) # check
# print(acm_2.columns)


# # Now we need to combine them.
dfs = [elsevier, ieee, springer, acm_1, acm_2]

final_df = pd.concat(dfs, ignore_index = True).fillna('missing')
final_df = final_df[['Title', 'Notes','Link','Venue','Year','Authors','Type', 'Abstract']]

# Save final df
final_df.to_csv('search_term_2/technical_papers_KEEP.csv', index=False)
# print(final_df)
