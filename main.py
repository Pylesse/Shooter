import pygame
pygame.init()

# generer la fenetre du jeu
pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

# importer et charger l'arriere plan
background = pygame.image.load("assets/bg.jpg")

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan de notre jeu
    screen.blit(background, (0,-200))

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")