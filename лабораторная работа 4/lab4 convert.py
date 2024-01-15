import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = 'output.json'
def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(reader)
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(rows, json_file, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end = '')

                                           # TODO считать содержимое csv файла

                                           # TODO Сериализовать в файл с отступами равными 4
