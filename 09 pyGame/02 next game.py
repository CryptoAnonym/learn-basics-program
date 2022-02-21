import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((1150,720)) # tworzymy okno do gry o rozmiarach (podwojny nawias())


class Player:               # tworzymy klasę z obiektem w grze (gracz)
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("gracz.png") # pobiera obrazek gracza
        self.width = self.image.get_width() # pobiera szerokosc obrazka automatycznie
        self.height = self.image.get_height() # pobiera wysokosc obrazka automatycznie
        self.speed = 4 # nadajemy co ile maja zmieniać sie wspołzedne x, y 
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord,self.width,self.height)

    def tick(self, keys): # wykonuje sie raz na powtorzenie petli
        if keys[pygame.K_w]:
            self.y_cord -= self.speed
        if keys[pygame.K_a]:
            self.x_cord -= self.speed
        if keys[pygame.K_s]:
            self.y_cord += self.speed
        if keys[pygame.K_d]:
            self.x_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord,self.width,self.height)
    
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Cash:                 # tworzymy klase z obiektem w grze (kase)
    def __init__(self):
        self.x_cord = randint(0,1100)      # połozenie banknotu x (troche mniejsze nizokno aby sie zmiesciły)
        self.y_cord = randint(0,680)      # połozenie banknotu y  (troche mniejsze nizokno aby sie zmiesciły)  
        self.image = pygame.image.load("banknot.png")
        self.width = self.image.get_width() 
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord,self.width,self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord,self.width,self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


def main():
    run = True
    player = Player()
    clock = 0
    score = 0
    banknotes = []
    background = pygame.image.load("tlo.png")
    while run:
        clock += pygame.time.Clock().tick(60) / 1000   # ustalamy pdświerzenia pętli na sekunde czyli w tym przypadku fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # jeżeli gracz zamknie okienko przerywamy pętlę
                run = False
        keys = pygame.key.get_pressed()
        if clock >= 2:
            clock = 0
            banknotes.append(Cash())

        player.tick(keys)
        for banknote in banknotes:
            banknote.tick()

        for banknote in banknotes:                           # petla sprawdza kolizje pomiedzy hitbox-em różnych klas (gracza a kasy)
            if player.hitbox.colliderect(banknote.hitbox):
                banknotes.remove(banknote)    # kolizja kasuje banknot z wyswietlania
                score += 1                    #  do wyniku gracza dodaje 1                       



        window.blit(background,(0,0))  
        player.draw()
        for banknote in banknotes:
            banknote.draw()
        pygame.display.update()

 
    print(score)


main()