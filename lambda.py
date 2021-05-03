from functools import reduce

palindromo = lambda string: string == string[::-1]

numeros = [1,4,5,6,9,13,19,21]

def run():
    # lister = list(filter(lambda x: x % 2 != 0, numeros))
    # list_2 = [1,2,3,4,5]
    list_3 = [2,2,2,2,2]
    # lister2 = [i * i for i in list_2]
    # lister2 = list(map(lambda x: x * x, list_2))

    lister3 = reduce(lambda a,b: a * b, list_3)

    print(lister3)

if __name__ == '__main__':
    run()