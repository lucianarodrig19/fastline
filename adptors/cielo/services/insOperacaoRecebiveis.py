# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
from connections.connectionMysql import connect

def execute(list):
    try:
        conn = connect()
        cur = conn.cursor()
        
        for item in list:
            
            query_insert = "INSERT INTO OperacaoRecebiveis ("
            query_insert = query_insert + "	idFile"
            query_insert = query_insert + "	, TpRegistro"
            query_insert = query_insert + "	, NroEstabelecimento"
            query_insert = query_insert + "	, CdOperacao"
            query_insert = query_insert + "	, CPFCNPJTitular"
            query_insert = query_insert + "	, CPFCNPJRecebedor"
            query_insert = query_insert + "	, CPFCNPJTitularConta"
            query_insert = query_insert + "	, DtPagamento"
            query_insert = query_insert + "	, DtVenctoOriginal"
            query_insert = query_insert + "	, TipoOperacao"
            query_insert = query_insert + "	, Bandeira"
            query_insert = query_insert + "	, TpLiquidacao"
            query_insert = query_insert + "	, SnlVlrOperacao"
            query_insert = query_insert + "	, VlrOperacao"
            query_insert = query_insert + "	, CdMoeda"
            query_insert = query_insert + "	, Banco"
            query_insert = query_insert + "	, Agencia"
            query_insert = query_insert + "	, Conta"
            query_insert = query_insert + "	, UsoCielo"
            query_insert = query_insert + " ) VALUES( "
            query_insert = query_insert + "   '" + item.idFile + "'"
            query_insert = query_insert + "	, '" + item.TpRegistro + "'"
            query_insert = query_insert + "	, '" + item.NroEstabelecimento + "'"
            query_insert = query_insert + "	, '" + item.CdOperacao + "'"
            query_insert = query_insert + "	, '" + item.CPFCNPJTitular + "'"
            query_insert = query_insert + "	, '" + item.CPFCNPJRecebedor + "'"
            query_insert = query_insert + "	, '" + item.CPFCNPJTitularConta + "'"
            query_insert = query_insert + "	, '" + item.DtPagamento + "'"
            query_insert = query_insert + "	, '" + item.DtVenctoOriginal + "'"
            query_insert = query_insert + "	, '" + item.TipoOperacao + "'"
            query_insert = query_insert + "	, '" + item.Bandeira + "'"
            query_insert = query_insert + "	, '" + item.TpLiquidacao + "'"
            query_insert = query_insert + "	, '" + item.SnlVlrOperacao + "'"
            query_insert = query_insert + "	, "  + str(float(item.VlrOperacao)/100) 
            query_insert = query_insert + "	, '" + item.CdMoeda + "'"
            query_insert = query_insert + "	, '" + item.Banco + "'"
            query_insert = query_insert + "	, '" + item.Agencia + "'"
            query_insert = query_insert + "	, '" + item.Conta + "'"
            query_insert = query_insert + "	, '" + item.UsoCielo + "'"
            query_insert = query_insert + ");"
            
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        