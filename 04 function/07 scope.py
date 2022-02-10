number = 12 

def test1():           # definiujemy funkcje ktora ma odwolanie do
    print(number)      # globalnej zmiennej 

test1()

def test2():            # w tej funkcji tworzymy lokalna zmienna 
    number = 100        # ktora w tej funkcji jest urzywana lecz nie zmieniamy globalnej
    print(number)

test2()
print(number)

print("-------------------------")

def test3():
    global number       # global zmienia zmienną globalną/ nie tworzy lokalnej
    number = 5
    print(number)
    if 1 == 1:
        number = 6
        print(number)   # global z poczatku funkcji dalej działa dlatego zmieni zmienna globalnie

test3()
print(number)

print("-------------------------")

number = 10

def test4(number):      # ta samma zmienna w funkcji nadpisuje się parametrem
    print(number)
    number = 20         # FUNKCJA zmienia lokalna zmienna
    print(number)       

test4(33)               # globalna zmienna poostaje taka sama 
print(number)
print("-------------------------")

number = 10
def foo():
    print(number)

def bar():
    number = 9              # zdefiniowana lokalnie
    print(number)
    foo()                   # wywołanie funkcji zdefiniowanej wcześnie nie powoduje uzycia lokalnej zmiennej
                            # tylko tej z ktorej funkcja korzystała przy definiowaniu
foo()
bar()    
print("-------------------------")

number = 10
def check1():
    number = 12              
    print(number)
    def check2():        # zdefiniowanie funkcji w funkcji będzie korzystać z lokalnej zmiennej
        print(number)
    check2()                   
                            
check1() 
print(number)


# petle if , try nie tworza lokalnych zmienych tylko globalne  

if 1 ==1:
    data = 100  # jeżeli instrukcja się nie wykona nie stworzy zmiennej globalnej

print(data)