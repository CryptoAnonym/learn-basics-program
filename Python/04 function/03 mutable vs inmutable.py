# immutable int, float, bool, str, frozenset 
# proba edycji tworzy nowe miejsce w pamięci nie zmianiając 
# poprzedniej wartości początkowej

def modifyStr(strData):
    print(id(strData))   # wartość id początkowa
    strData += "!"
    print(strData)
    print(id(strData))  # wartość id po zmianie


string = "Hello"

modifyStr(string)   # funkcja zmienia miejsce w pamięci i dodaje !

print(string)  # zmienna nie ulega zmianie - dalej odwołuje się do pocżatkowej wartości
print(id(string)) # wartość id początkowa dalej taka sama

print("----------------------------------")

# mutable: list, set, dict
# przy zmianie nie powstaje nowe miejsce w pamięci, zostaje nadpisana 
# czyli zmienia wartość początkową

def modyfyList(listData):
    print(listData)
    print(id(listData))
    listData += [2,3,4]
    print(listData)
    print(id(listData))

jakasLista = [0,1,2]

modyfyList(jakasLista)

print(id(jakasLista))    # wszystkie id pamieci takie same 
                         #ponieważ zawsze nadpisujemy jej wartość przy zmianach
# fukkcja zarezewuje nową wartość tylko wtedy kiedy w niej nadpiszemy 
# zmienna inna wartośćia: czyli np zdefiniujemy wewnątrz niej inna wartość listData 
