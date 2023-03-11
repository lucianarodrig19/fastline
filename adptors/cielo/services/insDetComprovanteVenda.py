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
            
            query_insert = "INSERT INTO DetComprovanteVenda ( \n"
            query_insert = query_insert + "     idFile,\n"
            query_insert = query_insert + "     idRO,\n"
            query_insert = query_insert + " 	TpRegistro,\n"
            query_insert = query_insert + " 	NroEstabelecimento,\n"
            query_insert = query_insert + " 	NroRO,\n"
            query_insert = query_insert + " 	NroCartaoTruncado,\n"
            query_insert = query_insert + " 	DtVendaAjuste,\n"
            query_insert = query_insert + " 	SnlVlrCompraVlrParcela,\n"
            query_insert = query_insert + " 	VlrCompraVlrParcela,\n"
            query_insert = query_insert + " 	Parcela,\n"
            query_insert = query_insert + " 	TptalParcelas,\n"
            query_insert = query_insert + " 	MotivoRejeição,\n"
            query_insert = query_insert + " 	CdAutorização,\n"
            query_insert = query_insert + " 	TID,\n"
            query_insert = query_insert + " 	NSUDOC,\n"
            query_insert = query_insert + " 	VlrComplementar,\n"
            query_insert = query_insert + " 	DigCartao,\n"
            query_insert = query_insert + " 	VlrTotalVenda,\n"
            query_insert = query_insert + " 	VlrProximaParcela,\n"
            query_insert = query_insert + " 	NroNotaFiscal,\n"
            query_insert = query_insert + " 	TipoCartao,\n"
            query_insert = query_insert + " 	GrupoCartoes,\n"
            query_insert = query_insert + " 	NroLogicoTerminal,\n"
            query_insert = query_insert + " 	IdTxEmbarqueVlrEntrada,\n"
            query_insert = query_insert + " 	RefCdPedido,\n"
            query_insert = query_insert + " 	HrTransacao,\n"
            query_insert = query_insert + " 	NroUnicoTransacao,\n"
            query_insert = query_insert + " 	IndicadorCieloPromo,\n"
            query_insert = query_insert + " 	ModoEntradaCartao,\n"
            query_insert = query_insert + " 	CdVenda,\n"
            query_insert = query_insert + " 	CdInternoAjuste\n"
            query_insert = query_insert + " ) VALUES (\n"
            query_insert = query_insert + " 	'" + item.idFile + "',\n"
            query_insert = query_insert + " 	'" + item.idRO + "',\n"
            query_insert = query_insert + " 	'" + item.TpRegistro + "',\n"
            query_insert = query_insert + " 	'" + item.NroEstabelecimento + "',\n"
            query_insert = query_insert + " 	'" + item.NroRO + "',\n"
            query_insert = query_insert + " 	'" + item.NroCartaoTruncado + "',\n"
            query_insert = query_insert + " 	'" + item.DtVendaAjuste + "',\n"
            query_insert = query_insert + " 	'" + item.SnlVlrCompraVlrParcela + "',\n"
            query_insert = query_insert + " 	"  + str(float(item.VlrCompraVlrParcela)/100) + ",\n"
            query_insert = query_insert + " 	'" + item.Parcela + "',\n"
            query_insert = query_insert + " 	'" + item.TotalParcelas + "',\n"
            query_insert = query_insert + " 	'" + item.MotivoRejeição + "',\n"
            query_insert = query_insert + " 	'" + item.CdAutorização + "',\n"
            query_insert = query_insert + " 	'" + item.TID + "',\n"
            query_insert = query_insert + " 	'" + item.NSUDOC + "',\n"
            query_insert = query_insert + " 	"  + str(float(item.VlrComplementar)/100) + ",\n"
            query_insert = query_insert + " 	'" + item.DigCartao + "',\n"
            query_insert = query_insert + " 	 " + str(float(item.VlrTotalVenda)/100) + ",\n"
            query_insert = query_insert + " 	 " + str(float(item.VlrProximaParcela)/100) + ",\n"
            query_insert = query_insert + " 	'" + item.NroNotaFiscal + "',\n"
            query_insert = query_insert + " 	'" + item.TipoCartao + "',\n"
            query_insert = query_insert + " 	'" + item.GrupoCartoes + "',\n"
            query_insert = query_insert + " 	'" + item.NroLogicoTerminal + "',\n"
            query_insert = query_insert + " 	'" + item.IdTxEmbarqueVlrEntrada + "',\n"
            query_insert = query_insert + " 	'" + item.RefCdPedido + "',\n"
            query_insert = query_insert + " 	'" + item.HrTransacao + "',\n"
            query_insert = query_insert + " 	'" + item.NroUnicoTransacao + "',\n"
            query_insert = query_insert + " 	'" + item.IndicadorCieloPromo + "',\n"
            query_insert = query_insert + " 	'" + item.ModoEntradaCartao + "',\n"
            query_insert = query_insert + " 	'" + item.CdVenda + "',\n"
            query_insert = query_insert + " 	'" + item.CdInternoAjuste + "'\n"
            query_insert = query_insert + " )";
            
            cur.execute(query_insert)
        
        conn.commit()
    
    except (Exception) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            
        