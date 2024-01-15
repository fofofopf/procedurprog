import json
with open('input.json', 'r') as file:
    data = json.load(file)

def calculate_sum_of_products(data):
    result = sum(item['score'] * item['weight'] for item in data)
    return round(result, 3)


print(calculate_sum_of_products(data))

