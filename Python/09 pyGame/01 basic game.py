import pygame

pygame.init()

window = pygame.display.set_mode((800,600)) # tworzymy okno do gry o rozmiarach (podwojny nawias())

x = 200
y = 200
player = pygame.rect.Rect(x,y,10,10)    # tworzymy obiekt 

run = True

while run:
    pygame.time.Clock().tick(60)    # ustalamy pdświerzenia pętli na sekunde czyli w tym przypadku fps

    for event in  pygame.event.get():
       if event.type == pygame.QUIT:  # jeżeli gracz zamknie okienko przerywamy pętlę
           run = False


    speed = 5
    keys = pygame.key.get_pressed() # zczytuje cała klawiature do listy

    if keys[pygame.K_RIGHT]: # czy strzałka w prawo jest naduszona 
        x += speed
    if keys[pygame.K_LEFT]: # czy strzałka w lewo jest naduszona 
        x -= speed
    if keys[pygame.K_UP]:  #czy strzałka do góry jest naduszona 
        y -= speed
    if keys[pygame.K_DOWN]:  #czy strzałka w dół jest naduszona 
        y += speed
    
    player = pygame.rect.Rect(x,y,10,10)
    
    window.fill((33, 155, 204))  # nadajemy kolor tła okienka
    pygame.draw.rect(window, (20,200,20), player) # umieszczamy nasz obiekt w grze  i jego kolor 
    pygame.display.update()