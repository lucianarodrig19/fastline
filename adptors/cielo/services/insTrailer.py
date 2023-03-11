# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
from connections.connectionMysql import connect

def execute(trailers):
    try:
        conn = connect()
        cur = conn.cursor()
        
        for trailer in trailers:
            
            query_insert = "INSERT INTO Trailer (idFile, TpRegistr, TotalRegistro, SnlVlrLiqSomaCVs, VlrLiqSomaCVs, QtdeTotalCVs, SnlVlrBrutoSomaROs, VlrBrutoSomaROs, SnlVlrBrutoAnteciSomaROs, VlrBrutoAnteciSomaROs, SnlSomaVlrsNegociados, SomaVlrsNegociados, UsoCielo) "
            query_insert = query_insert + "VALUES('"+ trailer.idFile +"','"+ trailer.TpRegistro +"','"+ trailer.TotalRegistro +"', '" + trailer.SnlVlrLiqSomaCVs + "', " + str(float(trailer.VlrLiqSomaCVs)/100) + ", '" + trailer.QtdeTotalCVs + "', '" + trailer.SnlVlrBrutoSomaROs + "', " + str(float(trailer.VlrBrutoSomaROs)/100) + ", '" + trailer.SnlVlrBrutoAnteciSomaROs + "', " + str(float(trailer.VlrBrutoAnteciSomaROs)/100) + ", '" + trailer.SnlSomaVlrsNegociados + "', " + str(float(trailer.SomaVlrsNegociados)/100) + ", '" + trailer.UsoCielo + "')";
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        