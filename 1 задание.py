import csv

#открыте файла
with open('vacancy.csv', encoding='utf-8-sig') as file:
    reader = list(csv.DictReader(file, delimiter=';'))[1:]
    #сортировка
    for i in range(len(reader)):
        key = reader[i]
        j = i - 1
        while j >= 0 and key['Salary'] > reader[j]['Salary']:
            reader[j + 1] = reader[j]
            j -= 1
        reader[j + 1] = key
    for i in range(3):
        k = reader[i]
        print(k['Company'] +  '-' + k['Role'], '-' + k['Salary'])
    for c in range(len(reader)):
        key = reader[c]
        j = c - 1
        while j >= 0 and key['Company'] == reader[j]['Company']:
            reader.remove(reader[j])
            j -= 1
        reader[j + 1] = key
    for row in reader:
        del row['Work_Type']
        del row['Company_Size']

#запись в новый файл
with open('vacancy_new.csv', 'w', encoding='utf-8-sig', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['Company','Role','Salary'], delimiter=';')
    w.writeheader()
    w.writerows(reader)