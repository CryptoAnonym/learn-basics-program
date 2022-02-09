# if jeżeli ( wyświetla tylko wtedy kiedy jest prawdą)
#elif jeżeli if nie jest spełniony przechodzi do elif które nie musi być spełnone aby przeszedł dalej

#else w każdej innej sytuacji 
num = 1

if num >= 3:
    print("Num jest wieksze lub równe 3")
    print("oraz kolejny blok kodu")
if num == 5:
    print("Num jest rowne 5") # warunkie się nie wykluczają

if num == 1:
    print("Num jest równe 1." ) # if wykonane tylko gdy prawda 
elif num == 2:
    print("Num równe jest 2")   # elif wykonuje się aż osiągnie prawdę 
elif num <= 0:
    print("Num jest ujemne lub 0")
else:                      # else wykona się kiedy żadne powyższe fukcje sie nie są prawdą
    print("Num jest wieksze od 2")
    
if 1==1:
     print("Przęchodzę do sprawdzania Num")
     if num > 0:
        print("Num jest wieksze od 0")      # blok kodu gdzie kolejny warynek sprawdzany po wykonaniu pierwszego
            
