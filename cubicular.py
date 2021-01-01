import spacy 
nlp = spacy.load('pt')
doc = nlp(u'Você encontrou o livro que eu te falei, Carla cristina antunes?')
# for i in doc:
#     print(i.pos_, i.text, i.ents)
#parser = 
lista = list(doc)
print(lista)
print(doc.__dict__)