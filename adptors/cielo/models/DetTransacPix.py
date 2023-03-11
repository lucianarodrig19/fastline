# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
class DetTransacPix:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.TpTransacao = fileRow[11:13]
        self.DtTransacao = fileRow[13:19]
        self.HrTransacao = fileRow[19:25]
        self.IDPIX= fileRow[25:61]
        self.NSUDOC = fileRow[61:67]
        self.DtPagamento = fileRow[67:73]
        self.SnlVlrBruto = fileRow[73:74]
        self.ValorBruto = fileRow[74:87]
        self.SnlTxAdmin = fileRow[87:88]
        self.VlrTxAdmin = fileRow[88:101]
        self.SnlVlrLiq = fileRow[101:102]
        self.VlrLiq = fileRow[102:115]
        self.Banco = fileRow[115:119]
        self.Agência = fileRow[119:124]
        self.Conta = fileRow[124:144]
        self.DtCaptTransc = fileRow[144:150]
        self.TxAdmin = fileRow[150:154]
        self.TrfaAdmin = fileRow[154:159]
        self.MeioCaptura = fileRow[159:161]
        self.NroLogTerminal = fileRow[161:169]
        self.DtTranscOrig = fileRow[169:175]
        self.HrTranscOrig = fileRow[175:181]
        self.IDPIXOrig = fileRow[181:217]
        self.IndicTrocoSaque = fileRow[217:219]
        self.UsoCielo = fileRow[219:250]



       