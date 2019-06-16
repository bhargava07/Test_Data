import json
import uuid
import glob
import os
import shutil
from datetime import datetime

d = {}
mob = {}


def is_exist(k):
    if k in mob.keys():
        value = mob[k]
    else:
        value = str(uuid.uuid4())
        mob[k] = value
    return value


i = 100000
for file_path in glob.iglob(r"C:\Users\User1\Desktop\Test Data\Test\*.json"):
    a = file_path.split("_")
    json_file = open(file_path, 'r', encoding='utf-8')
    file = json.load(json_file)
    json_file.close()
    mobileAppIdentifier = file['header']['device']['uniqueIdentifier']
    country = a[-1][:2]
    d['metadata'] = {'dataId': {}, 'upload': {}}
    d['metadata']['dataId']["country"] = country
    d['metadata']['dataId']['mobileAppIdentifier'] = mobileAppIdentifier[1:-1]
    d['metadata']['dataId']['userIdentifier'] = is_exist(mobileAppIdentifier[1:-1])
    d['metadata']['upload']['identifier'] = str(uuid.uuid1())
    d['metadata']['upload']['uploadDate'] = datetime.today().strftime('%Y-%m-%d')
    x = d['metadata']['dataId']['userIdentifier']
    meta_filename = (x + '--%s.meta.json' % i)
    raw_filename = (x + '--%s.raw.json' % i)
    i += 1
    with open(os.path.join(r"C:\Users\User1\Desktop\Test Data\Output", meta_filename), 'w') as outfile:
        json.dump(d, outfile, indent=2)
    with open(os.path.join(r"C:\Users\User1\Desktop\Test Data\Output", raw_filename), 'w') as out:
        json.dump(file, out, indent=2)
    print(d)

shutil.make_archive(data, 'zip', dir_name)
