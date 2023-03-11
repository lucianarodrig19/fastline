# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
#Registro 7 - Detalhe dos Débitos de ROs Antecipados
class DetDebROAntecipado:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.NroUnicoRoOrigVnd = fileRow[11:33]
        self.NroRoAntecipado = fileRow[33:40]
        self.DtPagtoROAntecipado = fileRow[40:48]
        self.SnlVlrROAntecipado = fileRow[48:49]
        self.VlrROAntecipado = fileRow[49:62]
        self.NroUnicoROVendaOriginouAjuste = fileRow[62:84]
        self.NroROAjusteDebito = fileRow[84:91]
        self.DtPagtoAjuste = fileRow[91:99]
        self.SnlVlrAjusteDebito = fileRow[99:100]
        self.VlrAjusteDebito = fileRow[100:113]
        self.SnlVlrCompensado = fileRow[113:114]
        self.VlrCompensado = fileRow[114:127]
        self.SnlSaldoROAntecipado = fileRow[127:128]
        self.VlrSaldoROAntecipado = fileRow[128:141]
        self.UsoCielo = fileRow[141:250]



        