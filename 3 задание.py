import csv

# открытие файла
with open('vacancy.csv', encoding='utf-8-sig') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    check = True

    while check:
        # ввод названия компании
        company = input('Введите название >>>')
        c = 0
        for row in reader:
            # нахождение названия компании в базе данны=
            if company in row['Company']:
                print(f'В {row['Company']} найдена вакансия: {row['Role']}. З/п составит: {row['Salary']}')
                c += 1
                break
        if c == 0 and company != 'None':
            print('К сожалению, ничего не удалось найти')
        if company == 'None':
            # остановка программы
            check = False
