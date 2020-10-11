import fuzzywuzzy as fuzz
import xlrd

book = xlrd.open_workbook("/Users/tetsuo/dev/python/Relacaodegalerias.xls")
gal = book.sheet_by_name("GAL-CUB")
