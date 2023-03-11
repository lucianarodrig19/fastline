SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

CREATE TABLE `opcao_extrato` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;
 
INSERT INTO `opcao_extrato` (`id`, `description`) VALUES
('03', 'Vendas com Plano Parcelado'),
('04', 'Pagamentos'),
('09', 'Saldo em Aberto'),
('10', 'Antecipação de Recebíveis Alelo'),
('12', 'Vendas Alelo'),
('13', 'Pagamentos Alelo'),
('14', 'Saldo em Aberto Alelo'),
('15', 'Negociação de Recebíveis'),
('16', 'Transações PIX');

CREATE TABLE `tipo_transacao` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `tipo_transacao` (`id`, `description`) VALUES
('01', 'Venda'),
('02', 'Ajuste a Crédito'),
('03', 'Ajuste a Débito'),
('04', 'Plano Cielo'),
('05', 'Reagendamento');


CREATE TABLE `status_pagto` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
  `observation` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `status_pagto` (`id`, `description`, `observation`) VALUES
('00', 'Agendado', 'identifica a captura de uma transação e informa a previsão de pagamento. A data prevista poderá ser alterada.'),
('01', 'Pago', 'identifica que o pagamento foi realizado pelo banco domicílio.'),
('02', 'Enviado para o Banco', 'identifica que a Cielo solicitou o pagamento/cobrança para o banco domicílio, porém não houve confirmação.'),
('03', 'A Confirmar', 'identifica que a Cielo solicitou o pagamento/cobrança para o banco domicílio, porém ainda não houve confirmação.');

CREATE TABLE `produto` 
( `id` VARCHAR(3) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `produto` (`id`, `description`) VALUES
('001', 'Agiplan crédito à vista'),
('002', 'Agiplan parcelado loja'),
('003', 'Banescard crédito à vista'),
('004', 'Banescard parcelado loja'),
('005', 'Esplanada crédito à vista'),
('006', 'Credz crédito à vista'),
('007', 'Esplanada parcelado loja'),
('008', 'Credz parcelado loja'),
('009', 'Elo Crediário'),
('010', 'Mastercard crédito à vista'),
('011', 'Maestro'),
('012', 'Mastercard parcelado loja'),
('013', 'Elo Construcard'),
('014', 'Elo Agro Débito'),
('015', 'Elo Agro Custeio'),
('016', 'Elo Agro Investimento'),
('017', 'Elo Agro Custeio + Débito'),
('018', 'Elo Agro Investimento + Débito'),
('019', 'Discover crédito à vista'),
('020', 'Diners crédito à vista'),
('021', 'Diners parcelado loja'),
('022', 'Visa Agro Custeio + Débito'),
('023', 'Visa Agro Investimento + Débito'),
('024', 'FCO Investimento'),
('025', 'Agro Electron'),
('026', 'Agro Custeio'),
('027', 'Agro Investimento'),
('028', 'Visa FCO Giro'),
('029', 'Visa crediário no crédito'),
('030', 'Visa parcelado cliente'),
('033', 'JCB crédito a vista'),
('036', 'Visa Saque com cartão de Débito'),
('037', 'Flex Car Visa Vale'),
('038', 'Credsystem crédito à vista'),
('039', 'Credsystem parcelado loja'),
('040', 'Visa crédito à vista'),
('041', 'Visa Electron Débito à vista'),
('042', 'Visa Pedágio'),
('043', 'Visa parcelado loja'),
('044', 'Visa Electron Pré-Datado'),
('045', 'Alelo Refeição'),
('046', 'Alelo Alimentação'),
('058', 'Alelo Multibenefícios'),
('059', 'Alelo Auto'),
('060', 'Sorocred débito à vista'),
('061', 'Sorocred crédito à vista'),
('062', 'Sorocred parcelado loja'),
('064', 'Visa Crediário'),
('065', 'Alelo Refeição'),
('066', 'Alelo Alimentação'),
('067', 'Visa Capital de Giro'),
('068', 'Visa Crédito Imobiliário'),
('069', 'Alelo Cultura'),
('070', 'Elo crédito a vista'),
('071', 'Elo débito à vista'),
('072', 'Elo parcelado loja'),
('079', 'Pagamento Carnê Visa Electron'),
('080', 'Visa Crédito Conversor de Moeda'),
('081', 'Mastercard Crédito Especializado (*)'),
('082', 'Amex crédito à vista'),
('083', 'Amex parcelado loja'),
('084', 'Amex parcelado banco'),
('089', 'Elo Crédito Imobiliário'),
('091', 'Elo Crédito Especializado (*)'),
('094', 'Banescard Débito'),
('096', 'Cabal crédito à vista'),
('097', 'Cabal débito à vista'),
('098', 'Cabal parcelado loja'),
('161', 'Hiper crédito à vista'),
('162', 'Hiper débito à vista'),
('163', 'Hiper parcelado loja'),
('164', 'Hipercard crédito à vista'),
('165', 'Hipercard parcelado loja'),
('200', 'Verdecard crédito a vista'),
('201', 'Verdecard parcelado loja'),
('202', 'Nutricash Alimentação'),
('203', 'Nutricash Refeição'),
('204', 'Nutricash Multibenefícios'),
('205', 'Nutricash Combustível'),
('206', 'Ben Alimentação'),
('207', 'Ben Refeição'),
('314', 'Ourocard Agro débito'),
('315', 'Ourocard Agro custeio'),
('316', 'Ourocard Agro investimento'),
('317', 'Ourocard Agro custeio + débito'),
('318', 'Ourocard Agro investimento + débito'),
('321', 'Mastercard crediário no crédito'),
('322', 'Mastercard parcelado cliente'),
('324', 'Elo parcelado cliente'),
('330', 'Elo crediário no crédito'),
('342', 'Mastercard Pedágio'),
('377', 'Elo Carnê'),
('378', 'Mastercard Carnê'),
('380', 'Mastercard Crédito Conversor de Moeda'),
('433', 'JCB parcelado loja');


CREATE TABLE `origem_ajuste` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL ,
  `tipo_ajuste` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;
 
INSERT INTO `origem_ajuste` (`id`, `description`, `tipo_ajuste`) VALUES
('01', 'Acerto de correção monetária', 'Acerto'),
('02', 'Acerto de data de Pagamento', 'Acerto'),
('03', 'Acerto de taxa de comissão', 'Acerto'),
('04', 'Acerto de valores não processados', 'Acerto'),
('05', 'Acerto de valores não recebidos', 'Acerto'),
('06', 'Acerto de valores não reconhecidos', 'Acerto'),
('07', 'Acerto de valores negociados', 'Acerto'),
('08', 'Acerto de valores processados indevidamente', 'Acerto'),
('09', 'Acerto de lançamento não compensado em conta-corrente', 'Acerto'),
('10', 'Acerto referente valores contestados', 'Acerto/Chageback'),
('12', 'Acertos diversos', 'Acerto'),
('13', 'Acordo de cobrança', 'Acerto'),
('14', 'Acordo jurídico', 'Acerto'),
('15', 'Multa do Programa de Bandeira (Master Card)', 'Acerto/Chageback'),
('16', 'Bloqueio de valor por ordem judicial', 'Bloqueio'),
('17', 'Cancelamento da venda', 'Cancelamento'),
('18', 'Cobrança de tarifa Operacional', 'Cobrança'),
('19', 'Valor Mensalidade Farol', 'Acerto / Cobrança'),
('20', 'Cobrança Plano Cielo', 'Cobrança'),
('21', 'Contrato de caução', 'Acerto'),
('22', 'Crédito de devolução do cancelamento banco emissor	Acerto/Cance', 'amento'),
('23', 'Crédito EC referente contestação portador', 'Acerto/Chargeback'),
('24', 'Crédito por cancelamento rejeitado Cielo', 'Acerto/Chargeback'),
('25', 'Processamento do débito duplicado Visa Pedágio', 'Acerto'),
('26', 'Débito por venda realizada sem a leitura do chip', 'Acerto'),
('27', 'Débito por venda rejeitada no sistema Cielo', 'Acerto'),
('28', 'Consumidor não reconhece a compra', 'Acerto/Chargeback'),
('29', 'Estorno de acordo jurídico', 'Acerto'),
('30', 'Estorno de contrato de caução', 'Acerto'),
('31', 'Estorno de acordo de cobrança', 'Acerto'),
('32', 'Estorno de bloqueio de valor por ordem judicial', 'Acerto'),
('33', 'Estorno de cancelamento de venda', 'Acerto'),
('34', 'Estorno de cobrança de tarifa operacional', 'Acerto'),
('35', 'Estorno de cobrança mensal Lynx Comércio', 'Acerto'),
('36', 'Estorno de cobrança Plano Cielo', 'Acerto'),
('37', 'Estorno de débito venda sem a leitura do Chip', 'Acerto'),
('38', 'Estorno de incentivo comercial', 'Acerto'),
('39', 'Multa do Programa de Bandeira (Visa)', 'Acerto/Chargeback'),
('40', 'Estorno de rejeição ARV', 'Acerto'),
('41', 'Estorno de reversão de duplicidade do pagamento - ARV', 'Acerto'),
('42', 'Estorno de tarifa de cadastro', 'Acerto'),
('43', 'Estorno de extrato papel', 'Acerto'),
('44', 'Estorno de processamento duplicado de débito - Visa Pedágio', 'Acerto'),
('45', 'Incentivo comercial', 'Acerto'),
('46', 'Incentivo por venda de Recarga', 'Acerto'),
('47', 'Regularização de rejeição ARV', 'Acerto'),
('48', 'Reversão de duplicidade do pagamento - ARV', 'Acerto'),
('49', 'Tarifa de cadastro', 'Cobrança'),
('50', 'Tarifa de extrato no papel', 'Cobrança'),
('51', 'Aceleração de débito de antecipação', 'Acerto'),
('52', 'Descumprimento de contrato', 'Acerto/Chargeback'),
('53', 'Venda recorrente cancelada pelo consumidor', 'Acerto/Chargeback'),
('54', 'Consumidor não reconhece a compra', 'Acerto/Chargeback'),
('55', 'Cartão com validade vencida', 'Acerto/Chargeback'),
('56', 'Tarifa por retentativa de transações (Master Card)', 'Acerto'),
('57', 'Mercadoria com defeito ou diferente da descrição', 'Acerto/Chargeback'),
('58', 'Transação irregular', 'Acerto/Chargeback'),
('59', 'Mercadoria não foi entregue', 'Acerto/Chargeback'),
('60', 'Serviços não prestados', 'Acerto/Chargeback'),
('61', 'Venda sem código de autorização', 'Acerto/Chargeback'),
('62', 'Número de cartão inválido', 'Acerto/Chargeback'),
('63', 'Cópia do comprovante / documento inválido', 'Acerto/Chargeback'),
('65', 'Comprovante / documento ilegível', 'Acerto/Chargeback'),
('66', 'Venda sem leitura de chip', 'Acerto/Chargeback'),
('67', 'Venda em outra moeda', 'Acerto/Chargeback'),
('68', 'Venda processada incorretamente', 'Acerto/Chargeback'),
('69', 'Venda cancelada', 'Acerto/Chargeback'),
('70', 'Crédito em duplicidade', 'Acerto/Chargeback'),
('71', 'Documentos não recebidos', 'Acerto/Chargeback'),
('72', 'Pagamento realizado por outros	meios', 'Acerto/Chargeback'),
('73', 'Equipamento perdido / roubado', 'Acerto/Cobrança'),
('77', 'Multa por excesso de chargeback', 'Acerto/Chargeback'),
('78', 'Serviços Score', 'Cobrança'),
('79', 'Reagendamento do débito de antecipação', 'Acerto'),
('80', 'Ajuste do débito de cessão', 'Acerto'),
('81', 'Cielo e-Commerce', 'Acerto/Cobrança'),
('85', 'Cielo Controle (Excedente)', 'Acerto/Cobrança'),
('86', 'Cielo Controle (Franquia)', 'Acerto/Cobrança'),
('89', 'Débito/crédito compensação de cancelamento de transação em operação de Penhora', 'Acerto'),
('90', 'Débito/crédito compensação de valores', 'Acerto'),
('91', 'Estorno debito/crédito de cessão', 'Acerto'),
('92', 'Estorno débito/crédito de gravame', 'Acerto'),
('93', 'Meliuz', 'Acerto/Cobrança'),
('94', 'Débito/crédito compensação cancelamento de transação em operação de Cessão', 'Acerto'),
('95', 'Débito/crédito de penhora', 'Acerto'),
('96', 'Estorno de crédito/débito de penhora', 'Acerto'),
('97', 'Débito/crédito compensação cancelamento em operação', 'Acerto'),
('98', 'Débito/crédito compensação cancelamento de transação em operação de gravame', 'Acerto'),
('99', 'Tarifa por retentativa de transações (Visa)', 'Acerto');



CREATE TABLE `bandeira` 
( `id` VARCHAR(3) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `bandeira` (`id`, `description`) VALUES
('001', 'Visa'),
('002', 'Mastercard'),
('003', 'Amex'),
('006', 'Sorocred'),
('007', 'Elo'),
('009', 'Diners'),
('011', 'Agiplan'),
('015', 'Banescard'),
('023', 'Cabal'),
('029', 'Credsystem'),
('035', 'Esplanada'),
('040', 'Hipercard'),
('060', 'Jcb'),
('064', 'Credz'),
('072', 'Hiper'),
('075', 'Ourocard');


CREATE TABLE `meio_captura` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `meio_captura` (`id`, `description`) VALUES
('00', 'LIO'),
('01', 'POS (Point of Sale)'),
('02', 'PDV (Ponto de Venda) ou TEF (Transferência Eletrônica de Fundos)'),
('03', 'e-Commerce (Comércio Eletrônico)'),
('04', 'EDI (Troca Eletrônica de Dados)'),
('05', 'ADP/BSP (Empresa Capturadora) ou Reprocessamento'),
('06', 'Manual'),
('07', 'URA/CVA'),
('08', 'Mobile'),
('09', 'Moedeiro Eletrônico em Rede'),
('99', 'Não identificado');


CREATE TABLE `motivo_rejeicao` 
( `id` VARCHAR(3) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `motivo_rejeicao` (`id`, `description`) VALUES
('002', 'Cartão inválido'),
('023', 'Outros erros'),
('024', 'Tipo cartão inválido'),
('031', 'Transação de saque com cartão Electron valor zerado'),
('039', 'Banco emissor inválido'),
('044', 'Data da transação inválida'),
('045', 'Código de autorização inválido'),
('055', 'Número de parcelas inválido'),
('056', 'Transação financiada para estabelecimento não autorizado'),
('057', 'Cartão em boletim protetor'),
('061', 'Número de cartão inválido'),
('066', 'Transação não autorizada'),
('067', 'Transação não autorizada'),
('069', 'Transação não autorizada'),
('070', 'Transação não autorizada'),
('071', 'Transação não autorizada'),
('072', 'Transação não autorizada'),
('073', 'Transação inválida'),
('074', 'Valor de transação inválido'),
('075', 'Número de cartão inválido'),
('077', 'Transação não autorizada'),
('078', 'Transação não autorizada'),
('079', 'Transação não autorizada'),
('080', 'Transação não autorizada'),
('081', 'Cartão vencido'),
('082', 'Transação não autorizada'),
('083', 'Transação não autorizada'),
('084', 'Transação não autorizada'),
('086', 'Transação não autorizada'),
('091', 'Transação não autorizada'),
('092', 'Banco emissor sem comunicação'),
('093', 'Desbalanceamento no plano parcelado'),
('094', 'Venda parcelada para cartão emitido no exterior'),
('097', 'Valor de parcela menor do que o permitido'),
('099', 'Banco emissor inválido'),
('100', 'Transação não autorizada'),
('101', 'Transação duplicada'),
('102', 'Transação duplicada'),
('124', 'BIN não cadastrado'),
('126', 'Transação de saque com cartão Electron inválida'),
('128', 'Transação de saque com cartão Electron inválida'),
('129', 'Transação de saque com cartão Electron inválida'),
('130', 'Transação de saque com cartão Electron inválida'),
('133', 'Transação de saque com cartão Electron inválida'),
('134', 'Transação de saque com cartão Electron inválida'),
('140', 'Estabelecimento não e-commerce'),
('141', 'Cartão travel transação inválida'),
('143', 'Venda em dólar inválido'),
('145', 'Estabelecimento inválido para distribuição'),
('147', 'Parcelado emissor não habilitado'),
('150', 'Estabelecimento não financeiro');


CREATE TABLE `modo_entrada_cartao` 
( `id` VARCHAR(3) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `modo_entrada_cartao` (`id`, `description`) VALUES
('00', 'Reentrada manual'),
('01', 'Digitada'),
('02', 'Trilha magnética'),
('03', 'Código de barra'),
('04', 'OCR (tecnologia que processa uma imagem e extrai os textos escritos)'),
('05', 'Chip online'),
('06', 'Trilha'),
('07', 'Contactless'),
('81', 'Digitada'),
('90', 'Trilha'),
('91', 'Contactless emulando tarja'),
('95', 'Chip offline');

CREATE TABLE `grupo_cartoes` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;
 

INSERT INTO `grupo_cartoes` (`id`, `description`) VALUES
('00', 'Serviço não atribuído'),
('01', 'Cartão emitido no Brasil'),
('02', 'Cartão emitido no Exterior'),
('03', 'MDR por Tipo de Cartão - Inicial'),
('04', 'MDR por Tipo de Cartão - Intermediário'),
('05', 'MDR por Tipo de Cartão - Superio');


CREATE TABLE `tipo_cartao` 
( `id` VARCHAR(2) NOT NULL  , 
  `description` VARCHAR(255) NOT NULL , 
 PRIMARY KEY (`id`) 
) 
 ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO `tipo_cartao` (`id`, `description`) VALUES
('00', 'Serviço não atribuído'),
('01', 'Visa Classic'),
('02', 'Visa Empresarial'),
('03', 'Visa Gold'),
('04', 'Visa Platinum'),
('05', 'Visa Infinite'),
('06', 'Visa Corporate'),
('07', 'Visa Electron'),
('08', 'Visa Compras'),
('09', 'Master Platinum'),
('10', 'Master Standard'),
('11', 'Master Gold'),
('12', 'Master Pré-Pago'),
('13', 'Master Black'),
('14', 'Master Corporativo'),
('15', 'Master Cartão Viagem'),
('16', 'Master Cartão Benefício'),
('17', 'Master World'),
('18', 'Master Agro'),
('19', 'Elo Bndes'),
('20', 'Elo Classic'),
('21', 'Elo Empresarial'),
('22', 'Elo Insumos'),
('23', 'Elo Corporativo'),
('24', 'Elo Mais'),
('25', 'Elo Grafite'),
('26', 'Elo Nanquim'),
('27', 'Elo Pré Pagos Geral / Gift Card'),
('28', 'Elo Vale Cultura'),
('29', 'Elo Nacional PJ Empresarial'),
('30', 'Elo Compras'),
('31', 'Elo Viagem'),
('32', 'Elo Premiação Inc de Vendas PJ');


CREATE TABLE `Header` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`DtProcessamento` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`DtInicial` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`DtFinal` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`NroSeqArquivo` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`Adquirente` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`TipoExtrato` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`TransmissaoCielo` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`CaixaPostal` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`VrsLayout` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoEmBranco` varchar(177) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetResOperacao` (
	`idFile` varchar(36) not null,
	`idRO` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`NroRO` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`Parcela` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`Filler` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`Plano` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`TpTransacao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`DtApresentacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPrvstaPgto` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`DtVenctoOriginal` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBruto` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBruto` decimal(13,2) ,
	`SnlTxAdmin` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrTxAdmin` decimal(13,2) ,
	`SnlVlrRejeitado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrRejeitado` decimal(13,2) ,
	`SnlVlrLiquido` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiquido` decimal(13,2) ,
	`Banco` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`Agencia` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`CntCorrentePoupanca` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`StatusPagamento` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`QtdeCVsAceitos` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`IndicadorRecebaRapido` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`IndicadorTxMinima` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`QtdeCVsRejeitados` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`IdRevendaAceleracao` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`DtCapturaTransacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`OrigemAjuste` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrComplementar` decimal(13,2) ,
	`IdAntecipacao` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroOperAntecip` varchar(9) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBrutoAntecipado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAntecipado` decimal(13,2) ,
	`Bandeira` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`NroUnicoRO` varchar(22) COLLATE utf8mb4_general_ci NOT NULL,
	`TxAdministrativa` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`TarifaAdministrativa` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`TxRecebaRapido` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`MeioCaptura` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`NroLogicoTerminal` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`CdProduto` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`MtrzPagamento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`ReenvioPagamento` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`ConceitoAplicado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`GrupoCartoes` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`IndicadorSaldoAberto` varchar(1) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetComprovanteVenda` (
	`idFile` varchar(36) not null,
	`idRO` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`NroRO` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`NroCartaoTruncado` varchar(19) COLLATE utf8mb4_general_ci NOT NULL,
	`DtVendaAjuste` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrCompraVlrParcela` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrCompraVlrParcela` Decimal(13,2) ,
	`Parcela` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`TptalParcelas` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`MotivoRejeição` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`CdAutorização` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`TID` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`NSUDOC` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrComplementar` Decimal(13,2) ,
	`DigCartao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrTotalVenda` Decimal(13,2) ,
	`VlrProximaParcela` Decimal(13,2),
	`NroNotaFiscal` varchar(9) COLLATE utf8mb4_general_ci NOT NULL,
	`TipoCartao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`GrupoCartoes` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`NroLogicoTerminal` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`IdTxEmbarqueVlrEntrada` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`RefCdPedido` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`HrTransacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`NroUnicoTransacao` varchar(29) COLLATE utf8mb4_general_ci NOT NULL,
	`IndicadorCieloPromo` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`ModoEntradaCartao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`CdVenda` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
	`CdInternoAjuste` varchar(15) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `OperacaoRecebiveis` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`CdOperacao` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`CPFCNPJTitular` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`CPFCNPJRecebedor` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`CPFCNPJTitularConta` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPagamento` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`DtVenctoOriginal` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`TipoOperacao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`Bandeira` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`TpLiquidacao` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrOperacao` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrOperacao` decimal(17,2) ,
	`CdMoeda` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`Banco` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`Agencia` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`Conta` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(109) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetOperAnteCielo` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`NroOperAntecip` varchar(9) COLLATE utf8mb4_general_ci NOT NULL,
	`DtCredtOper` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBrutoAntecipVista` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAntecipVista` decimal(13,2) ,
	`SnlVlrBrutoAntecipParc` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAntecipParc` decimal(13,2) ,
	`SnlVlrBrutoAntecipElectronPreDatado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAntecipElectronPreDatado` decimal(13,2) ,
	`SnlVlrBrutoAntecip` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAntecip` decimal(13,2) ,
	`SnlVlrLiqAntecipVista` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAntecipVista` decimal(13,2) ,
	`SnlVlrLiqAntecipParc` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAntecipParc` decimal(13,2) ,
	`SnlVlrLiqAntecipPreDatado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAntecipPreDatado` decimal(13,2) ,
	`SnlVlrLiqAntecip` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAntecip` decimal(13,2) ,
	`TxDescAntecip` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`Banco` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`Agencia` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`ContaCorrentePoupanca` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrLiqAntecipTotal` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAntecipTotal` decimal(13,2) ,
	`SnlVlrTarifa` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`Tarifa` varchar(9) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(58) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetResOperAnteCielo` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`NroOperAntecip` varchar(9) COLLATE utf8mb4_general_ci NOT NULL,
	`DtVenctoRO` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`NroROAnteci` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`ParcelaAnteci` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`TotalParcelas` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBrutoOrigRO` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoOrigRO` decimal(13,2) ,
	`SnlVlrLiqOrigRO` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqOrigRO` decimal(13,2) ,
	`SnlVlrBrutoAnteciRO` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAnteciRO` decimal(13,2) ,
	`SnlVlrLiqAnteciRO` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqAnteciRO` decimal(13,2) ,
	`Bandeira` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`NroUnicoRO` varchar(22) COLLATE utf8mb4_general_ci NOT NULL,
	`IdROAjstAnteci` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(129) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetDebROAntecipado` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`NroUnicoRoOrigVnd` varchar(22) COLLATE utf8mb4_general_ci NOT NULL,
	`NroRoAntecipado` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPagtoROAntecipado` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrROAntecipado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrROAntecipado` decimal(13,2) ,
	`NroUnicoROVendaOriginouAjuste` varchar(22) COLLATE utf8mb4_general_ci NOT NULL,
	`NroROAjusteDebito` varchar(7) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPagtoAjuste` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrAjusteDebito` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrAjusteDebito` decimal(13,2) ,
	`SnlVlrCompensado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrCompensado` decimal(13,2) ,
	`SnlSaldoROAntecipado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrSaldoROAntecipado` decimal(13,2) ,
	`UsoCielo` varchar(109) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


CREATE TABLE `DetTransacPix` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`NroEstabelecimento` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
	`TpTransacao` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`DtTransacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`HrTransacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`IDPIX` varchar(36) COLLATE utf8mb4_general_ci NOT NULL,
	`NSUDOC` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPagamento` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBruto` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`ValorBruto` decimal(13,2) ,
	`SnlTxAdmin` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrTxAdmin` decimal(13,2) ,
	`SnlVlrLiq` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiq` decimal(13,2) ,
	`Banco` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`Agência` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`Conta` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`DtCaptTransc` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`TxAdmin` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`TrfaAdmin` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`MeioCaptura` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`NroLogTerminal` varchar(8) COLLATE utf8mb4_general_ci NOT NULL,
	`DtTranscOrig` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`HrTranscOrig` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`IDPIXOrig` varchar(36) COLLATE utf8mb4_general_ci NOT NULL,
	`IndicTrocoSaque` varchar(2) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(31) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
	

CREATE TABLE `ResNegRecebiveis` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`DtNegociacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`DtPagamento` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`CPFCNPJ` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`PrazoMedio` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`TxNominal` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBruto` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrButo` decimal(13,2) ,
	`SnlVlrLiq` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiq` decimal(13,2) ,
	`CdOperacao` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(167) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
	
	

CREATE TABLE `DetNegRecebiveis` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`DtNegociacao` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`DtVenctoOrig` varchar(6) COLLATE utf8mb4_general_ci NOT NULL,
	`CPFCNPJ` varchar(14) COLLATE utf8mb4_general_ci NOT NULL,
	`Bandeira` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`TpLiq` varchar(3) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBruto` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBruto` decimal(13,2) ,
	`SnlVlrLiq` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiq` decimal(13,2) ,
	`TxEfetiva` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`InstFinanceira` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(134) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `ContaRecebimento` (
	`idFile` varchar(36) not null,
	`TpRegistro` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`Banco` varchar(4) COLLATE utf8mb4_general_ci NOT NULL,
	`Agencia` varchar(5) COLLATE utf8mb4_general_ci NOT NULL,
	`Conta` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrDepositado` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrDepositado` varchar(13) COLLATE utf8mb4_general_ci NOT NULL,
	`UsoCielo` varchar(206) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;




CREATE TABLE `Trailer` (
	`idFile` varchar(36) not null,
	`TpRegistr` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`TotalRegistro` varchar(11) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrLiqSomaCVs` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrLiqSomaCVs` decimal(17,2) ,
	`QtdeTotalCVs` varchar(11) COLLATE utf8mb4_general_ci NOT NULL,
	`SnlVlrBrutoSomaROs` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoSomaROs` decimal(17,2) ,
	`SnlVlrBrutoAnteciSomaROs` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`VlrBrutoAnteciSomaROs` decimal(17,2) ,
	`SnlSomaVlrsNegociados` varchar(1) COLLATE utf8mb4_general_ci NOT NULL,
	`SomaVlrsNegociados` decimal(17,2) ,
	`UsoCielo` varchar(155) COLLATE utf8mb4_general_ci NOT NULL)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;