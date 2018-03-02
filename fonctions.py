def ma_fonction():
	print("Hello les gens")

ma_fonction()


def ma_fonction(param):
	print(param)

def somme(a, b):
	return a + b 

somme = somme (1,10)
print(somme)

def spat_fonction(*params):
	print(params[0])
	print(params[1])
	print(params[2])
	print(params[3])

spat_fonction(1,2,"salut",3)