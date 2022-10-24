def visualize():
    # !/usr/bin/env python
    # coding: utf-8

    # In[84]:

    import pandas as pd
    from datetime import datetime
    df = pd.read_csv('out.csv', header=0)

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

    # In[96]:
    ans = ""
    ans += "Min of date : "+str(min(dat))
    print(min(dat))

    # In[97]:
    ans += "Max of date: "+str(max(dat))
    print(max(dat))

    # In[103]:

    # import numpy as np
    # print(np.median(dat))

    # In[104]:

    length = len(dat)

    # In[105]:

    median = dat[length // 2]
    ans += "Median of date: " + str(median)
    # In[106]:

    median

    # In[107]:

    targets = data[:, 1]

    # In[108]:

    targets

    # In[109]:

    min(targets)
    ans += "Min of targets: "+str(min(targets))
    # In[110]:

    max(targets)
    ans += "max of targets: " + str(max(targets))
    # In[113]:

    median = targets[len(targets) // 2]
    ans += "Median of targets: " + str(median)
    print(median)



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
    ans += "Min of counts: " + str(min(counts))
    min(counts)
    #print("abc")
    # In[120]:

    max(counts)
    ans += "max of counts: " + str(max(counts))
    # In[121]:
    import numpy as np
    np.median(counts)
    ans += "median of counts: " + str(np.median(counts))

    with open("summary.txt", "w+") as text_file:
        text_file.write(ans)
    # In[129]:

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
    print(key[0])
    # print(val[0])

    # least frequent word
    print(key[-1])
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
    # print(val[0])

    # least active user
    print(key[-1])
    # print(val[-1])

    # In[155]:

    # df.corr(numeric_only=False)

    # In[160]:

    from datetime import datetime

    # input datetime
    dt = datetime(2018, 10, 22, 0, 0)
    # epoch time
    epoch_time = datetime(1970, 1, 1)

    # subtract Datetime from epoch datetime
    delta = (dt - epoch_time)

    dat_in_sec = [(date - epoch_time).total_seconds() for date in dat]

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
    ax.set(title='Scatter Plot',
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

    plt.savefig('word_count_vs_age.png')

    # In[196]:

    fig, ax = plt.subplots()
    ax.set(title='Scatter Plot',
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

    plt.savefig('target_vs_word_count.png')

    # In[198]:

    fig, ax = plt.subplots()
    ax.set(title='Scatter Plot',
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

    plt.savefig('target_vs_age.png')

    # In[ ]:




