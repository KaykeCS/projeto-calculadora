array_numbers = []
result = None


def get_number():
    try:
        num = float(input("Digite um número: "))
        return num
    except ValueError:
        print('Dados inválidos. Insira apenas números.')
        return None


def get_operator():
    while True:
        operator = input(
            "Digite o operador que deseja utilizar (+) (-) (*) (/): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        else:
            print('Operador inválido. Insira apenas os operadores válidos.')


def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Não é possível dividir por zero.")
            return None
        else:
            return num1 / num2


def Calculator():
    global result

    num1 = get_number()
    if num1 is None:
        return
    array_numbers.append(num1)

    operator = get_operator()
    array_numbers.append(operator)

    num2 = get_number()
    if num2 is None:
        return
    array_numbers.append(num2)

    if len(array_numbers) >= 3:
        num1 = array_numbers[0]
        operator = array_numbers[1]
        num2 = array_numbers[2]

        result = calculate(num1, operator, num2)
        if result is not None:
            print(f"Resultado: {result}")
    else:
        print("Não há números suficientes na lista para calcular.")


while True:
    Calculator()

    yes_no = input("Deseja continuar calculando? (sim/não): ")
    if yes_no.lower() != 'sim':
        break
