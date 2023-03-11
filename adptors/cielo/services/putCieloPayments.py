# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
from connections.connectionMysql import connect

def execute():
    try:
        conn = connect()

    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        