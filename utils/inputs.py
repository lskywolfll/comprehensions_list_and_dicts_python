def get_input(typ, msg, err):
    while True:
        try:
            return typ(input(msg))
        except ValueError:
            print("{0}".format(err))
        except TypeError:
            print("Solo se pueden ingresar strings")