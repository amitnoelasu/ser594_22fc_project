#### SER594: Exploratory Data Munging and Visualization
#### Proprocessing and Visualizing user tweet data (title)
#### Amit Noel Thokala (author)
#### 23 Oct 2022(date)

## Basic Questions
**Dataset Author(s):** 
Μαριος Μιχαηλιδης KazAnova (Owner)

**Dataset Construction Date:** 
5 Years ago

**Dataset Record Count:** 
1.6 Million

**Dataset Field Meanings:** 

target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)

ids: The id of the tweet ( 2087)

date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)

flag: The query (lyx). If there is no query, then this value is NO_QUERY.

user: the user that tweeted (robotickilldozr)

text: the text of the tweet (Lyx is cool)

**Dataset File Hash(es):**  
DF952449D6F9B5F9FDFE3FC53DDEF7CA

## Interpretable Records
### Record 1
**Raw Data:** 
"0","1467812416","Mon Apr 06 22:20:16 PDT 2009","NO_QUERY","erinx3leannexo","spring break in plain city... it's snowing "

**Interpretation:** 
It is a negative tweet with tweet ID 1467812416, which was posted on Apr the 6th 2009 by user 'erinx3leannexo'. There was no special query used to retrieve this tweet. The user has tweeted "spring break in plain city... it's snowing "

### Record 2
**Raw Data:** 
"0","1467813137","Mon Apr 06 22:20:25 PDT 2009","NO_QUERY","armotley","about to file taxes "

**Interpretation:** 
It is a negative tweet with tweet ID 1467813137, which was posted in Apr the 6th 2009 by user "armotley".There was no special query used to retrieve this tweet. The user has tweeted "about to file taxes ".

## Data Sources
https://www.kaggle.com/datasets/kazanova/sentiment140?resource=download

### Transformation 1
**Description:** 
	Remove infrequent twitter users

**Soundness Justification:** Removing records of users who do not have at least 100 tweets, because too few tweets can lead to inconclusive results


### Transformation 2
**Description:** 
	Lower-case all words.

**Soundness Justification:** Converting all letters to lowercase prevents treating the same word as multiple words

### Transformation 3
**Description:** 
	Remove all URLs
        

**Soundness Justification:** URLs do not reflect any aspect of the user's personality, so it was removed

### Transformation 4
**Description:** 	
        
        Remove all @mentions
        
**Soundness Justification:** Mentions do not reflect any aspect of user's personality, so it was removed

### Transformation 5
**Description:** 

        Remove all punctuations.
        
**Soundness Justification:** Punctuations clutter the keyword set, so they were removed

### Transformation 6
**Description:** 

        Remove stopwords. (Stopwords are the lists in the nltk library that are trivial and not relevant to the context/text.)
        Perform lemmatization on the data.

**Soundness Justification:** Stopwords that are trivial and not relevant to the context/text were removed

### Transformation 7
**Description:** 

        Perform lemmatization on the data.

**Soundness Justification:** Converting all tenses of a word to a single tense for uniqueness 



## Visualization
### Visual 1 : Target vs Age
**Analysis:** Shows the scatterplot between the polarity of the tweet and the age of the tweet

### Visual 2 : Target vs Word count
**Analysis:** Shows the scatterplot between the polarity of the tweet and word count of the tweet

### Visual 3 : Word count vs Age
**Analysis:** Shows the scatterplot between the word count of the tweet and the age of the tweet

### Visual 4 : User Histogram
**Analysis:** Shows the most active users by their frequency(total number) of tweets in the dataset

### Visual 5 : Words Histogram
**Analysis:** Shows the most used words by their frequencey(total count) of usage in a tweet in the dataset
