
from operator import index
from functions import checker 
from functions import  edit



print('|------------------------------------------|')
print('|---Bienvenidos a la maquina espendedora---|')
print('|------------------------------------------|')
print('|----------[0]Papitas--$25 pesos-----------|')
print('|----------[1]Agua-----$10 pesos-----------|')
print('|----------[2]Refresco-$25 pesos-----------|')
print('|----------[3]Jugos----$50 pesos-----------|')
print('|----------[4]Galletas-$10 pesos-----------|')
print('|------------------------------------------|')
print('|-Nota: Solo aceptamos monedas de 10-25-50-|')
print('|------------------------------------------|')


def index():
    Condition = True
    while Condition == True:
        money = input('Introduca las monedas: ')
        if money == 50 or money ==10 or money == 25:
            Condition = False    
    products = input('Cual producto deseas: ')
    checker(products, money)

index()
    