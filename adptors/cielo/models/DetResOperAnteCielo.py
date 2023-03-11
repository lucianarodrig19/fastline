# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
#Registro 6 - Detalhe dos ROs Antecipados Alelo

class DetResOperAnteCielo:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile #Construtor da classe.
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.NroOperAntecip = fileRow[11:20]
        self.DtVenctoRO = fileRow[20:28]
        self.NroROAnteci = fileRow[28:35]
        self.ParcelaAnteci = fileRow[35:37]
        self.TotalParcelas = fileRow[37:39]
        self.SnlVlrBrutoOrigRO = fileRow[39:40]
        self.VlrBrutoOrigRO = fileRow[40:53]
        self.SnlVlrLiqOrigRO = fileRow[53:54]
        self.VlrLiqOrigRO = fileRow[54:67]
        self.SnlVlrBrutoAnteciRO = fileRow[67:68]
        self.VlrBrutoAnteciRO = fileRow[68:81]
        self.SnlVlrLiqAnteciRO = fileRow[81:82]
        self.VlrLiqAnteciRO = fileRow[82:95]
        self.Bandeira = fileRow[95:98]
        self.NroUnicoRO = fileRow[98:120]
        self.IdROAjstAnteci = fileRow[120:121]
        self.UsoCielo = fileRow[121:250]


       