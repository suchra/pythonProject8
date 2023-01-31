expenses = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
            'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}


def choose_coffee(*args):
    for x in args:
        outlay = expenses[x]
        if stocks[0] - outlay[0] >= 0 and stocks[1] - outlay[1] >= 0 and stocks[2] - outlay[2] >= 0:
            stocks[0] -= outlay[0]
            stocks[1] -= outlay[1]
            stocks[2] -= outlay[2]
            return x
    else:
        return 'К сожалению, не можем предложить Вам напиток'


stocks = [7, 5, 3]

drink = ''
while drink != 'q':
    drink = (input('Введите цифру, соответствующую заказываемому напитку:\n\
        Эспрессо       - 1\n\
        Капучино       - 2\n\
        Маккиато       - 3\n\
        Кофе по-венски - 4\n\
        Латте Маккиато - 5\n\
        Кон Панна      - 6\n\
    для выхода нажмите "q"'))
    if drink == '1':
        preference = 'Эспрессо'
    elif drink == '2':
        preference = 'Капучино'
    elif drink == '3':
        preference = 'Маккиато'
    elif drink == '4':
        preference = 'Кофе по-венски'
    elif drink == '5':
        preference = 'Латте Маккиато'
    elif drink == '6':
        preference = 'Кон Панна'
    else:
        exit()
    print('\n' * 20)
    print(choose_coffee(preference), '\n')