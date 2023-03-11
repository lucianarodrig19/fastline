# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
class ResNegRecebiveis:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        
        self.TpRegistro = fileRow[:1]
        self.DtNegociacao = fileRow[1:7]
        self.DtPagamento = fileRow[7:13]
        self.CPFCNPJ = fileRow[13:27]
        self.PrazoMedio = fileRow[27:30]
        self.TxNominal = fileRow[30:35]
        self.SnlVlrBruto = fileRow[35:36]
        self.VlrButo = fileRow[36:49]
        self.SnlVlrLiq = fileRow[49:50]
        self.VlrLiq = fileRow[50:63]
        self.CdOperacao = fileRow[63:83]
        self.UsoCielo = fileRow[83:250]

        