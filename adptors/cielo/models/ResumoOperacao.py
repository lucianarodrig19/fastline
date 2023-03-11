# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 03 2023

@author: Luciana
"""
class ResumoOperacao:
    
    def __init__(self, fileRow, idfile): #Construtor da classe.

        self.idFile = idfile
        self.TpRegistro = fileRow[:1]
        self.NroEstabelecimento = fileRow[1:11]
        self.NroRO = fileRow[11:18]
        self.Parcela = fileRow[18:20]
        self.Filler = fileRow[20:21]
        self.Plano = fileRow[21:23]
        self.TpTransacao = fileRow[23:25]
        self.DtApresentacao = fileRow[25:31]
        self.DtPrvstaPgto = fileRow[31:37]
        self.DtVenctoOriginal = fileRow[37:43]
        self.SnlVlrBruto = fileRow[43:44]
        self.VlrBruto = fileRow[44:57]
        self.SnlTxAdmin = fileRow[57:58]
        self.VlrTxAdmin = fileRow[58:71]
        self.SnlVlrRejeitado = fileRow[71:72]
        self.VlrRejeitado = fileRow[72:85]
        self.SnlVlrLiquido = fileRow[85:86]
        self.VlrLiquido = fileRow[86:99]
        self.Banco = fileRow[99:103]
        self.Agencia = fileRow[103:108]
        self.CntCorrentePoupanca = fileRow[108:122]
        self.StatusPagamento = fileRow[122:124]
        self.QtdeCVsAceitos = fileRow[124:130]
        self.IndicadorRecebaRapido = fileRow[130:131]
        self.IndicadorTxMinima = fileRow[131:132]
        self.QtdeCVsRejeitados = fileRow[132:138]
        self.IdRevendaAceleracao = fileRow[138:139]
        self.DtCapturaTransacao = fileRow[139:145]
        self.OrigemAjuste = fileRow[145:147]
        self.VlrComplementar = fileRow[147:160]
        self.IdAntecipacao = fileRow[160:161]
        self.NroOperAntecip = fileRow[161:170]
        self.SnlVlrBrutoAntecipado = fileRow[170:171]
        self.VlrBrutoAntecipado = fileRow[171:184]
        self.Bandeira = fileRow[184:187]
        self.NroUnicoRO = fileRow[187:209]
        self.TxAdministrativa = fileRow[209:213]
        self.TarifaAdministrativa = fileRow[213:218]
        self.TxRecebaRapido = fileRow[218:222]
        self.MeioCaptura = fileRow[222:224]
        self.NroLogicoTerminal = fileRow[224:232]
        self.CdProduto = fileRow[232:235]
        self.MtrzPagamento = fileRow[235:245]
        self.ReenvioPagamento = fileRow[245:246]
        self.ConceitoAplicado = fileRow[246:247]
        self.GrupoCartoes = fileRow[247:249]
        self.IndicadorSaldoAberto = fileRow[249:250]
        