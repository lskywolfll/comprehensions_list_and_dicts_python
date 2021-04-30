

def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firtsname": "Rene",
        "lastname": "Sanchez"
    }

    super_list = [
        {
            "firtsname": "Rene",
            "lastname": "Sanchez"
        },
        {
            "firtsname": "Miguel",
            "lastname": "Torres"
        },
        {
            "firtsname": "Pepe",
            "lastname": "Rodelo"
        },
        
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for i in super_list:
        for key,value in i.items():
            print(f"{key} - {value}")

    # for key,value in super_dict.items():
    #     print(f"{key} - {value}")


if __name__ == '__main__':
    run()
