import csv

#открываем файл
with open('vacancy.csv', encoding='utf-8-sig') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    s = set()
    for row in reader:
        s.add(row['Work_Type'])
    s = sorted(s)
    sw = []

    for row in reader:
        su = 0
        for g in range(len(s)):
            if row['Work_Type'] == s[g]:
                su += int(row['Salary'])
        sw.append(su)
    sp = []
    for row in reader:
        for g in range(len(s)):
            if row['Work_Type'] == s[g]:
                row['Persent'] = (str(sw[g] / int(row['Salary']) * 100)[:str(sw[g] / int(row['Salary']) * 100).find('.')] + '%')
                sp.append(row)

#записыаем в новый файл
with open('vacancy_persent.csv', 'w', encoding='utf-8-sig', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['Salary', 'Work_Type', 'Company_Size', 'Role', 'Company','Persent'],delimiter=';')
    w.writeheader()
    w.writerows(sp)