# Lista kodow pocztowych 1.1
# Tomasz Mering, CODE2.0, 2015r.

kod1 = "79-900"
kod2 = "80-155"
kod1 = int(kod1.replace('-',''))
kod2 = int(kod2.replace('-',''))
lista_kodow = map(str, range(kod1, (kod2 + 1)))
lista_kodow = map(lambda e : (e[0:2] + '-' + e[2:5]), lista_kodow)
print lista_kodow

