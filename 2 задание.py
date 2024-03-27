import csv

# открытие файла
with open('vacancy.csv', encoding='utf-8-sig') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    # сортировка
    for i in range(len(reader)):
        key = reader[i]
        j = i - 1
        while j >= 0 and key['Company_Size'] > reader[j]['Company_Size']:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
    for row in reader:
        # нахождение профессии классного руководителя в базе данных
        if 'классный руководитель' in row['Role']:
            # вывод
            print(
                f'В компании {row['Company']} есть заданная профессия: {row['Role']}, з/п в такой компании составит: {row['Salary']}')
            break
