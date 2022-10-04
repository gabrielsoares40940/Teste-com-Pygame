import pygame
from sys import exit

pygame.init()
tela = pygame.display.set_mode((800,400))
pygame.display.set_caption("Jogo")
tempo = pygame.time.Clock()
test_fonte = pygame.font.SysFont('pygame/ComicSansMS3.ttf', 50)

# de fundo
ceu_surface = pygame.image.load('ceu.png')
chao_surface = pygame.image.load('chao.png')
texto_surface = test_fonte.render('Meu jogo', True, 'black')

# personagem
caracol_surface = pygame.image.load('caracol1.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.blit(ceu_surface,(0,0))
    tela.blit(chao_surface,(0,140))
    tela.blit(texto_surface,(300,10))
    tela.blit(caracol_surface,(700,350))
    
    pygame.display.update()
    tempo.tick(60)