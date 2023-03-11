# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
import os
from models.DetComprovanteVenda import DetComprovanteVenda
from models.DetDebROAntecipado import DetDebROAntecipado
from models.DetOperAnteCielo import DetOperAnteCielo
from models.DetResOperAnteCielo import DetResOperAnteCielo
from models.OperacaoRecebiveis import OperacaoRecebiveis
from models.DetTransacPix import DetTransacPix
from models.ResNegRecebiveis import ResNegRecebiveis
from models.DetNegRecebiveis import DetNegRecebiveis
from models.ContaRecebimento import ContaRecebimento
from services.configurations.config import getRootPathFiles
from models.CieloFile import CieloFile
from models.Header import Header
from models.Trailer import Trailer
from models.DetResOperacao import DetResOperacao
import uuid
    
rootPath = getRootPathFiles()
bufsize = 65536
cieloFile = CieloFile()

def execute():
    idFile = ''
    idRO = ''
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
                            idFile = str(uuid.uuid4())
                            cieloFile.addHeader(Header(line, idFile))

                        if line[:1] == '1' :
                            idRO = str(uuid.uuid4())
                            cieloFile.addDetResOperacao(DetResOperacao(line, idFile, idRO))
                        
                        if line[:1] == '2' :
                            cieloFile.addDetComprovanteVenda(DetComprovanteVenda(line, idFile, idRO))
                        
                        if line[:1] == '3' :
                            cieloFile.addOperacaoRecebiveis(OperacaoRecebiveis(line, idFile))
                        
                        if line[:1] == '5' :
                            cieloFile.addDetOperAnteCielo(DetOperAnteCielo(line, idFile))
                        
                        if line[:1] == '6' :
                            cieloFile.addDetResOperAnteCielo(DetResOperAnteCielo(line, idFile))
                        
                        if line[:1] == '7' :
                            cieloFile.addDetDebROAntecipado(DetDebROAntecipado(line, idFile))
                            
                        if line[:1] == '8' :
                            cieloFile.addDetTransacPix(DetTransacPix(line, idFile))
                        
                        if line[:1] == 'A' :
                            cieloFile.addResNegRecebiveis(ResNegRecebiveis(line, idFile))
                        
                        if line[:1] == 'B' :
                            cieloFile.addDetNegRecebiveis(DetNegRecebiveis(line, idFile))
                        
                        if line[:1] == 'C' :
                            cieloFile.addContaRecebimento(ContaRecebimento(line, idFile))
                            
                        if line[:1] == '9' :
                            cieloFile.addTrailer(Trailer(line, idFile))
                            
                return cieloFile