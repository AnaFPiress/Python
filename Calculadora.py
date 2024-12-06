num1 = 0
num2 = 0
result = 0
op = ''

while true:
    num1 = float (input('Digite o primeiro número:'))
    op = input('Digite a operação matematica que pretende usar:')
    num2 = float (input('Digite o segundo número:'))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else: 
        print ('Operação não reconhecida!')

    print ('{} {} {} = {}'.format(num1, op, num2, result))

    