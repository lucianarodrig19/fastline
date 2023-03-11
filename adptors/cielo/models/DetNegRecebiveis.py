# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
class DetNegRecebiveis:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.DtNegociacao = fileRow[1:7]
        self.DtVenctoOrig = fileRow[7:13]
        self.CPFCNPJ = fileRow[13:27]
        self.Bandeira = fileRow[27:30]
        self.TpLiq = fileRow[30:33]
        self.SnlVlrBruto = fileRow[33:34]
        self.VlrBruto = fileRow[34:47]
        self.SnlVlrLiq = fileRow[47:48]
        self.VlrLiq = fileRow[48:61]
        self.TxEfetiva = fileRow[61:66]
        self.InstFinanceira= fileRow[66:116]
        self.UsoCielo = fileRow[116:250]


        