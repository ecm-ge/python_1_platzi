items = [
    {
        'nombre': 'camisa',
        'precio': 100
    },
    {
        'nombre': 'pantalon',
        'precio': 50
    },
    {
        'nombre': 'zapatillas',
        'precio': 200
    }
]

prices = list(map(lambda item: item['precio'], items))
print(prices)