# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

class ContaRecebimento:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile #Construtor da classe.
        self.TpRegistro = fileRow[:1]
        self.Banco = fileRow[1:5]
        self.Agencia = fileRow[5:10]
        self.Conta = fileRow[10:30]
        self.SnlVlrDepositado = fileRow[30:31]
        self.VlrDepositado = fileRow[31:44]
        self.UsoCielo = fileRow[44:250]
