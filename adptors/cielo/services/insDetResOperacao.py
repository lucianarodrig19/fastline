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
            
            query_insert = "INSERT INTO DetResOperacao ("
            query_insert = query_insert + "  idFile" 
            query_insert = query_insert + ", idRO" 
            query_insert = query_insert + ", TpRegistro"
            query_insert = query_insert + ", NroEstabelecimento"
            query_insert = query_insert + ", NroRO"
            query_insert = query_insert + ", Parcela"
            query_insert = query_insert + ", Filler"
            query_insert = query_insert + ", Plano"
            query_insert = query_insert + ", TpTransacao"
            query_insert = query_insert + ", DtApresentacao"
            query_insert = query_insert + ", DtPrvstaPgto"
            query_insert = query_insert + ", DtVenctoOriginal"
            query_insert = query_insert + ", SnlVlrBruto"
            query_insert = query_insert + ", VlrBruto"
            query_insert = query_insert + ", SnlTxAdmin"
            query_insert = query_insert + ", VlrTxAdmin"
            query_insert = query_insert + ", SnlVlrRejeitado"
            query_insert = query_insert + ", VlrRejeitado"
            query_insert = query_insert + ", SnlVlrLiquido"
            query_insert = query_insert + ", VlrLiquido"
            query_insert = query_insert + ", Banco"
            query_insert = query_insert + ", Agencia"
            query_insert = query_insert + ", CntCorrentePoupanca"
            query_insert = query_insert + ", StatusPagamento"
            query_insert = query_insert + ", QtdeCVsAceitos"
            query_insert = query_insert + ", IndicadorRecebaRapido"
            query_insert = query_insert + ", IndicadorTxMinima"
            query_insert = query_insert + ", QtdeCVsRejeitados"
            query_insert = query_insert + ", IdRevendaAceleracao"
            query_insert = query_insert + ", DtCapturaTransacao"
            query_insert = query_insert + ", OrigemAjuste"
            query_insert = query_insert + ", VlrComplementar"
            query_insert = query_insert + ", IdAntecipacao"
            query_insert = query_insert + ", NroOperAntecip"
            query_insert = query_insert + ", SnlVlrBrutoAntecipado"
            query_insert = query_insert + ", VlrBrutoAntecipado"
            query_insert = query_insert + ", Bandeira"
            query_insert = query_insert + ", NroUnicoRO"
            query_insert = query_insert + ", TxAdministrativa"
            query_insert = query_insert + ", TarifaAdministrativa"
            query_insert = query_insert + ", TxRecebaRapido"
            query_insert = query_insert + ", MeioCaptura"
            query_insert = query_insert + ", NroLogicoTerminal"
            query_insert = query_insert + ", CdProduto"
            query_insert = query_insert + ", MtrzPagamento"
            query_insert = query_insert + ", ReenvioPagamento"
            query_insert = query_insert + ", ConceitoAplicado"
            query_insert = query_insert + ", GrupoCartoes"
            query_insert = query_insert + ", IndicadorSaldoAberto"
            query_insert = query_insert + ") VALUES ("
            
            query_insert = query_insert + "  '" + item.idFile + "'"
            query_insert = query_insert + ", '" + item.idRO + "'"
            query_insert = query_insert + ", '" + item.TpRegistro + "'"
            query_insert = query_insert + ", '" + item.NroEstabelecimento + "'"
            query_insert = query_insert + ", '" + item.NroRO + "'"
            query_insert = query_insert + ", '" + item.Parcela + "'"
            query_insert = query_insert + ", '" + item.Filler + "'"
            query_insert = query_insert + ", '" + item.Plano + "'"
            query_insert = query_insert + ", '" + item.TpTransacao + "'"
            query_insert = query_insert + ", '" + item.DtApresentacao + "'"
            query_insert = query_insert + ", '" + item.DtPrvstaPgto + "'"
            query_insert = query_insert + ", '" + item.DtVenctoOriginal + "'"
            query_insert = query_insert + ", '" + item.SnlVlrBruto + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrBruto) /100) 
            query_insert = query_insert + ", '" + item.SnlTxAdmin + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrTxAdmin) /100) 
            query_insert = query_insert + ", '" + item.SnlVlrRejeitado + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrRejeitado) /100) 
            query_insert = query_insert + ", '" + item.SnlVlrLiquido + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrLiquido) /100)
            query_insert = query_insert + ", '" + item.Banco + "'"
            query_insert = query_insert + ", '" + item.Agencia + "'"
            query_insert = query_insert + ", '" + item.CntCorrentePoupanca + "'"
            query_insert = query_insert + ", '" + item.StatusPagamento + "'"
            query_insert = query_insert + ", '" + item.QtdeCVsAceitos + "'"
            query_insert = query_insert + ", '" + item.IndicadorRecebaRapido + "'"
            query_insert = query_insert + ", '" + item.IndicadorTxMinima + "'"
            query_insert = query_insert + ", '" + item.QtdeCVsRejeitados + "'"
            query_insert = query_insert + ", '" + item.IdRevendaAceleracao + "'"
            query_insert = query_insert + ", '" + item.DtCapturaTransacao + "'"
            query_insert = query_insert + ", '" + item.OrigemAjuste + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrComplementar) /100)
            query_insert = query_insert + ", '" + item.IdAntecipacao + "'"
            query_insert = query_insert + ", '" + item.NroOperAntecip + "'"
            query_insert = query_insert + ", '" + item.SnlVlrBrutoAntecipado + "'"
            query_insert = query_insert + ", "  + str(float(item.VlrBrutoAntecipado) /100)
            query_insert = query_insert + ", '" + item.Bandeira + "'"
            query_insert = query_insert + ", '" + item.NroUnicoRO + "'"
            query_insert = query_insert + ", '" + item.TxAdministrativa + "'"
            query_insert = query_insert + ", '" + item.TarifaAdministrativa + "'"
            query_insert = query_insert + ", '" + item.TxRecebaRapido + "'"
            query_insert = query_insert + ", '" + item.MeioCaptura + "'"
            query_insert = query_insert + ", '" + item.NroLogicoTerminal + "'"
            query_insert = query_insert + ", '" + item.CdProduto + "'"
            query_insert = query_insert + ", '" + item.MtrzPagamento + "'"
            query_insert = query_insert + ", '" + item.ReenvioPagamento + "'"
            query_insert = query_insert + ", '" + item.ConceitoAplicado + "'"
            query_insert = query_insert + ", '" + item.GrupoCartoes + "'"
            query_insert = query_insert + ", '" + item.IndicadorSaldoAberto + "')"
            
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        