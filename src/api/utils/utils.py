import datetime
import pandas as pd


def get_month(date:datetime):
    return date.month

def get_year(date:datetime):
    return date.year

def mapper(file,key,value,target):
    try:
        df = pd.read_csv(file)
        for index,row in df.iterrows():
            if row[key] == value:
                return row[target]
    except(e):
        print("Error")

def status_mapper(file,key,date,value,target):
    try:
        df = pd.read_csv(file)
        for index,row in df.iterrows():
            if row[key] == value and row['date']==date:
                return row[target]
    except:
        print("Error")