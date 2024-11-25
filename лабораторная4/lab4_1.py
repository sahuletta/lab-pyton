# TODO решите задачу
from json import load

def task() -> float:
    with open('input.json', 'r') as file:
        data = load(file)
    res = round(sum(el['score'] * el['weight'] for el in data), 3)
    return res

print(task())