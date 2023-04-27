import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

import warnings
warnings.filterwarnings('ignore')

def get_variable_viz(train_telco, column):
    '''Takes in the train_telco dataset and provides visualizations for the column variable as it relates to churn.
    
    Also runs stats test to determine statistic significance.'''
    if train_telco[column].dtype == 'O':
        print(column.upper())
        pct = pd.crosstab(train_telco[column], train_telco.churn)
        pct.plot.bar() # This will produce a bar graph with counts based on churn
        plt.show()
        print()
        print(f'Stats results for {column} vs churn:')
        print()
        chi2, p, degf, expected = stats.chi2_contingency(pct)
        print(f'Chi^2 value: {chi2}')
        print(f'P-value: {p}')
        print()
    else:
        print(column.upper())

        # churn values (0 and 1) have to be replaced with string values ('0' and '1') because boxplots will not function with integers as categories.

        train_telco.churn = train_telco.churn.replace([0,1], ['0', '1'])
        sns.boxplot(data=train_telco, x=column, y='churn') # Boxplots for integers vs. churn. 
        plt.show()
        print()
        print(f'Stats results for {column} vs churn:')
        print()
        # Checked that none of the numerical variables follow a normal distribution. Moving over to Mann-Whitney test.
        stat, p = stats.mannwhitneyu(train_telco[train_telco.churn == '0'][column], train_telco[train_telco.churn == '1'][column])
        print(f'Stat value: {stat}')
        print(f'P-value: {p}')

        # churn values have to be restored back to their dtype of integer so that it can work with modeling.

        train_telco.churn = train_telco.churn.replace(['0', '1'], [0,1])
        print()

def classification_models_performance(X_train, y_train, X_validate, y_validate):
    '''Takes split train/validate sets to produce performance of model across all four classification models.
    '''
    # hyper_value has been hard coded because each model has already been run through a for-loop and hyper_value selected for best hyperparameter performance.

    scores = pd.DataFrame({}) # To add performance of each model to a DataFrame.
    
    # Decision Tree

    dtc = DecisionTreeClassifier(max_depth=6)
    dtc.fit(X_train, y_train)

    score = pd.DataFrame({'model': ['Decision Tree']
                        , 'train': [dtc.score(X_train, y_train)]
                        , 'validate': [dtc.score(X_validate, y_validate)]
                        , 'hyper_value': [6]
                        , 'difference': [(dtc.score(X_train, y_train) - dtc.score(X_validate, y_validate))]})

    scores = pd.concat([scores, score])

    # Random Forest

    rfc = RandomForestClassifier(max_depth=6, min_samples_leaf=5, random_state=123)
    rfc.fit(X_train, y_train)
# find where to put random state
    score = pd.DataFrame({'model': ['Random Forest']
                        , 'train': [rfc.score(X_train, y_train)]
                        , 'validate': [rfc.score(X_validate, y_validate)]
                        , 'hyper_value': [6]
                        , 'difference': [(rfc.score(X_train, y_train) - rfc.score(X_validate, y_validate))]})

    scores = pd.concat([scores, score])

    # KNN

    knn = KNeighborsClassifier(n_neighbors=8)
    knn.fit(X_train, y_train)

    score = pd.DataFrame({'model': ['KNN']
                        , 'train': [knn.score(X_train, y_train)]
                        , 'validate': [knn.score(X_validate, y_validate)]
                        , 'hyper_value': [8]
                        , 'difference': [(knn.score(X_train, y_train) - knn.score(X_validate, y_validate))]})

    scores = pd.concat([scores, score])

    # Logistic Regression

    lr = LogisticRegression(C=10)
    lr.fit(X_train, y_train)

    score = pd.DataFrame({'model': ['Logistic Regression']
                        , 'train': [lr.score(X_train, y_train)]
                        , 'validate': [lr.score(X_validate, y_validate)]
                        , 'hyper_value': [10]
                        , 'difference': [(lr.score(X_train, y_train) - lr.score(X_validate, y_validate))]})

    scores = pd.concat([scores, score]).reset_index(drop=True)

    return scores