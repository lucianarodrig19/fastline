#Registro 2 - Detalhe do Comprovante de Venda (CV)
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""

class DetComprovanteVenda:
    
    def __init__(self, fileRow, idfile, idRO): #Construtor da classe.

        self.idFile = idfile
        self.idRO = idRO
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.NroRO = fileRow[11:18]
        self.NroCartaoTruncado = fileRow[18:37]
        self.DtVendaAjuste = fileRow[37:45]
        self.SnlVlrCompraVlrParcela = fileRow[45:46]
        self.VlrCompraVlrParcela = fileRow[46:59]
        self.Parcela = fileRow[59:61]
        self.TotalParcelas = fileRow[61:63]
        self.MotivoRejeição = fileRow[63:66]
        self.CdAutorização = fileRow[66:72]
        self.TID = fileRow[72:92]
        self.NSUDOC = fileRow[92:98]
        self.VlrComplementar = fileRow[98:111]
        self.DigCartao = fileRow[111:113]
        self.VlrTotalVenda = fileRow[113:126]
        self.VlrProximaParcela = fileRow[126:139]
        self.NroNotaFiscal = fileRow[139:148]
        self.TipoCartao = fileRow[148:150]
        self.GrupoCartoes = fileRow[150:152]
        self.NroLogicoTerminal = fileRow[152:160]
        self.IdTxEmbarqueVlrEntrada = fileRow[160:162]
        self.RefCdPedido = fileRow[162:182]
        self.HrTransacao = fileRow[182:188]
        self.NroUnicoTransacao = fileRow[188:217]
        self.IndicadorCieloPromo = fileRow[217:218]
        self.ModoEntradaCartao = fileRow[218:220]
        self.CdVenda = fileRow[220:235]
        self.CdInternoAjuste = fileRow[235:250]
