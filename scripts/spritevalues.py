import pygame



pygame.font.init()

#Fondo

bg = pygame.image.load("assets/sprites/background.png")
bg_big = pygame.transform.scale(bg, (1500, 1500))

#Fondo Menu

bg_menu = pygame.image.load("assets/sprites/background_menu.png")
bg_bigmenu = pygame.transform.scale(bg_menu, (1500, 1500))

#Fondo Seleccion Nave
bg_seleccionave = pygame.image.load("assets/sprites/hangar.png")
bg_bigseleccionave = pygame.transform.scale(bg_seleccionave, (1500, 1500))

#Fondo Seleccion de Nave

nave_sprite = pygame.image.load("assets/sprites/trianglereal.png")
nave_big = pygame.transform.scale(nave_sprite, (500, 500))

nave2_sprite = pygame.image.load("assets/sprites/triangle.png")
nave2_big = pygame.transform.scale(nave2_sprite, (1500, 1500))

nave3_sprite = pygame.image.load("assets/sprites/triangle.png")
nave3_big = pygame.transform.scale(nave3_sprite, (1500, 1500))


#jugador y enemigo

player_sprite = pygame.image.load("assets/sprites/triangle.png")
player_big = pygame.transform.scale(player_sprite, (1500, 1500))

player2_sprite = pygame.image.load("assets/sprites/triangle2.png")
player2_big = pygame.transform.scale(player_sprite, (1500, 1500))

player3_sprite = pygame.image.load("assets/sprites/triangle3.png")
player3_big = pygame.transform.scale(player_sprite, (1500, 1500))

enemy_sprite = pygame.image.load("assets/sprites/enemy.png")
enemy_big = pygame.transform.scale(enemy_sprite, (1500, 1500))

#objetos interactivos

heal_sprite = pygame.image.load("assets/sprites/star_f.png")
heal_big = pygame.transform.scale(heal_sprite, (30, 30))

fakeheal_sprite = pygame.image.load("assets/sprites/star_e.png")
fakeheal_big = pygame.transform.scale(fakeheal_sprite, (30, 30))

#balas

bullet_e_sprite = pygame.image.load("assets/sprites/bullet_e.png")
bullet_e_big = pygame.transform.scale(bullet_e_sprite, (10, 10))

bullet_f_sprite = pygame.image.load("assets/sprites/bullet_f.png")
bullet_f_big = pygame.transform.scale(bullet_f_sprite, (10, 10))

#asteroides

asteroid_s_sprite = pygame.image.load("assets/sprites/asteroid_s.png")
asteroid_s_big = pygame.transform.scale(asteroid_s_sprite, (30, 30))

asteroid_m_sprite = pygame.image.load("assets/sprites/asteroid_m.png")
asteroid_m_big = pygame.transform.scale(asteroid_m_sprite, (65, 65))

asteroid_l_sprite = pygame.image.load("assets/sprites/asteroid_L.png")
asteroid_l_big = pygame.transform.scale(asteroid_l_sprite, (100, 100))

#logo

logo = pygame.image.load("assets/sprites/logo.png")
logo_large = logo_grande = pygame.transform.scale(logo, (350,350))

#fuente menu 

font_title = pygame.font.Font("assets/fonts/space-power-demo.regular.ttf", (64)) 
font_menu = pygame.font.Font("assets/fonts/elemental-end.regular.ttf", (30))
font_menualternative = pygame.font.Font("assets/fonts/elemental-end.regular.ttf", (20))

# (Se utiliza para los controles fuente DejaVuSans ya que es una fuente que admite los simbolos de flechas y barra espaciadora)
font_settings = pygame.font.Font("assets/sprites/DejaVuSans.ttf", (20))
font_ingame = pygame.font.Font("assets/sprites/DejaVuSans.ttf", (25))
font_control = pygame.font.Font("assets/sprites/DejaVuSans.ttf", (40))
font_score = pygame.font.Font("assets/fonts/led_board-7.ttf", (25))