# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
import os
from cielo.models.DetComprovanteVenda import DetComprovanteVenda
from models.DetDebROAntecipado import DetDebROAntecipado
from models.DetOperAnteCielo import DetOperAnteCielo
from models.DetResOperAnteCielo import DetResOperAnteCielo
from models.OperacaoRecebiveis import OperacaoRecebiveis
from models.DetTransacPix import DetTransacPix
from models.ResNegRecebiveis import ResNegRecebiveis
from models.DetNegRecebiveis import DetNegRecebiveis
from models.ContaRecebimento import ContaRecebimento
from configurations.config import getRootPathFiles
from models.CieloFile import CieloFile
from models.Header import Header
from models.Trailer import Trailer
from models.DetResOperacao import DetResOperacao
    
rootPath = getRootPathFiles()
bufsize = 65536
cieloFile = CieloFile()

def execute():

    for diretorio, subpasta, arquivos in os.walk(rootPath["cielo"] + "/recebido"):
        for arquivo in arquivos:
            print(os.path.join(diretorio, arquivo))
            with open(os.path.join(diretorio, arquivo)) as infile: 
                while True:
                    lines = infile.readlines(bufsize)
                    if not lines:
                        break
                    for line in lines:
                        #process(line)        
                        if line[:1] == '0' :
                            cieloFile.addHeader(Header(line))
                        
                        if line[:1] == '1' :
                            cieloFile.addDetResOperacao(DetResOperacao(line))
                        
                        if line[:1] == '2' :
                            cieloFile.addDetComprovanteVenda(DetComprovanteVenda(line))
                        
                        if line[:1] == '3' :
                            cieloFile.addOperacaoRecebiveis(OperacaoRecebiveis(line))
                        
                        if line[:1] == '5' :
                            cieloFile.addDetOperAnteCielo(DetOperAnteCielo(line))
                        
                        if line[:1] == '6' :
                            cieloFile.addDetResOperAnteCielo(DetResOperAnteCielo(line))
                        
                        if line[:1] == '7' :
                            cieloFile.addDetDebROAntecipado(DetDebROAntecipado(line))
                            
                        if line[:1] == '8' :
                            cieloFile.addDetTransacPix(DetTransacPix(line))
                        
                        if line[:1] == 'A' :
                            cieloFile.addResNegRecebiveis(ResNegRecebiveis(line))
                        
                        if line[:1] == 'B' :
                            cieloFile.addDetNegRecebiveis(DetNegRecebiveis(line))
                        
                        if line[:1] == 'C' :
                            cieloFile.addContaRecebimento(ContaRecebimento(line))
                            
                        if line[:1] == '9' :
                            cieloFile.addTrailer(Trailer(line))
                return cieloFile