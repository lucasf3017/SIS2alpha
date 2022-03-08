

def INFO (xml, x, y):
    keys = [
        'xProd', 'NCM', 'CFOP', 'uCom', 'qCom', 'vUnCom', 'vProd', 'infAdProd', 'pICMS', 'vICMS',
        'pIPI', 'vIPI', 'pPIS', 'vPIS', 'pCOFINS', 'vCOFINS', 'vBC', 'CPF', 'CNPJ', 'xNome', 
        'xLgr', 'nro', 'xBairro', 'xMun', 'UF', 'xPais', 'IE', 'vNF', 'vol', 'qVol', 'pesoL', 'pesoB', 'infCpl',
        'chNFe', 'dest', 'total', 'det'
    ]
    mylist0 = []
    mylist1 = xml.find_all(keys[y])
    for itm in mylist1:
        myvar = itm.find(keys[x])
        if myvar != None:
            mylist0.append(myvar.contents)
        else:
            mylist0.append(['0']) 
    return mylist0             
                

# A DEF ACIMA ADICIONA OS ATRIBUTOS ABAIXOS USANDO INDICES FORNECIDOS PELO ATRIBUTO, REPARE QUE AO ADCIONAR 
#OU REMOVER UMAS DAS PALAVRAS DA LISTA TODAS AS OUTRAS PERDEM O INDICE CORRETO ENTAO CUIDADO AO USO;
#NA PRIMEIRA INDICE E RECOMENDADO USAR A TAG DO OBEJETO NA XML, CASO TENHA MAIS DE UM OBJETO COM A MESMA TAG
#A SEGUNDA SE POE O VALOR DE PAI DA PRIMEIRA TAG, PERCEBA QUE AS ULTIMAS 3 TAGS INDEXADAS GERALMENTE COM [-1,-2,-3]
#SAO AS MAIS UTILIZADAS COMO PAI

class XML:

    def __init__(self,xml):

        self.CPF = INFO(xml, 17, -3)
        self.CNPJ = INFO(xml, 18, -3)
        self.CLIENTE = INFO(xml, 19, -3)
        self.ENDERECO = INFO(xml, 20, -3)
        self.NUMERO =   INFO(xml, 21, -3)
        self.BAIRRO = INFO(xml, 22, -3)
        self.MUNICIPIO = INFO(xml, 23, -3)  
        self.UF = INFO(xml, 24, -3)
        self.PAIS = INFO(xml, 25, -3)
        self.IE = INFO(xml, 26, -3)
        
        self.CHAVENF = xml.chNFe.contents
        self.NNF = xml.ide.nNF.contents
        self.DATAE = xml.ide.dhEmi.contents
        self.OBS = INFO(xml, 32, 32)

        self.PRODUTO = INFO(xml, 0, -1)
        self.NCM = INFO(xml, 1, -1)
        self.CFOP = INFO(xml, 2, -1)
        self.UNIDADE = INFO(xml, 3, -1)
        self.QUANTIDADE = INFO(xml, 4, -1)
        self.VALORU = INFO(xml, 5, -1)
        self.VALORTP = INFO(xml, 6, -1) 
        self.DESCRICAO = INFO(xml, 7, -1)

        self.ICMSPU = INFO(xml, 8, -1)
        self.ICMSU = INFO(xml, 9, -1)
        self.IPIPU = INFO(xml, 10, -1)
        self.IPIU = INFO(xml, 11, -1) 
        self.PISPU = INFO(xml, 12, -1)
        self.PISU = INFO(xml, 13, -1)
        self.COFINSPU = INFO(xml, 14, -1)
        self.COFINSU = INFO(xml, 15, -1) 

        self.ICMSBCT = INFO(xml, 16, -1)
        self.ICMST = INFO(xml, 9, -2)
        self.IPIT = INFO(xml, 11, -2)
        self.PIST = INFO(xml, 13, -2)   
        self.COFINST = INFO(xml, 15, -2) 
        self.VALORP = INFO(xml, 6, -2)
        self.VALORT = INFO(xml, 27, -2)
 
        self.VOLUME = INFO(xml, 29, 28)
        self.PESOL = INFO(xml, 30, 28)
        self.PESOB = INFO(xml, 31, 28)
        
       

