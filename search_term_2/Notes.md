# Search term 2

We look for incidental studies.
("book-crossing" OR "bookcrossing" OR "Librarything" OR "Amazon books" OR "Goodreads" OR "Goodbooks" )("bias") ("recommender") 
## Thursday, 26 September 2024

### Start
Let’s start with searches.

Google scholar

1610 results. Download issue, work on it!


## Thursday, 03 October 2024

### Processing
Now we start processing

Google scholar

Managed to download 899 results.

Scopus

60 results. Downloaded into table

Let’s process them.

Merged table. 959 TOTAL. 37 duplicates. 940 left.


Remove duplicates with the previous search term: 9 of them we already have, so 931 left.
### Screening
Screening starts! First screen only Title and Abstract.

What is relevant:  Bias means BIAS, not bias parameter in algorithms. Not theses. Studying these actual datasets. Not surveys.


OMG it's such a terrible thing to be doing. Ill try something different:
- Take the bias and debias paper, look for the book datasets in the paper they cite.
    - 227 papers, exported by scopus.
- Do the search term 2 only from 2022 onwards.



<span style="color:blue">Tomorrow</span>
-

## Wednesday, 09 October 2024
Continue with the initial screening...

No! New idea. Search only in top conferences and journals related to RS. List:
- [ ] WWW ACM
- [ ] WSDM ACM
- [ ] SIGIR ACM
- [ ] RecSys ACM 
- [ ] TOIS ACM


- [ ] UMAP ACM
- [ ] (ECIR)
- [ ] TORS ACM
- [ ] Frontiers in Big Data|Recommender Systems

Searched term from this file in ACM. 366 results. 259 research articles. 34 short papers. -> 293.\
Includes the following: RecSys, CIKM, WWW, SIGIR, KDD, WSDM, UMAP, CHI, etc.



## Tuesday, 29 October 2024
Screen these 293 papers. Idea discussed with Laura: Yes for papers that specifically are looking into bias, No for irrelevant, Keep for some incidental so we might include them!
Let's fucking do it.


## Monday, 4 November 2024
Actually do the fucking thing mentioned above.\
Goals for this week:
- [ ] Screen these ACM papers
- [ ] Check citations of the relevant papers
- [ ] Find other relevant venues: ECIR,...
- [ ] Look for LIS venues \
I put everything in Notion\
I am 'keeping' some surveys. How do I search generally: click the link, search the word bias, see if it's relevant, then scheme through the abstract.

Look at information retrieval journal, see: Alejandro Bellogín, Pablo Castells, and Iván Cantador. 2017. Statistical biases in information retrieval metrics for
recommender systems

Maybe generally springer nature?

## Tuesday, 5 November 2024
Continue the previous task.

Unrelated: bias as in user/item bias in RS, bias in they way they decided some study, inductive bias, some algorithms are called 'biased something', not about RS, not using the datasets (but only referencing them in related work)\
Keep: not targeted work on uncovering or mitigating bias but incidental results, something interesting about book search/recommendation,


*Result*: 293 screened, 45 Yes, 202 no, 46 keep.\
No duplicates.

All of them are retrievable (they are from ACM library).
So I'll check eligibility.

To do that I'll make notes on each Yes paper.

Before doing the above: Make list of venues to look for papers.

LIS:\
From Emil's email!
1. <del>​Library Quarterly (JSTOR)
2. Journal of Documentation (Emerald insight)
3. <del>​Cataloging & Classification Quarterly (tandfonline)
4. Library Trends (John hopkins) **FOUND IT**
5. <del>​Collection Management (tandfonline)
6. Journal of the Association for Information Science & Technology (JASIST) (wiley) **Seems to be not only LIS**

Laura's:
7. Digital humanities conference
8. Digital humanities quarterly (journal)



Other:
1. ECIR (Springer nature) NOT UNIFIED!
2. Frontiers in Big Data|Recommender Systems (nothing I think)
4. Advances in Bias and Fairness in Information Retrieval (Springer nature)
5. <del>Transforming digital worlds (Springer nature)
6. Information Processing & Management (elsevier) !!
7. User Modeling and User-Adapted Interaction (Sprigner nature)
8. Transactions on Knowledge and data engineering (IEEE)
9. Data mining and knowledge discovery (springer)



## Wednesday, 6 November 2024
To-do: 
- Finish notes on every 'yes' in eligibility checked.
- Look at citations of every yes.
- Do notes on every 'keep'.

What am I doing: Going through every paper, note what they're doing, look at citations and see if they're citing non-acm papers. (See other above.)

Clear criterion: Papers that either measure or attempt to mitigate some form of bias in recommender systems, and try their method (of measurement or mitigation) on a book dataset.

Result!! Out of 45 yes's, now I have 33 yes's + 9 keeps + 3 no's\
I made notes and looked at citations. My conclusion: include springer nature, elsevier, ieee. repeat with the same term.

To-do:
- Repeat everything for springer nature, elsevier, ieee.
- Look at keeps! (maybe that later).

Idea: look only at springer nature places where youve found relevant work.

Other:
1. ECIR (Springer nature)
2. Frontiers in Big Data|Recommender Systems (nothing I think)
3. PeerJ computer science?
4. Advances in Bias and Fairness in Information Retrieval (Springer nature)
5. Transforming digital worlds (Springer nature) (probably not actually)
6. Information Processing & Management (elsevier) !! *17*
7. User Modeling and User-Adapted Interaction (Sprigner nature)
8. Transactions on Knowledge and data engineering (IEEE)
9. Data mining and knowledge discovery (springer)



springer: 86 confernece papers, 89 articles


Let's start with the 17 from elsevier's info processing and management! 5 yes, 1 Keep, 11 no

Let's do ieee tkde! 21 papers. 1 yes, 18 no, 2 keep

Let's do springer nature. 


## Thursday, 7 November 2024

For the LIS vnues, do: "bias" and "recommender" and see. 

Let's do springer nature. Filter in only the interesting venues: Advances in Bias and Fairness in Information Retrieval, Transforming digital worlds, User Modeling and User-Adapted Interaction, Data mining and knowledge discovery

116 springer articles, 115 springer conference papers.

Springer_list = ['User Modeling and User-Adapted Interaction', 'Advances in Bias and Fairness in Information Retrieval', 'Advances in Information Retrieval', 'Data Mining and Knowledge Discovery']

26 papers and articles after the above filtering. Let's check relevance.
10 relevant, 15 irrelevant,  1 keep

I finished with this line of work!!!!!


# Final from this search term

| Venue       | Total number| Yes number  | Keep number |
| ----------- | ----------- | ----------- | ----------- |
| ACM         | 293         | 35          | 35 **(updated)**|
| Info processing & management (elsevier)   | 17        | 5      | 1       |
| TKDE (IEEE)   | 21        | 1      | 2       |
| Springer_list (Springer)   | 26        | 10      |    1    |
| ----------- | ----------- | ----------- | ----------- |
| All venues | 257 | 51  | 39 |


To-do:
- [ ] Check the keeps of ACM. Reconsider, make notes.
- [ ] Put all of the technical 'Yes''s together. 
- [ ] Start going through the library venues. Look for: 'bias', 'recommender'


search term 3: ("recommender system" OR "recommendation system" OR "recommendation systems" OR "recommender systems" OR "artificial intelligence" OR "AI") (bias OR diversity OR diverse) *library quarterly*

MAYBE: ("book" OR "books" OR "library" OR "libraries") AND ("recommender system" OR "recommendation system" OR "recommendation systems" OR "recommender systems" OR "artificial intelligence" OR "AI") AND (bias OR diversity OR diverse) *cataloguing quarterly from 2010*, *collection management after 2010*, 


## Monday, 18 November 2024

Ok I am back to this. To-dos from earlier.

To-do:
- [ ] Check the keeps of ACM. Reconsider, make notes.
- [ ] Put all of the technical 'Yes''s together. 

Start with the firs. Look at the file: eligibility checked for Keeps, and make notes there.

## Tuesday, 19 November 2024

To-do:
- [x] Check the keeps of ACM (eligibility checked for Keeps). Reconsider, make notes.
- [x] Put all of the technical 'Yes''s together.
- [x] Put all of the technical 'Keep''s together.

Decision: Don't keep them if they dont measure some sort of bias at the end. 

Some papers about: improving long-tail item recommendation for cold start problems. Also, don't keep the ones that are about diversification and there's nothing really about bias...

If there was a conference first and a journal later, I keep journal.

Reasons to keep: coincidental study of bias, or something interesting about books.

From 46 keeps: 26 keeps, 2 yes, 2 library.

**Result**: | All venues | 257 | 51  | 39 |

To-do for updated Keeps:
- [x] Put yes's into their own file
- [x] Update to only include keeps in a new file
- [x] Keep libraries in their own file

Now let's collect all technical yes's! DONE! Both yes and keeps. 51 yes, 39 keep!!! Woo hooooooooo

I will follow up tomorrow with the following:

Format for analysis:
1. Book data used
2. Problem: which bias? On which side?
3. Solution: pre in post?
4. Results on the book dataset?


## Wednesday, 20 November 2024

I am transferring the technical papers on notion.

## Wednesday, 27 November 2024

Other things to keep track of: defintions about bias and fairness, preprocessing (filtering) of the datasets, was there hyperparameter tuning, framework used, is it social or statistical bias, are they reproducible!

**Problem**: I just noticed an issue: double spaced title of conference made me miss a paper from springer. FIX!