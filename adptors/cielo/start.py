

import os.path
import sys

__file__ = "D:\\Hackaton Bradesco\\fastfinance\\adptors\\cielo\\start.py"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.chdir(os.path.dirname(__file__))
os.getcwd()

from models.DetComprovanteVenda import DetComprovanteVenda
from datetime import datetime

from models.DetComprovanteVenda import DetComprovanteVenda
from models.ResumoOperacao import ResumoOperacao
from models.OperacaoRecebiveis import OperacaoRecebiveis
from models.Header import Header


import services.insDetResOperacao as insDetResOperacao
import services.insDetComprovanteVenda as insDetComprovanteVenda
import services.insOperacaoRecebiveis as insOperacaoRecebiveis
import services.insDetOperAnteCielo as insDetOperAnteCielo
import services.putCieloPayments as cielo
import services.readCieloFiles as readFile
import services.insHeader as insHeader
import services.insTrailer as insTrailer


inicio = datetime.now()
print('Inicio : ' + inicio.strftime("%d/%m/%Y %H:%M:%S.%f"))

while True:
   
    cieloFile = readFile.execute()
    insHeader.execute(cieloFile.lstHeader)
    insDetResOperacao.execute(cieloFile.lstDetResOperacao)
    insDetComprovanteVenda.execute(cieloFile.lstDetComprovanteVenda)
    insOperacaoRecebiveis.execute(cieloFile.lstOperacaoRecebiveis)
    #insDetOperAnteCielo.execute(cieloFile.lstDetOperAnteCielo)
    insTrailer.execute(cieloFile.lstTrailer)
    
    
    fim = datetime.now()
    print('Inicio : ' + inicio.strftime("%d/%m/%Y %H:%M:%S.%f"))
    print('Termino: ' + fim.strftime("%d/%m/%Y %H:%M:%S.%f"))
    print('Duração: ' + str(fim - inicio))
    break




