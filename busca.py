# import fuzzywuzzy as fuzz
from fuzzywuzzy import fuzz, process
import xlrd
import textract
import urllib
import chardet

scr = 90  #score_cutoff
# scrr=fuzz.partial_token_sort_ratio # scorer
scrr= fuzz.WRatio #scorer
book = xlrd.open_workbook("/Users/tetsuo/dev/python/relacaodegalerias.xlsx")
gal = book.sheet_by_name("GAL-CUB")
todosNomes = gal.col_values(3)
doc = xlrd.open_workbook("/Users/tetsuo/dev/python/19-11-2020.xlsx")
text = textract.process("/Users/tetsuo/dev/python/AGENDAMENTO ADVOGADO VIDEOCONFERÊNCIA - 25.11.2020.doc", encoding = 'unicode_escape')
#Utext = unicode(text, 'utf-8')
tabela = doc.sheet_by_index(0)
# print(todosNomes)
print(' numero de colunas: ', tabela.row_len(0))
print('numero de linhas: ', tabela.nrows)
for x in range(tabela.nrows):
    for y in range(tabela.ncols):
        if tabela.cell_value(x,y) != '' and isinstance(tabela.cell_value(x,y), str):
            print(tabela.cell_value(x,y))
            # print(process.extractBests(tabela.cell_value(x,y).strip(), todosNomes, scorer=scrr, score_cutoff = scr))
            if process.extractBests(tabela.cell_value(x,y).strip(), todosNomes, scorer=scrr, score_cutoff = scr):
                print(process.extractBests(tabela.cell_value(x,y).strip(), todosNomes, scorer=scrr, score_cutoff = scr).pop(0)[0])
            else:
                print('No match.')

print(text.split())
print(chardet.detect(text))


