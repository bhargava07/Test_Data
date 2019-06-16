import json
import glob
import os
from faker import Faker
fake = Faker()

s = set()
d = {}
for file_path in glob.iglob(r"C:\Users\User1\Desktop\Test Data\Output\*.meta.json"):
    json_file = open(file_path, 'r', encoding='utf-8')
    file = json.load(json_file)
    json_file.close()
    x = file['metadata']['dataId']['userIdentifier']
    country = file['metadata']['dataId']['country']
    s.add(x)
    d[x] = country

w = {}
a = []
for i in s:
    w['userIdentifier'] = i
    if i in d.keys():
        w['country'] = d[i]
    w['devOrTestUser'] = str(fake.boolean(chance_of_getting_true=10)).lower()
    w['firstName'] = fake.first_name()
    w['middleInitial'] = ''
    w['lastName'] = fake.last_name()
    w['nameSuffix'] = ''
    w['email'] = fake.email()
    w['dateOfBirth'] = str(fake.date_between(start_date='-48y', end_date='-18y'))
    a.append(w.copy())


e = {"users": a}
print(e)
with open(os.path.join(r"C:\Users\User1\Desktop\Test Data\Output", 'flash_reports.json'), 'w') as outfile:
    json.dump(e, outfile, indent=2)
