# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:02:11 2020

@author: Milica
"""

import pandas as pd
import json

file_path = 'data/devices.csv'
file_name_json = 'devices_pandas.json'
column_order = ['MODELNAME', 'IP', 'SYSDESC', 'COMMUNITY', 'CLASSNAME', 'HOSTNAME', 'SERIALNUMBER' ]

def read_data_frame():
    ''' Reads data from a file and returns a data frame. 
    NaN values filled with '' as in example. '''    
    df = pd.read_csv(file_path)
    df = df.fillna('')

    return df


def sort_columns(data_frame):  
    ''' Sorts columns in order specified above. '''
    return data_frame[column_order]


def add_column_vendor(data_frame):
    ''' Creates a new column - VENDOR. '''
    data_frame['VENDOR'] = data_frame['CLASSNAME'].apply(lambda x: 'Cisco' if ('Cisco' in x) 
                                                        else 'Nokia' if (('Alcatel' in x) | ('Nokia' in x)) 
                                                        else 'Huawei' if ('Huawei' in x) 
                                                        else 'Juniper' if ('Juniper' in x) 
                                                        else 'Other')


def remove_devices_without_vendors_df(data_frame):
    ''' Removes devices without vendor. '''
    return  data_frame[data_frame['VENDOR'] != 'Other']
  

def remove_column(data_frame, column):
    ''' Removes a column. '''    
    return data_frame.drop(columns = [column])


def create_dictionary(data_frame):
    ''' Creates a list of dictionaries from a data frame. '''
    return data_frame.to_dict('records')


def create_json_df(list_of_devices):
    ''' Creates json file from a list of dictionaries. 
    File name specified above.'''
    with open(file_name_json, 'w') as file_out:
        json.dump(list_of_devices, file_out, indent=4)   
        return file_name_json



