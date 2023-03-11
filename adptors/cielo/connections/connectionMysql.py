# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

""" !pip3 install mysql.connector """
""" !pip3 install ssl """
 #!pip3 install urllib2
 
 #import requests;
 #print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])
 
#import ssl; print(ssl.OPENSSL_VERSION)

#import urllib2

#ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

import mysql.connector
from mysql.connector import errorcode
from  connections.configurations.config import getMySqlConnection

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = getMySqlConnection()
        #params['client_flags'] = [mysql.connector.ClientFlag.SSL]
        
        conn = mysql.connector.connect(**params)
        
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


if __name__ == '__main__':
    connect()
    

    
