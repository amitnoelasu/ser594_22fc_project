import numpy as np


def visualize():
    # !/usr/bin/env python
    # coding: utf-8

    # In[84]:

    import pandas as pd
    from datetime import datetime
    df = pd.read_csv('data_processed/out.csv', header=0)

    # In[85]:

    df

    # In[86]:

    data = df.to_numpy()

    # In[87]:

    data

    # In[88]:

    # date
    date = data[:, 2]

    # In[89]:

    date

    # In[90]:

    dates = [a.split(" ") for a in date]

    # In[91]:

    dates

    # In[92]:

    date_s = [s[1]+"/"+s[5] for s in dates]

    # In[93]:

    

    # In[94]:

    dat = [datetime.strptime(d, '%b/%Y') for d in date_s]

    # In[95]:

    dat

    # datetime(year, month, day, hour, minute, second, microsecond)
    monthslist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    new_dates = []
    for s in dates:
        timedata = s[3].split(":")
        b = datetime(int(s[5]), monthslist.index(s[1]) + 1, int(s[2]), int(timedata[0]), int(timedata[1]),
                     int(timedata[2]))
        new_dates.append(b)



    # In[96]:
    ans = ""
    ans += "Min of date : "+str(min(new_dates))+"\n"
    # print(min(dat))

    # In[97]:
    ans += "Max of date: "+str(max(new_dates))+"\n"
    # print(max(dat))

    # In[103]:

    # import numpy as np
    # print(np.median(dat))

    # In[104]:

    length = len(dat)

    # In[105]:

    median = new_dates[length // 2]
    ans += "Median of date: " + str(median)+"\n"
    # In[106]:

    median

    # In[107]:

    targets = data[:, 1]

    # In[108]:

    targets

    # In[109]:

    min(targets)
    ans += "Min of targets: "+str(min(targets))+"\n"
    # In[110]:

    max(targets)
    ans += "max of targets: " + str(max(targets))+"\n"
    # In[113]:

    median = targets[len(targets) // 2]
    ans += "Median of targets: " + str(median)+"\n"
    # print(median)



    # In[114]:

    texts = data[:, 4]
    texts

    # In[117]:

    counts = []
    for text in texts:
        counts.append(len(str(text).split(" ")))

    # In[118]:

    counts

    # In[119]:
    ans += "Min of word count in tweets: " + str(min(counts))+"\n"
    min(counts)
    #print("abc")
    # In[120]:

    max(counts)
    ans += "max of word count in tweets: " + str(max(counts))+"\n"
    # In[121]:
    import numpy as np
    np.median(counts)
    ans += "median of word count in tweets: " + str(np.median(counts))+"\n"

    

    wordset = dict()
    for text in texts:
        wordList = str(text).split(" ")
        for w in wordList:
            if w in wordset:
                wordset[w] = wordset[w] + 1
            else:
                wordset[w] = 1

    # In[130]:

    wordset

    # In[139]:

    sortedwordset = {k: v for k, v in sorted(wordset.items(), key=lambda item: item[1], reverse=True)}
    sortedwordset

    # In[143]:

    key = []
    val = []
    for k, v in sortedwordset.items():
        key.append(k)
        val.append(v)
    # most frequent word
    ans += "most frequent word: " + str(key[0]) + "\n"
    # print(key[0])
    # print(val[0])

    # least frequent word
    ans += "least frequent word: " + str(key[-1]) + "\n"
    # print(key[-1])
    # print(val[-1])

    # In[144]:

    # val

    # In[145]:

    # val.sort()

    # In[148]:

    users = data[:, 3]
    userset = dict()
    for w in users:

        if w in userset:
            userset[w] = userset[w] + 1
        else:
            userset[w] = 1

    # In[149]:

    userset

    # In[150]:

    sorteduserset = {k: v for k, v in sorted(userset.items(), key=lambda item: item[1], reverse=True)}
    sorteduserset

    # In[152]:

    key = []
    val = []
    for k, v in sorteduserset.items():
        key.append(k)
        val.append(v)
    # most active user
    print(key[0])
    ans += "most active user: " + str(key[0]) + "\n"
    # print(val[0])

    # least active user
    print(key[-1])
    ans += "least active user: " + str(key[-1]) + "\n"
    # print(val[-1])

    # In[155]:

    # df.corr(numeric_only=False)

    # In[160]:
    
    with open("./data_processed/summary.txt", "w+") as text_file:
        text_file.write(ans)
    # In[129]:

    from datetime import datetime

    # input datetime
    dt = datetime(2018, 10, 22, 0, 0)
    # epoch time
    epoch_time = datetime(1970, 1, 1)

    # subtract Datetime from epoch datetime
    delta = (dt - epoch_time)

    dat_in_sec = [(date - epoch_time).total_seconds() for date in dat]
    dat_in_sec = [(date-epoch_time).total_seconds() for date in new_dates]

    # In[161]:

    dat_in_sec

    # In[164]:

    tarray = [dat_in_sec, counts, targets]

    # In[165]:

    x = np.array(tarray)

    # In[166]:

    y = np.transpose(x)

    # In[173]:

    y = y.astype(int)

    # In[174]:

    quant_data = pd.DataFrame(data=y, columns=["date", "word_count", "target"])

    # In[186]:

    z = quant_data.corr()
    writePath = "./data_processed/correlations.txt"
    #
    # for index, row in z.iterrows():
    #     print(index)
    #     print(row)
    with open(writePath, 'w+') as f:
        dfAsString = z.to_string(header=True, index=True)
        f.write(dfAsString)

    print(z)

    # In[178]:

    type(z)

    # In[189]:

    # f = open(r'data_processed\correlations.txt', "x")
    # f.close()
    # np.savetxt(f, z.values.astype(int))

    # In[195]:

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set(title='age vs word count',
           ylabel='word count', xlabel='age of the tweet(days)')

    xx = y[:, 0] / 86400
    # print(max(xx))
    # print(len(xx))

    yy = y[:, 1]

    # print(max(yy))
    # print(len(yy))

    #     ax.ticklabel_format(useOffset=False, style='plain')
    ax.scatter(xx, yy)
    fig.set_dpi(800)

    plt.savefig('visuals/word_count_vs_age.png')

    # In[196]:

    fig, ax = plt.subplots()
    ax.set(title='target vs word count',
           xlabel='word count', ylabel='target(polarity of the tweet)')

    xx = y[:, 1]
    # print(max(xx))
    # print(len(xx))

    yy = y[:, 2]

    # print(max(yy))
    # print(len(yy))

    #     ax.ticklabel_format(useOffset=False, style='plain')
    ax.scatter(xx, yy)
    fig.set_dpi(800)

    plt.savefig('visuals/target_vs_word_count.png')

    # In[198]:

    fig, ax = plt.subplots()
    ax.set(title='target vs age',
           xlabel='age of the tweet(days)', ylabel='target(polarity of the tweet)')

    xx = y[:, 0] / 86400
    # print(max(xx))
    # print(len(xx))

    yy = y[:, 2]

    # print(max(yy))
    # print(len(yy))

    #     ax.ticklabel_format(useOffset=False, style='plain')
    ax.scatter(xx, yy)
    fig.set_dpi(800)



    plt.savefig('visuals/target_vs_age.png')

    fig, ax = plt.subplots()
    ax.set(title="Histogram - Most used words", xlabel="Word in tweet", ylabel="Frequency")
    wordsList = []
    texts = data[:,4]

    mostFreqWords = set()
    c = 0
    for k, v in sortedwordset.items():
        if (c == 10):
            break
        mostFreqWords.add(k)
        c += 1

    for text in texts:
        for w in str(text).split(" "):
            if w in mostFreqWords:
                wordsList.append(w)

    # print(mostFreqWords)
    # print(wordsList)
    ax.hist(wordsList, density=False)
    fig.set_dpi(800)
    plt.savefig('visuals/words_histogram.png')

    fig, ax = plt.subplots()
    ax.set(title="Histogram - Most active users", xlabel="Username", ylabel="Frequency")
    userslist = []
    users = data[:, 3]

    mostactiveuser = set()
    c = 0
    for k, v in sorteduserset.items():
        if (c == 5):
            break
        mostactiveuser.add(k)
        c += 1
    # print(mostactiveuser)
    for user in users:
        if user in mostactiveuser:
            userslist.append(user)

    # print(userslist)
    # print(wordsList)
    ax.hist(userslist, density=False)
    fig.set_dpi(800)
    plt.savefig('visuals/user_histogram.png')


def visualize1():
    import json
    import pandas as pd
    import matplotlib.pyplot as plt

    with open('data_processed/celeb_json.json', 'r') as f:
        data = json.load(f)

    data1 = pd.read_json('data_processed/celeb_json.json')

    openness = -1
    conscientiousness = -1
    extraversion = -1

    dat = data1['openness']
    dat = dat.to_numpy()
    # mean =
    print(np.mean(dat))
    print(np.median(dat))
    print(np.min(dat))
    print(np.max(dat))

    dat = data1['conscientiousness']
    dat = dat.to_numpy()
    # mean =
    print(np.mean(dat))
    print(np.median(dat))
    print(np.min(dat))
    print(np.max(dat))
    # #print(data1)

    dat = data1['neuroticism']
    dat = dat.to_numpy()
    # mean =
    print(np.mean(dat))
    print(np.median(dat))
    print(np.min(dat))
    print(np.max(dat))
    #

    fig, ax = plt.subplots()
    ax.set(title="Histogram - openness", xlabel="openness", ylabel="Frequency")

    ax.hist(dat, density=False)
    fig.set_dpi(800)
    plt.savefig('visuals/op_histogram.png')

    fig, ax = plt.subplots()
    ax.set(title="Histogram - conscientiousness", xlabel="conscientiousness", ylabel="Frequency")

    ax.hist(data1['conscientiousness'].to_numpy(), density=False)
    fig.set_dpi(800)
    plt.savefig('visuals/co_histogram.png')

    fig, ax = plt.subplots()
    ax.set(title="Histogram - Extraversion", xlabel="Extraversion", ylabel="Frequency")

    ax.hist(data1['extraversion'].to_numpy(), density=False)
    fig.set_dpi(800)
    plt.savefig('visuals/ex_histogram.png')




    # In[ ]:
# visualize()
visualize1()




