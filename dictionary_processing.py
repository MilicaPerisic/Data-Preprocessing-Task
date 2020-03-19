# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:34:11 2020

@author: Milica
"""
import pandas as pd
import json

file_path = 'data/devices.csv'
file_name_json = 'devices_dictionary.json'
key_order = ['MODELNAME', 'IP', 'SYSDESC', 'COMMUNITY', 'CLASSNAME', 'HOSTNAME', 'SERIALNUMBER' ]


def read_data_dict():
    ''' Reads data from a file.
    NaN values filled with '' as in example. 
    Returns a list of dictionaries created from a data frame rows.'''
    df = pd.read_csv(file_path)
    df = df.fillna('')
    
    devices = df.to_dict('records')
    return devices


def sort_keys(list_of_devices):
    ''' Sorts keys in order specified above. '''
    devices = []
    for unordered_device in list_of_devices:
        device = {k: unordered_device[k] for k in key_order}
        devices = devices + [device]
    
    return devices


def add_key_vendor(list_of_devices):
    ''' Creates a new key - VENDOR. '''
    for device in list_of_devices:
        if 'Cisco' in device['CLASSNAME']:
            device.update({'VENDOR' : 'Cisco'})
        if ('Alcatel' in device['CLASSNAME']) or ('Nokia' in device['CLASSNAME']):
            device.update({'VENDOR' : 'Nokia'})
        if 'Huawei' in device['CLASSNAME']:
            device.update({'VENDOR' : 'Huawei'})
        if 'Juniper' in device['CLASSNAME']:
            device.update({'VENDOR' : 'Juniper'})

       
def remove_devices_without_vendors_dict(list_of_devices):
    ''' Removes devices without vendor. '''
    for device in list_of_devices:
        if 'VENDOR' not in device.keys():
            list_of_devices.remove(device)

          
def remove_key(list_of_devices, key):
    ''' Removes a key. ''' 
    for device in list_of_devices:
        del device[key]


def create_json_dict(list_of_devices):
    ''' Creates json file from a list of dictionaries. File name specified above.'''
    with open(file_name_json, 'w') as file_out:
        json.dump(list_of_devices, file_out, indent=4)
        return file_name_json
        

