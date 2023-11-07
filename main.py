addition = "+"
subtraction = "-"
multiplication = "*"
division = "/"


def Calculator():
    n1 = int(input("Digite um número: "))

    quest_operator = input(
        "Digite o operador que deseja utilizar: (+) (-) (*) (/) \n"
    )

    result = None
    n2 = int(input("Digite outro número: "))

    if quest_operator == addition:
        result = n1 + n2
    elif quest_operator == subtraction:
        result = n1 - n2
    elif quest_operator == multiplication:
        result = n1 * n2
    elif quest_operator == division:
        result = n1 / n2
    else:
        print("Operador inválido.")

    if result is not None:
        print(f"Resultado: {result}")


ex_calculator = Calculator()
