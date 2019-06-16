import json
import uuid
import os
from faker import Faker
fake = Faker()

w = {}
a = []
for x in range(1000000):
    w['userIdentifier'] = str(uuid.uuid4())
    w['country'] = fake.country_code()
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
with open(os.path.join(r"C:\Users\User1\Desktop\Test Data\P", "1M.json"), 'w') as outfile:
    json.dump(e, outfile, indent=2)

