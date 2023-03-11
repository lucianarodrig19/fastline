# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

import requests
import json
import pandas as pd

url = "https://services.contaazul.com/contaazul-bff/dashboard/v1/financial-accounts"

payload={}
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'X-Authorization': '99588ab7-4251-47b5-a565-9627f07c5424',
    'Cookie': 'cookiesession1=678A3E102C1A34414D38841841A26711'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json()

df = pd.json_normalize(data, record_path=['dashboardBankAccounts'])
