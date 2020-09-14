from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import xlrd
import difflib
book = xlrd.open_workbook("/Users/tetsuo/dev/python/Relacaodegalerias.xls")
gal = book.sheet_by_name("GAL-CUB")
nome = gal.col_values(4)
aprox = []
for a in nome:
    aprox.append(str(a))

print(nome[2])
#print(aprox)
P1 = process.extract("DIEGO ", aprox, limit=20)
print(P1)
print(difflib.get_close_matches("DIEGO", aprox, 3, 0.2))