
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70},DATA))

    # Challenge One for usign filter and map to: all_python_devs and all_platzi_workers
    # Complete
    all_python_devs_filtr = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs_filtr = list(map(lambda worker: worker["name"], all_python_devs_filtr))

    all_platzi_workers_filtr = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers_filtr = list(map(lambda worker: worker["name"], all_platzi_workers_filtr))

    # print({
    #     "devs": all_python_devs_filtr,
    #     "workers": all_platzi_workers_filtr
    # })
    
    # Challenge Two using list comprehensions in: old_people and adults
    old_people_comprhnsons = [worker | { "old": worker["age"] > 70 } for worker in DATA]
    old_people_comprhnsons = [worker["old"] for worker in old_people_comprhnsons]

    adults_2 = [worker["name"] for worker in DATA if worker["age"] > 18]
    


if __name__ == '__main__':
    run()