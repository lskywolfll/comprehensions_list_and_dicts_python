
def palindromo(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]

divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]

def run():
    # print(palindromo(""))
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    num = int(num)
    print(divisors(num))
    print("Termino mi programa")

if __name__ == '__main__':
    run()