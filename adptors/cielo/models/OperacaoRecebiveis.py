# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
#Registro 3 - Operação de recebíveis

class OperacaoRecebiveis:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.CdOperacao = fileRow[11:31]
        self.CPFCNPJTitular = fileRow[31:45]
        self.CPFCNPJRecebedor = fileRow[45:59]
        self.CPFCNPJTitularConta = fileRow[59:73]
        self.DtPagamento = fileRow[73:81]
        self.DtVenctoOriginal = fileRow[81:89]
        self.TipoOperacao = fileRow[89:91]
        self.Bandeira = fileRow[91:94]
        self.TpLiquidacao = fileRow[94:97]
        self.SnlVlrOperacao = fileRow[97:98]
        self.VlrOperacao = fileRow[98:115]
        self.CdMoeda = fileRow[115:118]
        self.Banco = fileRow[118:122]
        self.Agencia = fileRow[122:127]
        self.Conta = fileRow[127:141]
        self.UsoCielo = fileRow[141:250]
       