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

def linear_regression():
    import json

    with open('data_processed/train_data.json', 'r') as f:
        data1 = json.load(f)

    data1 = pd.read_json('data_processed/train_data.json')
    # #print(data1)
    feature_set = pd.concat([data1['wordcount'], data1['category'], data1.iloc[:,9:]], axis=1)
    # #print(feature_set.columns)
    feature_set = feature_set.to_numpy()
    output_openness = pd.concat([data1['openness']], axis=1).to_numpy()
    output_conscientiousness = pd.concat([data1['conscientiousness']], axis=1).to_numpy()
    output_extraversion = pd.concat([data1['extraversion']], axis=1).to_numpy()
    output_agreeableness = pd.concat([data1['agreeableness']], axis=1).to_numpy()
    output_neuroticism = pd.concat([data1['neuroticism']], axis=1).to_numpy()
    # openness model
    X_train = feature_set
    y_train = output_openness
    # (X_train, X_test, y_train, y_test) = train_test_split(feature_set, output_openness, test_size=0, shuffle=False)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, y_train)
    ridge_model = ridge_regrssion(X_train, y_train)
    lasso_model = lasso_regression(X_train, y_train)
    svm_model = svm_regression(X_train, y_train)
    # y_pred = linear_regressor.predict(X_test)
    # #print(y_pred)
    #
    # error = mean_squared_error(y_test, y_pred, squared=False)
    # #print("error", error)
    filename_lr = 'models/lr_openness_model.sav'
    filename_rr = 'models/rr_openness_model.sav'
    filename_lasso = 'models/lasso_openness_model.sav'
    filename_svm = 'models/svm_openness_model.sav'
    pickle.dump(linear_regressor, open(filename_lr, 'wb'))
    pickle.dump(ridge_model, open(filename_rr, 'wb'))
    pickle.dump(lasso_model, open(filename_lasso, 'wb'))
    pickle.dump(svm_model, open(filename_svm, 'wb'))



    # output_conscientiousness model
    X_train = feature_set
    y_train = output_conscientiousness
    # (X_train, X_test, y_train, y_test) = train_test_split(feature_set, output_conscientiousness, test_size=0, shuffle=False)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, y_train)
    ridge_model = ridge_regrssion(X_train, y_train)
    lasso_model = lasso_regression(X_train, y_train)
    svm_model = svm_regression(X_train, y_train)
    # y_pred = linear_regressor.predict(X_test)
    # #print(y_pred)
    #
    # error = mean_squared_error(y_test, y_pred, squared=False)
    # #print("error", error)
    filename_lr = 'models/lr_conscientiousness_model.sav'
    filename_rr = 'models/rr_conscientiousness_model.sav'
    filename_lasso = 'models/lasso_conscientiousness_model.sav'
    filename_svm = 'models/svm_conscientiousness_model.sav'
    pickle.dump(linear_regressor, open(filename_lr, 'wb'))
    pickle.dump(ridge_model, open(filename_rr, 'wb'))
    pickle.dump(lasso_model, open(filename_lasso, 'wb'))
    pickle.dump(svm_model, open(filename_svm, 'wb'))



    # output_extraversion model
    X_train = feature_set
    y_train = output_extraversion
    # (X_train, X_test, y_train, y_test) = train_test_split(feature_set, output_extraversion, test_size=0, shuffle=False)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, y_train)
    ridge_model = ridge_regrssion(X_train, y_train)
    lasso_model = lasso_regression(X_train, y_train)
    svm_model = svm_regression(X_train, y_train)

    filename_lr = 'models/lr_extraversion_model.sav'
    filename_rr = 'models/rr_extraversion_model.sav'
    filename_lasso = 'models/lasso_extraversion_model.sav'
    filename_svm = 'models/svm_extraversion_model.sav'
    pickle.dump(linear_regressor, open(filename_lr, 'wb'))
    pickle.dump(ridge_model, open(filename_rr, 'wb'))
    pickle.dump(lasso_model, open(filename_lasso, 'wb'))
    pickle.dump(svm_model, open(filename_svm, 'wb'))


    # output_agreeableness model
    X_train = feature_set
    y_train = output_agreeableness
    # (X_train, X_test, y_train, y_test) = train_test_split(feature_set, output_agreeableness, test_size=0, shuffle=False)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, y_train)
    ridge_model = ridge_regrssion(X_train, y_train)
    lasso_model = lasso_regression(X_train, y_train)
    svm_model = svm_regression(X_train, y_train)

    filename_lr = 'models/lr_agreeableness_model.sav'
    filename_rr = 'models/rr_agreeableness_model.sav'
    filename_lasso = 'models/lasso_agreeableness_model.sav'
    filename_svm = 'models/svm_agreeableness_model.sav'
    pickle.dump(linear_regressor, open(filename_lr, 'wb'))
    pickle.dump(ridge_model, open(filename_rr, 'wb'))
    pickle.dump(lasso_model, open(filename_lasso, 'wb'))
    pickle.dump(svm_model, open(filename_svm, 'wb'))


    # output_neuroticism model
    X_train = feature_set
    y_train = output_neuroticism
    # (X_train, X_test, y_train, y_test) = train_test_split(feature_set, output_neuroticism, test_size=0, shuffle=False)
    linear_regressor = LinearRegression()
    linear_regressor.fit(X_train, y_train)
    ridge_model = ridge_regrssion(X_train, y_train)
    lasso_model = lasso_regression(X_train, y_train)
    svm_model = svm_regression(X_train, y_train)

    filename_lr = 'models/lr_neuroticism_model.sav'
    filename_rr = 'models/rr_neuroticism_model.sav'
    filename_lasso = 'models/lasso_neuroticism_model.sav'
    filename_svm = 'models/svm_neuroticism_model.sav'
    pickle.dump(linear_regressor, open(filename_lr, 'wb'))
    pickle.dump(ridge_model, open(filename_rr, 'wb'))
    pickle.dump(lasso_model, open(filename_lasso, 'wb'))
    pickle.dump(svm_model, open(filename_svm, 'wb'))



def ridge_regrssion(X_train, y_train):
    clf = Ridge(alpha=1.0)
    clf.fit(X_train, y_train)
    return clf

def lasso_regression(X_train, y_train):
    from sklearn import linear_model
    clf = linear_model.Lasso(alpha=0.1)
    clf.fit(X_train, y_train)
    return clf

def svm_regression(X_train, y_train):
    from sklearn import svm
    regr = svm.SVR()
    regr.fit(X_train, y_train)
    return regr


linear_regression()