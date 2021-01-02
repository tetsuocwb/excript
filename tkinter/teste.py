from fuzzywuzzy import process, fuzz
from tkinter import *
import pprint
import inspect
# lista = ['lucas', 'pamela']
#pprint.pprint(Entry.__dict__.keys())
# #print(lista.process.utils)
pprint(inspect.getmembers(Entry, predicate=inspect.ismethod))