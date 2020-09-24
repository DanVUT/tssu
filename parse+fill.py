from datetime import datetime
import sqlite3
import xml.etree.ElementTree as ET



tree = ET.parse('export.xml')
root = tree.getroot()
allContracts = []


for item in root:
    date = datetime.strptime(item.find('datum').text, '%Y-%m-%d')
    #date = item.find('datum').text
    contractNumber = item.find('cislo').text
    subject = item.find('predmet').text
    amount = float(item.find('suma').text)
    distributor = item.find('dodavatel').text
    ico = item.find('ico').text
    address = item.find('adresa').text
    allContracts.append((contractNumber, date, subject, amount, distributor, ico, address))

print(len(allContracts))


connection = sqlite3.connect('test.db')
cursor = connection.cursor()

try:
    cursor.execute('DROP TABLE contracts')
except:
    pass
finally:
    cursor.execute('''CREATE TABLE contracts
    (contract_number text, contract_date text,
    subject text, amount real, distributor text, ico text, address text)''')

cursor.executemany('INSERT INTO contracts VALUES(?, ?, ?, ?, ?, ?, ?)', allContracts)
connection.commit()
connection.close()
