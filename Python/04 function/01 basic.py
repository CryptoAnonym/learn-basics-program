
def addNr(a,b):         # definiujemy jakąś funkcje z argumentami a, b 
    return a + b

def subNr (a,b):
    return a - b

def miltiplyNr (a,b):
    return a * b

def add4Nr(num1,num2,num3,num4):
    result = num1 + num2 + num3 + num4 
    return result

print(addNr(10,5))      # wyołujemy naszą funkcje
print("-------------------")  

z = 5
y= 12
print(addNr(z,y))       # wywołujemy z zmiennymi
print("-------------------") 

number = subNr(y,z)     # przypisanie funkcji do zmiennej
print(number)
print("-------------------") 


number1 = miltiplyNr(z,y)
print(number1)
print("-------------------") 

sum= add4Nr(3, number, number1,addNr(z,y)) # argumentami mogą być zmienne, funkcje , dane
print(sum)