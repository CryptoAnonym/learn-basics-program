
def addNr(a,b,c):
    return a + b + c 

def sumListElements(listData):
    if len(listData) == 0:
        return "Pusta lista"
    result = 0

    for v in listData:
        result += v
    return result

print(sumListElements([]))
print(sumListElements([1,2,3,4,5]))
print("--------------------------")
def printList(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)
    return 
    # lub wychodzi z funkcji
    # zwraca dane (nie musi zawsze być kiedy nie zwracamy wartości )

printList([])
printList([1,2,3,4,5,6,7])
print("--------------------------")
