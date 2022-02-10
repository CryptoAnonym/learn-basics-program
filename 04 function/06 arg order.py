

def printCar(brand, / ,name= "concept",*, year = 1960, color = "black"):
    print(brand, name, year, color)




# znak / powoduje że w funkcji parametry przed nim 
# nie moga być wywoływane po nazwie ani zmieniana kolejność 

# znak * powoduje że wywołane parametry za nią muszą być po nazwie
# nie musi być zachowana kolejność 

printCar("Ford", "dowolność" , year= 2010, color="red")

#
#  np. to będzie błędne : 
#  printCar(brand = "Ford", "dowolność" , year= 2010, color="red")