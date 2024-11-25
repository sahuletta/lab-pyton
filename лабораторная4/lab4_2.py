# TODO импортировать необходимые молули
from csv import DictReader
from json import dump

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME,'r') as input:
        table = DictReader(input, delimiter=',', quotechar='\n')
        list_from_csv = list(row for row in table)

    with open(OUTPUT_FILENAME, 'w') as output:
        dump(list_from_csv, output, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
