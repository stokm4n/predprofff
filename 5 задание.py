import csv

def hash(s: str):
    alph = 'zxcvbnmlkjhgfdsaqwertyuiop' + 'zxcvbnmlkjhgfdsaqwertyuiop'.upper()
    c = {i: i for i. l in enumerate(alph,1)}
    hash_wal = 0
    



with open('vacancy.csv', encoding='utf-8-sig') as file:
    reader = list(csv.DictReader(file,delimiter=';'))


with open('vacancy.csv', 'w', encoding='utf-8-sig') as file:
    w = csv.DictWriter(file, delimiter=';')
    w.writerow(['Company','Salary','hash'])
    w.writerows(s)