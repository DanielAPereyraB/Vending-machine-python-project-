from variables import values

def checker(product, money):
    if values.amount[product] > 0:       
        if values.price[product] < money:
            edit(product, money)
        else:
            print('El dinero no es suficiente')
    else:
        print('No hay ',values.products[product])  
               
       
def edit(product, money):
    values.amount[product] = values.amount[product] - 1
    back = money - values.price[product]
    print('Gracias por su compra')
    return_money(back)

def return_money(num):
    total = num
    mon25 = 0
    mon10 = 0
    mon5 = 0

    while num >= 25:
        mon25 += 1
        num-=25

    while num >= 10:
        mon10 += 1
        num-=10

    while num >= 5:
        mon5 += 1
        num-=5
    print('Su devuelta es de ',mon25,' monedas de 25',mon10 ,'monedas de 10',mon5,'monedas de 5 con un total de ',total,' pesos')
