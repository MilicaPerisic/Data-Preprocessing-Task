# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:47:19 2020

@author: Milica
"""
import logging
from pandas_processing import * 
from dictionary_processing import *


def init_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter("LOG %(asctime)s %(levelname)-5s %(message)s")
    handler.setFormatter(formatter)
    
    if (logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(handler)
    logger.addHandler(handler)
    logger.setLevel('INFO')
    return logger

done = False
logger = init_logger()

def pd_processing():
    df = read_data_frame()
    logger.info(f">>> Dataset was read, contains {df.shape[0]} rows.")

    df = sort_columns(df)
    logger.info(f">>> Columns are in the desired order: {list(df.columns)}")
            
    add_column_vendor(df)
    logger.info(f">>> Vendors have been added. Vendors summary:\n{df['VENDOR'].value_counts()}")
    

    df = remove_devices_without_vendors_df(df)
    logger.info(f">>> Devices without vendor have been deleted. Current dataframe has {df.shape[0]} rows.")

    df = remove_column(df, 'CLASSNAME')
    logger.info(">>> The column CLASSNAME has been removed.")

    devices = create_dictionary(df)
    logger.info(">>> List of dictionaries have been created.")

    file_name = create_json_df(devices)
    logger.info(f">>> Output json file has been created and saved. File name: {file_name}")

def dict_processing():
    devices = read_data_dict()
    logger.info(f">>> Dataset was read, list of dictionaries has {len(devices)} values.")

    devices = sort_keys(devices)
    logger.info(">>> Keys are in the desired order.")

    add_key_vendor(devices)
    logger.info(">>> Vendors have been added.")
        
    remove_devices_without_vendors_dict(devices)
    logger.info(f">>> Devices without vendor have been deleted. Current list has {len(devices)} values.")

    remove_key(devices, 'CLASSNAME')
    logger.info(">>> The key-value pair CLASSNAME has been removed.")

    file_name = create_json_dict(devices)
    logger.info(f">>> Output json file has been created and saved. File name: {file_name}")
    
def menu():
    print("=========================================")
    print("Data Preprocessing Task")
    print("=========================================")
    print("Menu:")
    print("1. Use pandas processing")
    print("2. Use dictionary processing")
    print("3. END")
    print("=========================================")
    

    


if __name__ == '__main__':

    while not done:
        menu()
        answer = input("Please input your choice: ")

        try:
            choice = int(answer)
        except:
            print("Wrong format of the input. Try again.")
            continue

        if choice == 1:
            pd_processing()
        elif choice == 2:
            dict_processing()
        elif choice == 3:
            done = True
            
    
    
    