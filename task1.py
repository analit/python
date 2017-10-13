listObj = [1, 2, 3, 'owe', 'two', [3, 'three']]
print listObj, type(listObj)

tupleFromList = tuple(listObj)
print tupleFromList, type(tupleFromList)

listFromTuple = list(tupleFromList)
print listFromTuple, type(listFromTuple)

listFromTuple = None
listFromTuple = [element for element in tupleFromList]
print listFromTuple, type(listFromTuple)

dictionaryFromList = dict((str(element), len(listFromTuple)) for element in listFromTuple)
print dictionaryFromList, type(dictionaryFromList)

testDict = dict([[1, 2], [2, 3]])
print(testDict)

dictionaryFromList = None
dictionaryFromList = dict([str(element), len(listFromTuple)] for element in listFromTuple)
print dictionaryFromList, type(dictionaryFromList)

dictionaryFromList = None
dictionaryFromList = {str(element): len(listFromTuple) for element in listFromTuple}
print dictionaryFromList, type(dictionaryFromList)

dictionaryFromTuple = dict((str(element), tupleFromList.count(element)) for element in tupleFromList)
print(dictionaryFromTuple, type(dictionaryFromTuple))