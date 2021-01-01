import xlrd

from fuzzywuzzy import fuzz, process

book = xlrd.open_workbook("/Users/tetsuo/dev/python/Relacaodegalerias.xls")
lista_test = ['Diego arthur joao', 'lucas matsuo antunes', 'Pamela Antunes', 'Joao Vitor', 'Jose diego Barcelo']
a = fuzz.partial_ratio('Diego ', "Diego arthur antunes")
b = fuzz.ratio('diego ', "Diego arthur antunes")
c = fuzz.token_sort_ratio('Diego ', "Diego arthur antunes") #ignores order
print(a,b,c)
gal = book.sheet_by_name("GAL-CUB")
todosNomes = gal.col_values(4)
nome = "runes"
print(nome.upper())
#resultado = process.extract(nome, todosNomes, scorer= fuzz.partial_token_sort_ratio, score_cutoff= 89 , limit=10 )
resultado = process.extract(nome, todosNomes, scorer= fuzz.partial_token_sort_ratio,  limit=10 ) #scorer= fuzz.token_sort_ratio,
#partial_token_sort_ratio
print(resultado)
