
import json

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
import pickle
def evaluate():
    import json

    with open('data_processed/celeb_json.json', 'r') as f:
        data = json.load(f)

    data1 = pd.read_json('data_processed/celeb_json.json')
    # #print(data1)

    #
    sum_tweets_list = []
    for tweets in data1['tweets']:
        sum_tweet = ""
        for tweet in tweets:
            sum_tweet += tweet
        sum_tweets_list.append(sum_tweet)

    data1['tweets'] = pd.DataFrame(np.array(sum_tweets_list))
    # #print(data1)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data1['tweets'])
    feature_names = vectorizer.get_feature_names()
    #print(feature_names)
    dense = vectors.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names)

    df_with_tfidf = pd.concat([data1, df], axis=1)
    (XY_train, XY_test) = train_test_split(df_with_tfidf, test_size=.2, shuffle=False)
    # #print("train data\n",XY_train)
    # #print()
    # #print("test data\n", XY_test)
    # df_new = pd.DataFrame(columns=XY_test.columns)
    # for i in range(len(XY_test)):
    #     if (i%2 == 1):
    #         xxx = (XY_test.iloc[i-1] + df.iloc[i])/2
    #         df_new = df_new.append(xxx, ignore_index=True)
    #         # for j in range(len(df.iloc[0,:])):
    #         #     df.iloc[i-1]
    #
    # # df_new=df_new.div(2)
    # print("length",len(df_new))
    # # print(df_new)
    # XY_test = XY_test.append(df_new)

    # keys=[]
    # for i in df_new:
    #     keys.append(i)
    # print(keys)
    col = df.columns


    ##### #printing index of positive feature words##########
    with open('data_processed/features_list.txt', 'w') as f:
        for i in range(len(XY_test.columns)):
            strr = str(i) +" "+ str(XY_test.columns[i]) +"\n"
            f.write(strr)

    good_feature_columns = [300,349,
350 ,
351 ,
386 ,
391 ,
427 ,
428 ,
1623 ,
1629 ,
1630 ,
1660 ,
1661 ,
1740 ,
1741 ,
1742 ,
1743 ,
1744 ,
1745 ,
1746 ,
1845 ,
2353]
    max_feature_values = dict()
    for feature in good_feature_columns:
        #print(feature," ",max(XY_test.iloc[:,feature]),"\n")
        max_feature_values[feature] = max(XY_test.iloc[:,feature])




    training_data_path = "data_processed/train_data.json"
    test_data_path = "data_processed/test_data.json"
    # XY_train = XY_train.loc[:, ~df.columns.duplicated()].copy()
    # XY_test = XY_test.loc[:,~df.columns.duplicated()].copy()

    # #print(XY_train.columns)
    # for i in XY_train.columns:
    #     if i not in set(XY_train.columns):
    #         #print(i)
    # #print(len(list()) == len(XY_train))
    result = XY_train.to_json(training_data_path, orient='records')
    result = XY_test.to_json(test_data_path, orient='records')

    import wf_ml_training
    wf_ml_training.linear_regression()

    import wf_ml_prediction
    predictions_df = wf_ml_prediction.predict(max_feature_values)
    # #print(predictions_df[0])
    predictions_df = pd.DataFrame(predictions_df, columns=["linear","ridge","lasso","svm"])
    #print("****************")
    #print(np.array(predictions_df.iloc[:]["linear"]))
    #print("****************")

    #evaluation
    errors = []
    # feature_set = pd.concat([data1['wordcount'], data1['category'], data1.iloc[:, 9:]], axis=1)
    # #print(feature_set.columns)
    import json
    predictionsList = []
    with open('data_processed/test_data.json', 'r') as f:
        data1 = json.load(f)
    data1 = pd.read_json('data_processed/test_data.json')
    # feature_set = pd.concat([data1['wordcount'], data1['category'], data1.iloc[:,9:]], axis=1)

    output_openness = pd.concat([data1['openness']], axis=1).to_numpy()
    output_conscientiousness = pd.concat([data1['conscientiousness']], axis=1).to_numpy()
    output_extraversion = pd.concat([data1['extraversion']], axis=1).to_numpy()
    output_agreeableness = pd.concat([data1['agreeableness']], axis=1).to_numpy()
    output_neuroticism = pd.concat([data1['neuroticism']], axis=1).to_numpy()

    y_true = np.concatenate((output_openness, output_conscientiousness, output_extraversion, output_agreeableness, output_neuroticism))
    y_pred = np.concatenate((predictions_df.iloc[0]['linear'], predictions_df.iloc[1]['linear'],
                            predictions_df.iloc[2]['linear'], predictions_df.iloc[3]['linear'],
                            predictions_df.iloc[4]['linear']))
    from sklearn.metrics import mean_absolute_error

    # MAE
    error1 = mean_absolute_error(
        y_true=y_true,
        y_pred=y_pred
    )
    #print("LR_MAE: ", error1)

    # RMSE
    error2 = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
        squared=False
    )
    #print("LR_RMSE: ", error2)
    errors.append([error1, error2])
    y_pred = np.concatenate((predictions_df.iloc[0]['ridge'], predictions_df.iloc[1]['ridge'],
                             predictions_df.iloc[2]['ridge'], predictions_df.iloc[3]['ridge'],
                             predictions_df.iloc[4]['ridge']))
    # MAE
    error1 = mean_absolute_error(
        y_true=y_true,
        y_pred=y_pred
    )
    #print("RR_MAE: ", error1)

    # RMSE
    error2 = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
        squared=False
    )
    #print("RR_RMSE: ", error2)
    errors.append([error1, error2])
    y_pred = np.concatenate((predictions_df.iloc[0]['lasso'], predictions_df.iloc[1]['lasso'],
                             predictions_df.iloc[2]['lasso'], predictions_df.iloc[3]['lasso'],
                             predictions_df.iloc[4]['lasso']))
    # MAE
    error1 = mean_absolute_error(
        y_true=y_true,
        y_pred=y_pred
    )
    #print("LASSO_MAE: ", error1)

    # RMSE
    error2 = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
        squared=False
    )
    #print("LASSO_RMSE: ", error2)
    errors.append([error1, error2])

    y_pred = np.concatenate((predictions_df.iloc[0]['svm'], predictions_df.iloc[1]['svm'],
                             predictions_df.iloc[2]['svm'], predictions_df.iloc[3]['svm'],
                             predictions_df.iloc[4]['svm']))
    # MAE
    error1 = mean_absolute_error(
        y_true=y_true,
        y_pred=y_pred
    )
    #print("SVM_MAE: ", error1)

    # RMSE
    error2 = mean_squared_error(
        y_true=y_true,
        y_pred=y_pred,
        squared=False
    )
    #print("SVM_RMSE: ", error2)
    errors.append([error1, error2])
    #creating summary.txt

    errors_df = pd.DataFrame(errors, columns=["MAE","MSE"])
    #print(errors_df)


    summary_df = pd.DataFrame(np.array([["json_data.json", "Linear regression"],
                                        ["json_data.json", "Ridge regression"],
                                        ["json_data.json", "Lasso regression"],
                                        ["json_data.json", "SVM regression"]], dtype='object'),
                                        columns=["Dataset", "Method"])

    summary_df = pd.concat([summary_df, errors_df], axis=1)
    #print(summary_df)

    summary_path = "evaluation/summmary.txt"
    with open(summary_path, 'w+') as f:
        dfAsString = summary_df.to_string(header=True, index=True)
        f.write(dfAsString)



evaluate()


