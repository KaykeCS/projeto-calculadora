array_numbers = []
result = None


def Calculator():
    global result

    n1 = float(input("Digite um número: "))
    array_numbers.append(n1)

    quest_operator = input(
        "Digite o operador que deseja utilizar -> (+) (-) (*) (/) :\n "
    )
    array_numbers.append(quest_operator)

    n2 = float(input("Digite outro número: "))
    array_numbers.append(n2)

    if len(array_numbers) >= 3:
        n1 = array_numbers[0]
        quest_operator = array_numbers[1]
        n2 = array_numbers[2]

        if quest_operator == '+':
            result = n1 + n2
        elif quest_operator == '-':
            result = n1 - n2
        elif quest_operator == '*':
            result = n1 * n2
        elif quest_operator == '/':
            if n2 == 0:
                print("Não é possível dividir por zero.")
            else:
                result = n1 / n2
        else:
            print("Operador inválido.")

        if result is not None:
            print(f"Resultado: {result}")
    else:
        print("Não há números suficientes na lista para calcular.")


def Delete_calcs():
    del_calc = input('Deseja apagar os cálculos ? \n (sim)  ou  (não) : ')

    if del_calc.lower() == 'sim':
        array_numbers.clear()
        print("Cálculos apagados.")
    else:
        print("Cálculos não foram apagados.")


Calculator()
Delete_calcs()
