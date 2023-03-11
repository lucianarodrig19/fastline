# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
#Registro 0 - Header
class Header:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.
        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.DtProcessamento = fileRow[11:19]
        self.DtInicial = fileRow[19:27]
        self.DtFinal = fileRow[27:35]
        self.NroSeqArquivo = fileRow[35:42]
        self.Adquirente = fileRow[42:47]
        self.TipoExtrato = fileRow[47:49]
        self.TransmissaoCielo = fileRow[49:50]
        self.CaixaPostal = fileRow[50:70]
        self.VrsLayout = fileRow[70:73]
        self.UsoEmBranco = fileRow[73:250]
    