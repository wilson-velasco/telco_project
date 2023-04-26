import pandas as pd
import numpy as np
import os
from env import get_db_url 
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

link = os.getcwd()+'/'

def get_telco_data():
    '''Pulls in customers table from the telco_churn database on CodeUp server. 
    
    Output includes joined tables: contract_types, internet_service_types, and payment_types.
    
    Writes to .csv file on initial pull, and will read from .csv for all future pulls (if it still exists in current working directory).'''

    url = get_db_url('telco_churn')
    SQL_query = '''SELECT * FROM customers
	            JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING(internet_service_type_id)
                JOIN payment_types USING(payment_type_id);'''

    # Checking to see if file exists in local directory. 

    if os.path.exists(link + 'telco.csv'):
        df = pd.read_csv('telco.csv')
        return df

    # Write to a local csv file if it doesn't exist. 

    else:
        df = pd.read_sql(SQL_query,url)
        df.to_csv('telco.csv', index=False)
        return df
    
def prep_telco(telco):
    '''Prepares telco data from get_telco_data function.

    Handles null values and switches dtype for total_charges to float.

    Encodes the following variables for modeling: gender, multiple_lines, online_security, device_protection, tech_support, streaming_tv, streaming_movies, contract_type, internet_service_type, payment_type'''
    
    # Set customer_id to index since it's unique and so it doesn't interfere with modeling. Will need to be preserved for predictions later.
    
    # Dropping ids for payment_type, internet_service_type, contract_type due to redundancy.

    telco = telco.set_index('customer_id').drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'])

    #!!! Discovered that a much higher percentage of customers who have internet churn vs those who don't. We'll look at just subset of those who do.

    telco = telco[telco.streaming_tv != 'No internet service'] #Arbitrarily choose streaming TV, since this filters out all other 'No internet' values in other columns too
    
    # Replacing Yes and No with 1's and 0's for easier modeling. Some columns with three values will still need additional encoding.

    telco.churn = telco.churn.replace(['Yes', 'No'], [1,0])

    # Encoding for columns with other string values and/or >3 unique values.

    telco_dummies = pd.get_dummies(telco[['gender', 'multiple_lines', 'online_security', 'tech_support', 'contract_type', 'internet_service_type', 'payment_type']], drop_first=True)
    #  'online_backup', 'device_protection', 'streaming_tv', 'streaming_movies',  -- in case my hypothesis is incorrect
    
    telco = pd.concat([telco, telco_dummies], axis=1)
    
    # Handling null values in total_charges and switching dtype to float.

    telco.total_charges = telco.total_charges.replace(' ', 0).astype(float)

    return telco

def split_data(df, target):
    '''
    Takes in a DataFrame and returns train, validate, and test DataFrames; stratifies on target argument.
    
    Train, Validate, Test split is: 60%, 20%, 20% of input dataset, respectively.
    '''
    # First round of split (train+validate and test)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])

    # Second round of split (train and validate)
    train, validate = train_test_split(train_validate, 
                                       test_size=.25, 
                                       random_state=123, 
                                       stratify=train_validate[target])
    return train, validate, test