num = 0

while True:
    print("Wprowadź liczbę lub exit aby zakończyć")
    strData = input()
    if strData == "exit" : break
    num = num + int(strData)
    print("Wartość po dodaniu liczby: " + str(num))

