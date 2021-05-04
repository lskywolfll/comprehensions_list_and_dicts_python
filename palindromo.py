# from math import isnan
from utils.inputs import get_input

palindromo = lambda string: string == string[::-1]

def run():
    text = get_input(str, "Ingresa un texto: ", "Por favor ingresa un texto valido")
    contains_number = text.isdigit()

    if len(text) == 0:
        raise ValueError("No se puede ingresar una cadena vacia")

    if contains_number:
        raise ValueError("No se pueden ingresar numeros")

    validate_msg = palindromo(text)
    if validate_msg:
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()