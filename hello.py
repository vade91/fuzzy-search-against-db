import sqlite3
from fuzzywuzzy import fuzz
from operator import itemgetter

pattern = input("Введите имя: ")   #ввод имени

conn = sqlite3.connect('lolwhat.db')
cur = conn.cursor()
cur.execute("select count(payer_id) from PAYERS")
nRows = cur.fetchone()[0]
bestRatio = 0
topNames = []
i=1
while i <= nRows:
    cur.execute("select payer_name from PAYERS where payer_id = " + str(i))
    payName = cur.fetchone()[0]
    RR = fuzz.ratio(pattern, payName)
    topNames.append((RR, payName))
    i = i+1

topNames = sorted(topNames, key=itemgetter(0), reverse=True)
cur.close()
conn.close()
print(topNames[0], topNames[1], topNames[2], sep='\n')