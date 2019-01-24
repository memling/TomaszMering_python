# Program 'Kody pocztowe'
# Drukuje listę kodów pocztowych
# Python 2.x

"""
kod1 = "79-900"
kod2 = "80-155"
kod1 = int(kod1.replace('-',''))
kod2 = int(kod2.replace('-',''))
lista_kodow = map(str, range(kod1, (kod2 + 1)))
lista_kodow = map(lambda e : (e[0:2] + '-' + e[2:5]), lista_kodow)
print (lista_kodow)
"""

kod1 = "79-900"
kod2 = "80-155"
kod1 = int(kod1.replace('-',''))
kod2 = int(kod2.replace('-',''))
lista_kodow = map(str, range(kod1, (kod2 + 1)))
lista_kodow = map(lambda e : (e[0:2] + '-' + e[2:5]), lista_kodow)
print (lista_kodow)


raw_input ("\n\nAby zakończyć program, naciśnij klawisz Enter.")
