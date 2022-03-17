# operatory tożsamości is sprawdza czy dana zmienna 
# odwołuje się do tej samej zarezerwowanej pamieci

strData = "test"

print(dir(strData)) # funkcja dir wywołuje informacje o obiekcie

print(strData.upper()) # np upper() - wielkie znaki zmennej

intData = 10
print(dir(intData))

print("------------------")

a = [1,2,3,4,5]
b = a
print(a is b)

a.append(77)
print (a)

print(id(a))
print(id(b))

print (b)
print(a is not b) # obie zmienne wskazują te same miejsce w pamięć