
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding='utf8') as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)
        

def write():
    names = ["Nicolas", "Rene", "Fernando", "Juan", "Michael"]

    with open("./archivos/names.txt", "w", encoding='utf8') as f:
        for name in names:
            f.write(f"{name}\n")

def run():
    read()
    write()

if __name__ == '__main__':
    run()