
from types import NoneType


print(bool())    # FALSE - values / brak elementu lub zera 
print(bool(False)) 
print(bool(0)) 
print(bool(0.0)) 
print(bool("")) 
print(bool(())) 
print(bool([]))
print(bool({}))
print(bool(None))   # None typ none = brak wartości

                # True / każdy inny przypadek
x= 5
print(bool(x))    
print(bool(True)) 
print(bool(1)) 
print(bool(-1)) 
print(bool(1.1)) 
print(bool("x")) 
print(bool((1))) 
print(bool([1]))
print(bool({1})) 