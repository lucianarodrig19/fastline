# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
class Trailer:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.TotalRegistro = fileRow[1:12]
        self.SnlVlrLiqSomaCVs = fileRow[12:13]
        self.VlrLiqSomaCVs = fileRow[13:30]
        self.QtdeTotalCVs = fileRow[30:41]
        self.SnlVlrBrutoSomaROs = fileRow[41:42]
        self.VlrBrutoSomaROs = fileRow[42:59]
        self.SnlVlrBrutoAnteciSomaROs = fileRow[59:60]
        self.VlrBrutoAnteciSomaROs = fileRow[60:77]
        self.SnlSomaVlrsNegociados = fileRow[77:78]
        self.SomaVlrsNegociados = fileRow[78:95]
        self.UsoCielo = fileRow[95:250]
