'''
Previsão do Tempo usando API
Por: Ricardo Rocha
deltab@gmail.com
'''

import requests
import json


def menu_principal():
    print('==========================')
    print('CONSULTA DO CLIMA')
    print('==========================')
    cidade = input('Digite o nome da cidade..: ')

    url = 'https://api.hgbrasil.com/weather?key=dadc12b4&city_name=' + cidade + ',SP&array_limit=3&fields=only_results,temp,description,city_name,forecast,max,min,date&key=dadc12b4'

    requisicao = requests.get(url)
    resposta = json.loads(requisicao.text)

    print('Cidade.......:', resposta['city_name'])
    print('Temperatura..:', resposta['temp'])
    print('Data.........:', resposta['date'])
    print('Condição.....:', resposta['description'])
    print('')
    print('Previsão do Tempo:')
    print('========================')
    for previsao in resposta['forecast']:
        data = previsao['date']
        maxima = previsao['max']
        minima = previsao['min']
        descricao = previsao['description']
        print('Data...: ', data)
        print('Máxima.: ', maxima)
        print('Mínima.: ', minima)
        print('Previsão.: ', descricao)
        print('=======================================')

while True:
    menu_principal()