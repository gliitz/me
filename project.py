import json
import re

def getContacts():
    val = input("Enter the first letter of the contacts name: ")

    contacts = []

    with open('contacts.json',encoding="utf-8") as json_file:
        data = json.load(json_file)
        for p in data:
            if (p['first_name'], p['last_name'], p['contact']) not in contacts:
                contacts.append(
                    (p['first_name'], p['last_name'], p['contact']))
        for tuples in contacts:
            m = re.findall(
                r'\b[{0}{1}]\w+'.format(val.lower(), val.upper()), tuples[0])
            if m:
                print(m[0], tuples[1], tuples[2])


getContacts()
