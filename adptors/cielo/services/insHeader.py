# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
from connections.connectionMysql import connect

def execute(headers):
    try:
        conn = connect()
        cur = conn.cursor()
        
        for header in headers:
            query_insert = "INSERT INTO Header (idFile, TpRegistro, NroEstabelecimento, DtProcessamento, DtInicial, DtFinal, NroSeqArquivo, Adquirente, TipoExtrato, TransmissaoCielo, CaixaPostal, VrsLayout, UsoEmBranco) "
            query_insert = query_insert + "VALUES('"+ header.idFile +"','"+ header.TpRegistro +"', '"+ header.NroEstabelecimento +"', '"+ header.DtProcessamento +"', '"+ header.DtInicial +"', '" + header.DtFinal +"', '" + header.NroSeqArquivo + "', '" + header.Adquirente + "', '"+ header.TipoExtrato +"', '"+ header.TransmissaoCielo +"', '"+ header.CaixaPostal +"', '"+ header.VrsLayout +"', '"+ header.UsoEmBranco +"');"
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        