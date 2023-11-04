from django.shortcuts import render
import pandas as pd
from myapp.business.save_trans_file import *
from django.http import HttpResponse

# Create your views here.


def index(abc):
  path = '/home/dev36/kreditz/spanish_data/TF transaction categorisation dictionary.xlsx'
  df = pd.read_excel(path)
  import pdb
  #pdb.set_trace()
  #df.reset_index(inplace=True)
  result = df.to_dict(orient="records")
  save_trans(result)
  return HttpResponse("Your response content here")


def index2(abc):
  #path = '/home/dev36/kreditz/spanish_data/TF_es_psd2_20230818/mk_es_2022.csv'
  # import csv

  # with open(path, 'r', encoding='latin-1') as file:
  #     reader = csv.reader(file)
  #     for row in reader:
  #         try:
  #             continue
  #         except csv.Error as e:
  #             sys.exit('file {}, line {}: {}'.format(path, reader.line_num, e))
  column_names = ['ApplicationId', 'ApplicationDate', 'IdRow', 'AccountId', 'Balance',
       'Bank', 'transactionDate', 'transactionAmount', 'transactionClass',
       'transactionDescription', 'predictedCategoryDescription']
  import pdb
  #df = pd.read_csv('mk_es_afterbanks_2023p3_.csv', skiprows=0, encoding='latin-1')
  #df = pd.read_csv('mk_es_afterbanks_2023p3_.csv', skiprows=4303210, encoding='latin-1', header=None, names=column_names)
  df = pd.read_csv('mk_es_afterbanks_2023p3_.csv', encoding='latin-1')
  # pdb.set_trace()
  batch_size = 2500000
  for i in range(0, df.shape[0], batch_size):
    batch = df.iloc[i:i + batch_size].copy()
    batch['Balance'] = batch['Balance'].str.replace(',','').astype(float)
    batch['ApplicationDate'] = pd.to_datetime(batch['ApplicationDate'])
    batch['transactionDate'] = pd.to_datetime(batch['transactionDate'])
    batch['transactionAmount'] = batch['transactionAmount'].str.replace(',','').astype(float)
    result = batch.to_dict(orient="records")
    save_trans(result)
  return HttpResponse("Your response content here")



  # batch_size = 2500000
  # batches = [df.iloc[i:i + batch_size].reset_index(drop=True) for i in range(0, df.shape[0], batch_size)]
  # for batch in batches:
  #   pdb.set_trace()
  #   #df = df.iloc[:500000]
  #   batch['Balance'] = batch['Balance'].str.replace(',','').astype(float)
  #   batch['ApplicationDate'] = pd.to_datetime(batch['ApplicationDate'])
  #   batch['transactionDate'] = pd.to_datetime(batch['transactionDate'])
  #   batch['transactionAmount'] = batch['transactionAmount'].str.replace(',','').astype(float)
  #   #batch.reset_index(inplace=True)
  #   result = batch.to_dict(orient="records")
  #   save_trans(result)
  # return HttpResponse("Your response content here")























# import dask.dataframe as dd
# from dask.diagnostics import ProgressBar
# import dask.bag as db


# def index2(abc):
#     column_names = ['ApplicationId', 'ApplicationDate', 'IdRow', 'AccountId', 'Balance',
#                      'Bank', 'transactionDate', 'transactionAmount', 'transactionClass',
#                      'transactionDescription', 'predictedCategoryDescription']

#     # Use Dask to read the CSV file
#     df = dd.read_csv('mk_es_afterbanks_2023p1_.csv', 
#                      #skiprows=0, 
#                      encoding='latin-1', 
#                      #header=None, 
#                      #names=column_names
#                      )

#     # Define functions to process the data
#     import pdb
#     def clean_balance(balance):
#         return balance.str.replace(',', '').astype(float)

#     def clean_dates(df):
#         df['ApplicationDate'] = dd.to_datetime(df['ApplicationDate'])
#         df['transactionDate'] = dd.to_datetime(df['transactionDate'])
#         return df

#     def clean_transaction_amount(amount):
#         return amount.str.replace(',', '').astype(float)

#     # Apply data cleaning functions
#     #pdb.set_trace()
#     df['Balance'] = clean_balance(df['Balance'])
#     df = clean_dates(df)
#     df['transactionAmount'] = clean_transaction_amount(df['transactionAmount'])

#     # Convert to a list of dictionaries
#     result = df.compute().to_dict(orient='records')

#     # Define a function to save the transactions
#     # def save_trans(records):
#     #     # Implement your saving logic here
#     #     pass

#     # Use Dask bag to process and save the records
#     with ProgressBar():
#         db.from_sequence(result).map(save_trans).compute()

#     # Return an HttpResponse (replace this with your actual response)
#     return HttpResponse("Your response content here")








