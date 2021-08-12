import requests
from bs4 import BeautifulSoup
from time import sleep as lp
from flask import jsonify

class CnpjRequest:
    def __init__(self):
        self.cnpj_nome = ''
        pass

    @staticmethod
    def Request(cnpj_nome):
        global titulos, informacoes
        url = requests.get(f'https://www.informecadastral.com.br/cnpj/{cnpj_nome}/')
        soup = BeautifulSoup(url.content, 'html.parser')
        titulos = soup.find_all('h3', attrs={'class': 'mb-0'})
        informacoes = soup.find_all('p', attrs={'class': 'mb-0'})
        return titulos, informacoes

    def get_data(self, cnpj_number):
        self.cnpj_nome = cnpj_number.replace('.', '').replace('/', '').replace('-', '')
        self.Request(cnpj_number)

        print('\n!!! Buscando informações no banco de dados !!!\n')
        lp(2)
        titulosLista = []
        lista = []  # resultados dos dados cnpj, APENAS OS RESULTADOS
        limit = None
        lenT = len(titulos)
        lenL = len(informacoes)
        data = None
        print(lenL, lenT)

        if lenT > lenL:
            for x in range(lenL):
                titulosLista.append(titulos[x].text.replace(':', '').replace('Ç', 'C').replace('Ã', 'A').replace('Ó', 'O').replace('Í', 'I').replace('Á', 'A'))
                lista.append(informacoes[x+1].text.replace(':', '').replace('Ç', 'C').replace('Ã', 'A').replace('Ó', 'O').replace('Í', 'I').replace('Á', 'A'))

            data = dict(tuple(zip(titulosLista, lista)))
        else:
            for x in range(lenT):
                titulosLista.append(titulos[x].text.replace(':', '').replace('Ç', 'C').replace('Ã', 'A').replace('Ó', 'O').replace('Í', 'I').replace('Á', 'A'))
                lista.append(informacoes[x+1].text.replace(':', '').replace('Ç', 'C').replace('Ã', 'A').replace('Ó', 'O').replace('Í', 'I').replace('Á', 'A'))

            data = dict(tuple(zip(titulosLista, lista)))
        print(data)
        cnpj_dict = data
        return jsonify(cnpj_dict)


# 97.422.620/0001-50
# 97422620000150
# 01.472.720/0003-84
# 17493833000134

