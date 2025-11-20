import pygame

# Pantalla (Resolucion)
SX = 720
SY = 720


#VELOCIDADES
PLAYER_VEL = 6 #DEFAULT 6
PLAYER_ROTATION_VEL = 5 #DEFAULT 5
PLAYER2_VEL = 8
PLAYER2_ROTATION_VEL = 6 #DEFAULT 5
PLAYER3_VEL = 10
PLAYER3_ROTATION_VEL = 7 #DEFAULT 5


BULLET_VEL = 10 #DEFAULT 10

ASTEROID_VEL = 1 #DEFAULT 1

FAKEHEAL_VEL = 2
HEAL_VEL = 2

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)


# Opciones del menu e inicializacion de selected_option
menu_options = ["Comenzar","Seleccionar Nave", "Opciones", "Controles", "Salir del juego"]
selected_option = 0

# Opciones de Nave
nave_options = ["Leviathan","Astra Nova", "Starlance"]
naveselected_option = 0
#VOLUMEN
SFX_VOLUME_LEVELS = 1
MUSIC_VOLUME_LEVELS = 1

#PROBABILIDAD

STAR_CHANCE = 1000 #1000 MEDIUM | 100 HIGH | 10000 LOW
LIFESTAR_CHANCE = 2500 #2500 MEDIUM | 250 HIGH | 25000 LOW
ASTEROID_CHANCE = 50 #50 MEDIUM | 5 HIGH | 500 LOW

# Variables de juego.py
clock = pygame.time.Clock() 
display = pygame.display.set_mode((SX, SY))
gg = False
lives = 3
score = 0
fire_boost = False
f_boost = -1
isSoundOn = True

player_bullet = []
asteroids = []
stars = []
count = 0

run = True # Bandera del Juego


