import math

array_numbers = []
result = None


def get_number():
    while True:
        try:
            num = float(input("Digite um número: "))
            return num
        except ValueError:
            print('Dado inválido. Insira apenas números.')


def get_operator():
    while True:
        operator = input(
            "Digite o operador que deseja utilizar : ")
        if operator in ('+', '-', '*', '/', '**', 'raiz'):
            return operator
        else:
            print('Operador inválido. Insira apenas os operadores válidos.')


def calculate(num1, operator, num2=None):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Erro: Divisão por zero.")
            return None
        else:
            return num1 / num2
    elif operator == '**':
        return num1 ** num2
    elif operator == 'raiz':
        return math.sqrt(num1)


def Calculator():
    global result
    num1 = get_number()

    if num1 is None:
        return

    array_numbers.append(num1)
    operator = get_operator()
    array_numbers.append(operator)

    if operator != 'raiz':
        num2 = get_number()
        if num2 is None:
            return
        array_numbers.append(num2)
    else:
        array_numbers.append(None)

    num1 = array_numbers[0]
    operator = array_numbers[1]

    result = calculate(num1, operator, array_numbers[2])
    if result is not None:
        print(f"Resultado: {result}")


while True:
    Calculator()

    yes_no = input("Deseja continuar calculando? (sim/não): ")
    if yes_no.lower() != 'sim':
        break
