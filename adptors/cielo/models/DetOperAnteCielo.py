# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

#Registro 5 - Detalhe da Operação de Antecipação Alelo

class DetOperAnteCielo:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.NroOperAntecip = fileRow[11:20]
        self.DtCredtOper = fileRow[20:28]
        self.SnlVlrBrutoAntecipVista = fileRow[28:29]
        self.VlrBrutoAntecipVista = fileRow[29:42]
        self.SnlVlrBrutoAntecipParc = fileRow[42:43]
        self.VlrBrutoAntecipParc = fileRow[43:56]
        self.SnlVlrBrutoAntecipElectronPreDatado = fileRow[56:57]
        self.VlrBrutoAntecipElectronPreDatado = fileRow[57:70]
        self.SnlVlrBrutoAntecip = fileRow[70:71]
        self.VlrBrutoAntecip = fileRow[71:84]
        self.SnlVlrLiqAntecipVista = fileRow[84:85]
        self.VlrLiqAntecipVista = fileRow[85:98]
        self.SnlVlrLiqAntecipParc = fileRow[98:99]
        self.VlrLiqAntecipParc = fileRow[99:112]
        self.SnlVlrLiqAntecipPreDatado = fileRow[112:113]
        self.VlrLiqAntecipPreDatado = fileRow[113:126]
        self.SnlVlrLiqAntecip = fileRow[126:127]
        self.VlrLiqAntecip = fileRow[127:140]
        self.TxDescAntecip = fileRow[140:145]
        self.Banco = fileRow[145:149]
        self.Agencia = fileRow[149:154]
        self.ContaCorrentePoupanca = fileRow[154:168]
        self.SnlVlrLiqAntecipTotal = fileRow[168:169]
        self.VlrLiqAntecipTotal = fileRow[169:182]
        self.SnlVlrTarifa = fileRow[182:183]
        self.Tarifa = fileRow[183:192]
        self.UsoCielo = fileRow[192:250]

       