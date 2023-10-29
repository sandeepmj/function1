def addNumbers(number1, number2):
	'''
	provide two numbers and i'll add them together
	'''
	return number1 + number2




def helloPerson(name):
	'''
	Enter a name in a string and i will say hello
	'''
	print(f"Hello {name}")



def byePerson(name):
	'''
	enter name as a string and i will say goodbye
	'''
	print(f"Goodbye {name}!")


import requests

def getUrl(url):
	'''
	provide url and i will request it.
	'''
	return requests.get(url)


def globFiles(path):
	'''
	provide path and i will glob its contents
	'''
	return sorted(glob.glob(path))