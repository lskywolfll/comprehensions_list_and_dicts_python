divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]

def get_input(msg):
    while True:
        try:
            result = int(input(msg))

            if result < 0:
                print("No se admiten numeros negativos 😭\n")
                raise ValueError()
            else:
                return result

        except ValueError:
            print("Por favor ingresar un numero valido")

def run():
    num = get_input("Ingresa un numero: ")
    print(divisors(num))
    print("Termino mi programa")

if __name__ == "__main__":
    run()