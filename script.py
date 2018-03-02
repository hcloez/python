
maListe = [1,2,3]
print(maListe)

maListe2 =[]

maListe2.append(1)
print(maListe2)
maListe2.append("Salut")
print(maListe2)

listeTest = ["1er", "deuxième", "troiseme"]

#del listeTest[1]
print(listeTest)

print(listeTest.count("1er"))
print(listeTest.index("1er"))

NouvelleListe = ["1er", "deuxeme", "troisieme"]
secondeList = NouvelleListe[:]
NouvelleListe[0] = "toto"
print(secondeList)

print("1e5r" in secondeList)

NouvelleListe = range(15)
print(NouvelleListe)
liste = range(10)
liste.extend(NouvelleListe)
print(liste)