def greet(name,msg):
    print(name,msg)

greet('더조은', '좋은하루')


def welcome(city,name='Guest', room=None):
    room.append(101)
    print(f'Hello {name}, This is {city}')

welcome('seoul')