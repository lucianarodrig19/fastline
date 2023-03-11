# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

class CieloFile:
    
    lstHeader = [] 
    lstDetComprovanteVenda = [] 
    lstContaRecebimento = []
    lstDetNegRecebiveis = []
    lstDetOperAnteCielo = []
    lstDetResOperacao = []
    lstDetDebROAntecipado = []
    lstDetResOperAnteCielo = []
    lstDetTransacPix = []
    lstOperacaoRecebiveis = []
    lstResNegRecebiveis = []
    lstResumoOperacao = []
    lstTrailer = []
    
    def addHeader(self, header):
        self.lstHeader.append(header)
    
    def addDetComprovanteVenda(self, detComprovanteVenda):
        self.lstDetComprovanteVenda.append(detComprovanteVenda)
        
    def addContaRecebimento(self, contaRecebimento):
        self.lstContaRecebimento.append(contaRecebimento)
    
    def addDetNegRecebiveis(self, detNegRecebiveis):
        self.lstDetNegRecebiveis.append(detNegRecebiveis)
        
    def addDetOperAnteCielo(self, detOperAnteCielo):
        self.lstDetOperAnteCielo.append(detOperAnteCielo)
    
    def addDetResOperacao(self, detResOperacao):
        self.lstDetResOperacao.append(detResOperacao)
    
    def addDetDebROAntecipado(self, detDebROAntecipado):
        self.lstDetDebROAntecipado.append(detDebROAntecipado)
    
    def addDetTransacPix(self, detTransacPix):
        self.lstDetTransacPix.append(detTransacPix)
        
    def addOperacaoRecebiveis(self, OperacaoRecebiveis):
        self.lstOperacaoRecebiveis.append(OperacaoRecebiveis)
    
    def addResNegRecebiveis(self, resNegRecebiveis):
        self.lstResNegRecebiveis.append(resNegRecebiveis)
        
    def addResumoOperacao(self, resumoOperacao):
        self.lstResumoOperacao.append(resumoOperacao)
    
    def addTrailer(self, trailer):
        self.lstTrailer.append(trailer)
    
