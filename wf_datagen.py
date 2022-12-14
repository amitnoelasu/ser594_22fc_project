import csv

import numpy as np
import  pandas as pd
import json

import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
api_key = "X"
api_key_secret = "X"
bearer_token = "X"

# consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "X"
access_secret = "X"


# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(api_key, api_key_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    # 200 tweets to be extracted
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username)

    # Empty Array
    tmp = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created

    # open and read the file after the appending:
    f = open("tweets.txt", "a")

    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        byte_str = j.encode('utf-8')
        # f.write(newStr)
        # str_str = str(byte_str, encoding='utf-8')
        # print(byte_str)
        # break
        tmp.append(byte_str)

    f.close()
        # Printing the tweets
    # for tweet in tmp:
    #     print(tweet)
    # print()
    return tmp


# Driver code
if __name__ == '__main__':
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    filepath = "data_original/analisis.csv"
    df = pd.read_csv(filepath, encoding='utf-8', header=0)
    print(df.columns)
    # print(df)
    #adding real data point
    # "usuario","op","co","ex","ag","ne","wordcount","categoria"
    # df = df.append([df, pd.DataFrame(C)])
    npData = df.to_numpy()
    npData = np.vstack([npData, np.array(["Puplunar","84","55","52","84","81","0","1"])])
    # npData = np.append(npData, np.array(["usuario","op","co","ex","ag","ne","wordcount","categoria"]))
    handles = npData[:,0]
    print(npData[0])
    # print(handles)
    all_tweets = []
    for handle in handles:
        tweets_of_user = []
        try:
            tweets_of_user.append(get_tweets(handle))
        except:
            print("Exception with user:", handle)

        all_tweets.append(tweets_of_user)


    json_path = "data_original/json_data.json"

    modified_df = pd.DataFrame(npData)

    modified_df[8] = np.array(all_tweets, dtype='object')
    modified_df.columns = ['username', 'openness', 'conscientiousness', 'extraversion', 'agreeableness', 'neuroticism', 'wordcount', 'category', 'tweets']
    # modified_df.append(all_tweets)
    # print(modified_df)
    result = modified_df.to_json(json_path,orient='records')
    # parsed = json.loads(result)

    # print(all_tweets[0])
    # print(tweets)

