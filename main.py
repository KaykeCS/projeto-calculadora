import math

historical = []


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


def format_calculation(num1, operator, num2, result):
    if operator != 'raiz':
        return f"{num1} {operator} {num2} = {result}"
    else:
        return f"raiz de {num1} = {result}"


def Calculator():
    num1 = get_number()

    if num1 is None:
        return

    operator = get_operator()

    if operator != 'raiz':
        num2 = get_number()
        if num2 is None:
            return
        result = calculate(num1, operator, num2)
        if result is not None:
            calculation = format_calculation(num1, operator, num2, result)
            historical.append(calculation)
            print(f"Resultado: {result}")
    else:
        result = calculate(num1, operator)
        if result is not None:
            calculation = format_calculation(num1, operator, None, result)
            historical.append(calculation)
            print(f"Resultado: {result}")


def display_history():
    print("\nHistórico de Cálculos:")
    for idx, calc in enumerate(historical, 1):
        print(f"{idx}. {calc}")


while True:
    Calculator()

    yes_no = input("Deseja continuar calculando? (sim/não): ")
    if yes_no.lower() != 'sim':
        break

display_history()
