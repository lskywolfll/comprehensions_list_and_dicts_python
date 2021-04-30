
def run():

    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    challenge = [i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(challenge)
    # squares = []
    # # quiero crear una lista de los 100 numeros al cuadrado
    # # Desafio: guardar el cuadrado de los numeros que no sean divisibles entre 3
    # for i in range(1,101):
    #     result = i ** 2

    #     if result % 3 != 0:
    #         squares.append(result)
    
    # print(squares)

if __name__ == '__main__':
    run()