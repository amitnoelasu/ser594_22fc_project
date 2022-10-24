# Processing tweets for personality trait extraction and their visualization
Author: Amit Noel Thokala
Date: Oct 23 2022


1. 
1.1. Author of the dataset: Μαριος Μιχαηλιδης KazAnova (Owner)
1.2. Meaning of the fields:

target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)

ids: The id of the tweet ( 2087)

date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)

flag: The query (lyx). If there is no query, then this value is NO_QUERY.

user: the user that tweeted (robotickilldozr)

text: the text of the tweet (Lyx is cool)

2. 

0	1467811372	Mon Apr 06 22:20:00 PDT 2009	NO_QUERY	joy_wolf	@Kwesidei not the whole crew 
0	1467811592	Mon Apr 06 22:20:03 PDT 2009	NO_QUERY	mybirch	Need a hug 

The data represents the tweet of a person that was posted on a particular day at a partiuclar time. It is reasonable
because it was obtained from the dataset which was created usin twitter API and the text field(last column) of the data
encapsulates the words said(posted) by the person which is derived from their personality traits. Hence it represents their personality.


4. Data source:
https://www.kaggle.com/datasets/kazanova/sentiment140?resource=download

