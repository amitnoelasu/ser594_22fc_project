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

def predict(max_feature_values):
    import json
    predictionsList = []
    with open('data_processed/test_data.json', 'r') as f:
        data1 = json.load(f)

    data1 = pd.read_json('data_processed/test_data.json')
    feature_set = pd.concat([data1['wordcount'], data1['category'], data1.iloc[:, 9:]], axis=1)
    # ###print(feature_set.columns)
    feature_set = feature_set.to_numpy()
    output_openness = pd.concat([data1['openness']], axis=1).to_numpy()
    output_conscientiousness = pd.concat([data1['conscientiousness']], axis=1).to_numpy()
    output_extraversion = pd.concat([data1['extraversion']], axis=1).to_numpy()
    output_agreeableness = pd.concat([data1['agreeableness']], axis=1).to_numpy()
    output_neuroticism = pd.concat([data1['neuroticism']], axis=1).to_numpy()
    #################################################################
    # A_varied = feature_set[0]
     #print()
    # A_varied[0] = 0
    # lis = []
    # for j in range(10):
    #     row = []
    #     for i in range(len(A_varied)):
    #         row.append(A_varied[i])
    #     lis.append(row)
    #
    # count = 0
    # for i in range(len(lis)):
    #     lis[i][0] = count
    #     count += 1

    A_varied = feature_set[0]
    ##print()
    A_varied[0] = 0
    lis = []
    for j in range(10):
        row = []
        for i in range(len(A_varied)):
            row.append(A_varied[i])
        lis.append(row)

    vals = np.linspace(280, 0, len(lis))
    count = 0
    for i in range(len(lis)):
        lis[i][0] = vals[i]
        count += 1

    for x, y in max_feature_values.items():
        maximums = np.linspace(0, 1, len(lis))
        for i in range(len(lis)):
            lis[i][x] = maximums[i]



    # #print(lis)

    ####################################################################
    #LR
    filename_lr = 'models/lr_openness_model.sav'
    filename_rr = 'models/rr_openness_model.sav'
    filename_lasso = 'models/lasso_openness_model.sav'
    filename_svm = 'models/svm_openness_model.sav'
    lr_model = pickle.load(open(filename_lr, 'rb'))
    rr_model = pickle.load(open(filename_rr, 'rb'))
    lasso_model = pickle.load(open(filename_lasso, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))
    #print(lr_model.predict(lis))
    y_pred1 = lr_model.predict(feature_set)
    y_pred2 = rr_model.predict(feature_set)
    y_pred3 = lasso_model.predict(feature_set)
    y_pred4 = svm_model.predict(feature_set)

    predictionsList.append([y_pred1, y_pred2, y_pred3, y_pred4])

    filename_lr = 'models/lr_conscientiousness_model.sav'
    filename_rr = 'models/rr_conscientiousness_model.sav'
    filename_lasso = 'models/lasso_conscientiousness_model.sav'
    filename_svm = 'models/svm_conscientiousness_model.sav'
    lr_model = pickle.load(open(filename_lr, 'rb'))
    rr_model = pickle.load(open(filename_rr, 'rb'))
    lasso_model = pickle.load(open(filename_lasso, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))
    #print(lr_model.predict(lis))
    y_pred1 = lr_model.predict(feature_set)
    y_pred2 = rr_model.predict(feature_set)
    y_pred3 = lasso_model.predict(feature_set)
    y_pred4 = svm_model.predict(feature_set)

    predictionsList.append([y_pred1, y_pred2, y_pred3, y_pred4])

    filename_lr = 'models/lr_extraversion_model.sav'
    filename_rr = 'models/rr_extraversion_model.sav'
    filename_lasso = 'models/lasso_extraversion_model.sav'
    filename_svm = 'models/svm_extraversion_model.sav'
    lr_model = pickle.load(open(filename_lr, 'rb'))
    rr_model = pickle.load(open(filename_rr, 'rb'))
    lasso_model = pickle.load(open(filename_lasso, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))
    #print(lr_model.predict(lis))
    y_pred1 = lr_model.predict(feature_set)
    y_pred2 = rr_model.predict(feature_set)
    y_pred3 = lasso_model.predict(feature_set)
    y_pred4 = svm_model.predict(feature_set)

    predictionsList.append([y_pred1, y_pred2, y_pred3, y_pred4])

    filename_lr = 'models/lr_agreeableness_model.sav'
    filename_rr = 'models/rr_agreeableness_model.sav'
    filename_lasso = 'models/lasso_agreeableness_model.sav'
    filename_svm = 'models/svm_agreeableness_model.sav'
    lr_model = pickle.load(open(filename_lr, 'rb'))
    rr_model = pickle.load(open(filename_rr, 'rb'))
    lasso_model = pickle.load(open(filename_lasso, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))

    #print(lr_model.predict(lis))
    #################################################################
    y_pred1 = lr_model.predict(feature_set)
    y_pred2 = rr_model.predict(feature_set)
    y_pred3 = lasso_model.predict(feature_set)
    y_pred4 = svm_model.predict(feature_set)

    predictionsList.append([y_pred1, y_pred2, y_pred3, y_pred4])

    filename_lr = 'models/lr_neuroticism_model.sav'
    filename_rr = 'models/rr_neuroticism_model.sav'
    filename_lasso = 'models/lasso_neuroticism_model.sav'
    filename_svm = 'models/svm_neuroticism_model.sav'
    lr_model = pickle.load(open(filename_lr, 'rb'))
    rr_model = pickle.load(open(filename_rr, 'rb'))
    lasso_model = pickle.load(open(filename_lasso, 'rb'))
    svm_model = pickle.load(open(filename_svm, 'rb'))
    #print(lr_model.predict(lis))
    y_pred1 = lr_model.predict(feature_set)
    y_pred2 = rr_model.predict(feature_set)
    y_pred3 = lasso_model.predict(feature_set)
    y_pred4 = svm_model.predict(feature_set)

    predictionsList.append([y_pred1, y_pred2, y_pred3, y_pred4])
    # #print("predictions:\n")
    # #print(predictionsList)
    return predictionsList
    # return pd.DataFrame(np.array(predictionsList, dtype='object'), columns=["linear","ridge","lasso"])
# predict()