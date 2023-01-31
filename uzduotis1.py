#Sukurti programą, kuri:
#Prie kiekvieno sakinio "The Zen of Python" žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
#Patarimai:
#Naudoti map (su lambda) arba comprehension, " ".join()

sakinys = "The Zen of Python"

#naujas = map(lambda x: x + "!", sakinys.split())
#print(" ".join(naujas))

naujas = [x + "!" for x in sakinys.split()]
print(" ". join(naujas))