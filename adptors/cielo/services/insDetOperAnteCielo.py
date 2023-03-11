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
            
            query_insert = "INSERT INTO DetResOperAnteCielo (\n"
            query_insert = query_insert + "  idFile\n"
            query_insert = query_insert + "	,TpRegistro\n"
            query_insert = query_insert + "	,NroEstabelecimento\n"
            query_insert = query_insert + "	,NroOperAntecip\n"
            query_insert = query_insert + "	,DtVenctoRO\n"
            query_insert = query_insert + "	,NroROAnteci\n"
            query_insert = query_insert + "	,ParcelaAnteci\n"
            query_insert = query_insert + "	,TotalParcelas\n"
            query_insert = query_insert + "	,SnlVlrBrutoOrigRO\n"
            query_insert = query_insert + "	,VlrBrutoOrigRO\n"
            query_insert = query_insert + "	,SnlVlrLiqOrigRO\n"
            query_insert = query_insert + "	,VlrLiqOrigRO\n"
            query_insert = query_insert + "	,SnlVlrBrutoAnteciRO\n"
            query_insert = query_insert + "	,VlrBrutoAnteciRO\n"
            query_insert = query_insert + "	,SnlVlrLiqAnteciRO\n"
            query_insert = query_insert + "	,VlrLiqAnteciRO\n"
            query_insert = query_insert + "	,Bandeira\n"
            query_insert = query_insert + "	,NroUnicoRO\n"
            query_insert = query_insert + "	,IdROAjstAnteci\n"
            query_insert = query_insert + "	,UsoCielo\n"
            query_insert = query_insert + ") VALUES (\n"
            query_insert = query_insert + "  '" + item.idFile + "'\n"
            query_insert = query_insert + "	,'" + item.TpRegistro + "'\n"
            query_insert = query_insert + "	,'" + item.NroEstabelecimento + "'\n"
            query_insert = query_insert + "	,'" + item.NroOperAntecip + "'\n"
            query_insert = query_insert + "	,'" + item.DtVenctoRO + "'\n"
            query_insert = query_insert + "	,'" + item.NroROAnteci + "'\n"
            query_insert = query_insert + "	,'" + item.ParcelaAnteci + "'\n"
            query_insert = query_insert + "	,'" + item.TotalParcelas + "'\n"

            query_insert = query_insert + "	,'" + item.SnlVlrBrutoOrigRO + "'\n"
            query_insert = query_insert + "	, " + str(float(item.VlrBrutoOrigRO) /100) + "\n"
            
            query_insert = query_insert + "	,'" + item.SnlVlrLiqOrigRO + "'\n"
            query_insert = query_insert + "	, " + str(float(item.VlrLiqOrigRO) /100) + "\n"
            
            query_insert = query_insert + "	,'" + item.SnlVlrBrutoAnteciRO + "'\n"
            query_insert = query_insert + "	, " + str(float(item.VlrBrutoAnteciRO) /100) + "\n"
            
            
            query_insert = query_insert + "	,'" + item.SnlVlrLiqAnteciRO + "'\n"
            query_insert = query_insert + "	, " + str(float(item.VlrBrutoAnteciRO) /100) + "\n"
            
            query_insert = query_insert + "	,'" + item.Bandeira + "'\n"
            query_insert = query_insert + "	,'" + item.NroUnicoRO + "'\n"
            query_insert = query_insert + "	,'" + item.IdROAjstAnteci + "'\n"
            query_insert = query_insert + "	,'" + item.UsoCielo + "'\n"
            query_insert = query_insert + ");\n"
            
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        