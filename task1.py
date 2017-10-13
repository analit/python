listObj = [1, 2, 3, 'owe', 'two', [3, 'three']]
print listObj, type(listObj)

tupleFromList = tuple(listObj)
print tupleFromList, type(tupleFromList)

listFromTuple = list(tupleFromList)
print listFromTuple, type(listFromTuple)

listFromTuple = None
listFromTuple = [element for element in tupleFromList]
print listFromTuple, type(listFromTuple)

testDict = dict([[1, 2], [2, 3]])
print(testDict)

# dictionary from list
dictionaryFromList = dict((str(element), len(listFromTuple)) for element in listFromTuple)
print dictionaryFromList, type(dictionaryFromList)

dictionaryFromList = dict.fromkeys([str(el) for el in listFromTuple], len(listFromTuple))
print dictionaryFromList, type(dictionaryFromList)

dictionaryFromList = dict([str(element), len(listFromTuple)] for element in listFromTuple)
print dictionaryFromList, type(dictionaryFromList)

dictionaryFromList = {str(element): len(listFromTuple) for element in listFromTuple}
print dictionaryFromList, type(dictionaryFromList)

# dictionary from tuple
dictionaryFromTuple = dict((str(element), tupleFromList.count(element)) for element in tupleFromList)
print(dictionaryFromTuple, type(dictionaryFromTuple))