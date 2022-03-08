from datetime import datetime
from bs4 import BeautifulSoup
import os
from SIS2 import XML

pasta = "C:/Users/adm/Desktop/programa/python/Python 3/projeto/Ja"
os.chdir(pasta)

print('CARREGANDO SEUS XMLs, aguarde...\n')

lista = []
for file in os.listdir():
    x = open(file)
    x = BeautifulSoup(x, "xml")
    if x.det != None:
        x = XML(x)
        lista.append(x)
    else:
        if x.descEvento.contents == ['Cancelamento']:
           for y in lista:
               if x.chNFe.contents == y.CHAVENF:
                   lista.remove(y)

#O SCRIPT ACIMA FAZ A LEITURA DAS XML DE ACORDO COM A PASTA SELECIONADA E O CONVERTE PARA OBJETO DE ACORDO COM
#O METODO CRIADO, É NECESSARIO ADCIONAR XML DE CANCELAMENTO PARA RESULTADO PRECISO, ESTE QUANDO ENCONTRA UMA XML 
#COM TAG DE CANCELAMENTO RETEM SUA CHAVE DE ACESSO E COMPARA COM AS JA ADCIONADAS NA LISTA DE CLASSIFICADOS E RETIRA O OBJETO

def CFOP(lista, cfop):
    cfopl = cfop
    y= 0
    for x in lista:
        vtcfop = 0
        for z in range(len(x.CFOP)):
            for a in cfopl:
                if x.CFOP[z] == a :
                    vtcfop += float(x.VALORTP[z][0]) + float(x.IPIU[z][0]) 
                    y+= float(x.VALORTP[z][0]) + float(x.IPIU[z][0])
                    if x.CFOP[z] is x.CFOP[-1]:
                        print(f'|{x.NNF[0].rjust(4)}|{x.DATAE[0][0:10].rjust(10)}|{x.CLIENTE[0][0].rjust(55)}|R$ {str(vtcfop).rjust(10)}|{x.CFOP[z][0].rjust(4)}|')
    print(f'|R$ {str(y).rjust(10)}|')                
                    
                     
#A DEF ACIMA PODE PARECER CONFUSA MAS SAO APENAS VALORES DE OBJETOS EM LISTA COM INDICES, ENTENDA QUE AS LISTAS 
#FORAM FEITAS PARA TRABALHAR COM O MESMO NUMERO DE INDICES, OU SEJA SE NECESSARIO O CFOP DO  VALOR DA LISTA
#ESTE SE ENCONTRARA NO MESMO INDICE = X.CFOP[Y][0] , X.VALORTP[Y][0]


def CONTAGEM_MESES(lista,data):
    meses = []
    for x in lista:
        meses[(int(x.DATAE[0][5:7]))-1].append(x)
    return meses
        
    

def criar_lista(x):
    matriz = []
    for y in range(x):
        matriz.append([])
    return matriz


def maiorvalor(x):
    b = x[0]
    for x in x:
        if (float(x.VALORT[0][0])) > float(b.VALORT[0][0]):
            b = x
    return b     

#ACIMA ALGUMAS FUNCOES NAO UTILIZADAS       


def datas(lista, datai, dataf):
    datsel = []
    d2 = datetime.strptime(dataf, '%Y-%m-%d')
    d1 = datetime.strptime(datai, '%Y-%m-%d')
    for x in lista:
        if datetime.strptime(x.DATAE[0][:10], '%Y-%m-%d') >= d1 and datetime.strptime(x.DATAE[0][:10],'%Y-%m-%d') <=d2:
            datsel.append(x)
    return datsel        
           

#ACIMA A FUNCAO RETORNA VALORES CLASSIFICADOS POR DATA, PARAMETROS FORNECIDOS PELO MAIN()

            
def imprimir(lista):
    y = 0
    for x in lista: 
        y += (float(x.VALORP[0][0]) + float(x.IPIT[0][0]))
        print(f'|{x.NNF[0].rjust(4)}|{x.DATAE[0][0:10].rjust(10)}|{x.CLIENTE[0][0].rjust(55)}|R$ {str(float(x.VALORP[0][0]) + float(x.IPIT[0][0])).rjust(10)}|{str(x.CFOP[0][0]).rjust(4)}|')
    print(f'|R$ {str(y).rjust(10)}|')
        
# ACIMA FUNCAO USADA SE O USUARIO NAO DESEJAR FILTRAR CFOP



def main():
    print('')
    print('SEJA BEM VINDO AO SIS2.')
    print('')
    print('TODAS AS XML EM SUA PASTA FORAM CARREGADAS')
    print('')
    print('1º. FATURAMENTO POR DATA')
    print('')
    option = int( input('Digite a opção desejada.\n'))
    if option == 1 :
        print('')
        var0 = input('Digite a data inicial no padrão 000A-0M-0D \n')
        var1 = input('Digite a data final. o padrão 000A-0M-0D\n')
        print('')
        var2 = input('Deseja categorizar valores baseados em CFOP? Se sim pressione (s) .\n')
        if var2 == 's':
            c= 0
            cfops = []
            x = input('Digite o CFOP desejado:\n')
            cfops.append([x])
            while c==0:
                x = input('Digite outro CFOP desejado; se não necessario pressione (n).\n')
                if x == 'n' :
                    c=1 
                cfops.append([x])
            print('FATURAMENTO')
            x =  CFOP((datas(lista,var0,var1)), cfops)
        else:
            print('FATURAMENTO')
            x = datas(lista,var0,var1)
            imprimir(x)
            

       
        datas(lista, var0, var1)

#ACIMA O MAIN EXECUTA UM FATURAMENTO CLASSIFICADO POR DATA E FILTRO DE CFOP, SE O USUARIO SEGUIR EXATAMENTE O 
#INDICADO RETORNA UMA TABELA E FINALIZA O PROGRAMA, MAS POR SE TRATAR DE CONCEITO DE ESTUDO SUA PREVISIBILIDADE 
#É MUITO FRAGIL

main()
   



