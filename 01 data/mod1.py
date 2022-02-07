
def zlicz(tekst):
    wyrazy = 1
    for i in tekst:
        if i == ' ':
            wyrazy += 1
    return wyrazy
