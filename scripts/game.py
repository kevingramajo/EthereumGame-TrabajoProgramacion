import pygame
import math
import random
from .spritevalues import *
from .sfx import *


pygame.init() # inicializa todos los módulos de Pygame que sean necesarios para ejecutar un juego o aplicación (display, font, event)
pygame.mixer.init()
pygame.display.set_caption("Asteroids")


class Player():
    """
    Representa al jugador en el juego.

    Atributos:
        img (pygame.Surface): Imagen del jugador.
        w (int): Ancho del Jugador Sprite.
        h (int): Altura del Jugador Sprite.
        x (int): Coordenada X actual del jugador (centrada horizontalmente).
        y (int): Coordenada Y actual del jugador (centrada verticalmente).
        angle (float): Ángulo de rotación actual del jugador en grados.
        rotateSprite (pygame.Surface): Imagen del jugador rotada según el ángulo actual.
        rotateRect (pygame.Rect): Rectángulo de colisión del sprite del jugador rotado.
        cos (float): Coseno del ángulo del jugador (usado para cálculos de movimiento y rotación).
        sin (float): Seno del ángulo del jugador (usado para cálculos de movimiento y rotación).
        head (tuple): Coordenadas de la "cabeza" del jugador (usadas como origen de las balas).
        rect (pygame.Rect): Rectángulo de colisión usado para detectar colisiones con asteroides y balas.
    """

    def __init__(self):
        """
        Inicializa al jugador en la posicion por defecto, orientacion, sprites.
        """
        self.img = player_sprite
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SX // 2  # Centra al jugador Horizontalmente en la pantalla
        self.y = SY // 2  # Centra al jugador verticalmente en la pantalla
        
        self.angle = 0  # Ángulo de rotación inicial
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)

        # Calcular el coseno y seno inicial para el movimiento
        self.cos = math.cos(math.radians(self.angle + 90)) 
        self.sin = math.sin(math.radians(self.angle + 90))
        
        # Determine la posición de la "cabeza" del jugador (usada para disparar balas)
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2)
        self.rect = pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)  #Rectángulo de colisión #default: - - | current: + +

    def update_rect(self) -> None:
        """
        Actualiza la posición del rectángulo de colisión para que coincida con la posición actual del jugador.
        """
        self.rect.center = (self.x, self.y)

    def draw(self, display) -> None:
        """
    Dibuja el sprite del jugador rotado en la ventana del juego.

    Argumentos:
    display (pygame.Surface): La superficie del juego donde se dibuja el jugador.
        """
        display.blit(self.rotateSprite, self.rotateRect)

    def rotate_left(self) -> None:
        """Rota al jugador hacia la izquierda a una velocidad de rotación fija."""
        self.angle += PLAYER_ROTATION_VEL
        self.update_sprite()

    def rotate_right(self) -> None:
        """Rota al jugador hacia la derecha a una velocidad de rotación fija."""
        self.angle -= PLAYER_ROTATION_VEL
        self.update_sprite()

    def move_forward(self) -> None:
        """Mueve al jugador hacia adelante en la dirección que está mirando."""
        self.x += self.cos * PLAYER_VEL
        self.y -= self.sin * PLAYER_VEL
        self.wrap_screen()
        self.update_sprite()

    def move_backwards(self) -> None:
        """Mueve al jugador hacia atrás en la dirección que está mirando."""
        self.x -= self.cos * PLAYER_VEL
        self.y += self.sin * PLAYER_VEL
        self.wrap_screen()
        self.update_sprite()

    def wrap_screen(self) -> None:
        """Teletransporta al jugador si sale por los bordes de la pantalla."""
        if self.x < 0:
            self.x = SX
        elif self.x > SX:
            self.x = 0
        if self.y < 0:
            self.y = SY
        elif self.y > SY:
            self.y = 0

    def update_sprite(self) -> None:
        """Actualiza la imagen, el rectángulo rotado y las coordenadas del jugador."""
        self.rotateSprite = pygame.transform.rotate(self.img, self.angle)
        self.rotateRect = self.rotateSprite.get_rect()
        self.rotateRect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.w // 2, self.y + self.sin * self.h // 2)
        self.update_rect()  # Actualiza el rectángulo de colisión

class Bullet():
    """
    Representa una bala disparada por el jugador.

    Atributos:
    img (pygame.Surface): Imagen de la bala.
    point (tuple): Coordenadas iniciales de la bala (posición del "cañón" del jugador).
    x (float): Coordenada x actual de la bala.
    y (float): Coordenada y actual de la bala.
    w (int): Ancho de la imagen de la bala.
    h (int): Altura de la imagen de la bala.
    cos (float): Valor del coseno de la dirección del disparo (basado en la orientación del jugador).
    sin (float): Valor del seno de la dirección del disparo (basado en la orientación del jugador).
    velx (float): Velocidad horizontal de la bala.
    vely (float): Velocidad vertical de la bala.
    rect (pygame.Rect): Rectángulo de colisión de la bala.
    """
    def __init__(self):
        """
        Inicializa una bala disparada desde la posición y la orientación del jugador.
        """
        self.img = bullet_f_big
        self.point = player.head
        self.x, self.y = self.point
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.cos = player.cos
        self.sin = player.sin
        self.velx = self.cos * BULLET_VEL
        self.vely = self.sin * BULLET_VEL
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Collision rectangle

    def move(self) -> None:
        """
        Mueve la bala en la dirección calculada y actualiza su rectángulo de colisión.
        """
        self.x += self.velx
        self.y -= self.vely
        self.rect.topleft = (self.x, self.y)  # Update the position of the rectangle

    def draw(self, display) -> None:
        """
    Dibuja la bala en la ventana del juego.

    Argumentos:
    display (pygame.Surface): La ventana del juego donde se dibuja la bala.
        """
        display.blit(self.img, (self.x, self.y))

class Asteroid():
    """
    Representa un asteroide en el juego.

    Atributos:
    rango (int): El tamaño del asteroide (3 = grande, 2 = mediano, 1 = pequeño).
    imagen (pygame.Surface): La imagen del asteroide según su tamaño.
    w (int): El ancho de la imagen del asteroide.
    h (int): La altura de la imagen del asteroide.
    ran_point (tuple): La posición aleatoria inicial del asteroide fuera de la pantalla.
    x (int): La coordenada x actual del asteroide.
    y (int): La coordenada y actual del asteroide.
    rect (pygame.Rect): El rectángulo de colisión del asteroide.
    dirx (int): La dirección inicial del asteroide en el eje x (-1 o 1).
    diry (int): La dirección inicial del asteroide en el eje y (-1 o 1).
    velx (int): La velocidad horizontal del asteroide.
    vely (int): La velocidad vertical del asteroide.
    """
    def __init__(self, rank: int):
        """
    Inicializa un asteroide con un tamaño y posición aleatorios.

    Args:
    rank (int): El tamaño del asteroide (3 = grande, 2 = mediano, 1 = pequeño).
        """
        self.rank = rank
        if self.rank == 1:
            self.image = asteroid_s_big
        elif self.rank == 2:
            self.image = asteroid_m_big
        else:
            self.image = asteroid_l_big
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.ran_point = random.choice([
            (random.randrange(0, SX - self.w), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, SY - self.h))
        ])
        self.x, self.y = self.ran_point
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)  # Collision rectangle
        if self.x < SX // 2:
            self.xdir = ASTEROID_VEL
        else:
            self.xdir = -ASTEROID_VEL
        if self.y < SY // 2:
            self.ydir = ASTEROID_VEL
        else:
            self.ydir = -ASTEROID_VEL
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)

    def move(self) -> None:
        """
    Mueve el asteroide en la dirección y velocidad actuales, y actualiza su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Update the position of the rectangle

    def draw(self, display) -> None:
        """
    Dibuja el asteroide en la ventana del juego.

    Args:
    display (pygame.Surface): La ventana del juego donde se dibuja el asteroide.
        """
        display.blit(self.image, (self.x, self.y))

class Star():
    """
    Representa una estrella que puede aparecer en el juego y tiene dos posibles efectos:
    - Aumenta la capacidad de disparo del jugador.
    - Reduce las vidas del jugador.

    Atributos:
    img (pygame.Surface): Imagen de la estrella.
    w (int): Ancho de la imagen de la estrella.
    h (int): Altura de la imagen de la estrella.
    ran_point (tuple): Posición aleatoria inicial de la estrella fuera de la pantalla.
    x (int): Coordenada x actual de la estrella.
    y (int): Coordenada y actual de la estrella.
    dirx (int): Dirección inicial en el eje x (1 o -1).
    diry (int): Dirección inicial en el eje y (1 o -1).
    velx (int): Velocidad en el eje x.
    vely (int): Velocidad en el eje y.
    rect (pygame.Rect): Rectángulo de colisión de la estrella.
    effect (str): Tipo de efecto de la estrella ('boost' para poder de fuego, 'lesslife' para disminuir la vida).
    """
    def __init__(self):
        """
        Inicializa una estrella con una posición aleatoria fuera de la pantalla y un efecto aleatorio.
        """
        self.img = fakeheal_big
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Genera coordenadas iniciales
        self.ran_point = random.choice([
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determina la direccion
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocidad
        self.xv = self.xdir * FAKEHEAL_VEL
        self.yv = self.ydir * FAKEHEAL_VEL

        # Colision de Rectangulos
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Determina al azar si la estrella dará un aumento de poder de fuego o reducirá una vida
        self.effect = random.choice(['boost', 'lesslife'])

    def move(self) -> None:
        """
        Actualiza la posición de la estrella y su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Actualizar el rectángulo de colisión

    def draw(self, display) -> None:
        """
    Dibuja la estrella en la ventana del juego.

    Args:
    display (pygame.Surface): La superficie del juego donde se dibuja la estrella.
        """
        display.blit(self.img, (self.x, self.y))

class LifeStar():
    """
    Representa una estrella que restaura 1 vida al jugador al colisionar.

    Atributos:
    img (pygame.Surface): Imagen de la estrella.
    w (int): Ancho de la imagen de la estrella.
    h (int): Altura de la imagen de la estrella.
    ran_point (tuple): Posición inicial aleatoria de la estrella fuera de la pantalla.
    x (int): Coordenada x actual de la estrella.
    y (int): Coordenada y actual de la estrella.
    dirx (int): Dirección inicial en el eje x (1 o -1).
    diry (int): Dirección inicial en el eje y (1 o -1).
    velx (int): Velocidad en el eje x.
    vely (int): Velocidad en el eje y.
    rect  (pygame.Rect): Rectángulo de colisión de la estrella.
    effect (str): Tipo de efecto de la estrella ('morelife' para restaurar vida).
    """
    def __init__(self) -> None:
        """
        Inicializa una estrella con una posición aleatoria fuera de la pantalla y el efecto 'morelife'.
        """
        self.img = heal_big 
        self.w = self.img.get_width()
        self.h = self.img.get_height()

        # Generar coordenadas iniciales
        self.ran_point = random.choice([  # Estrella apareciendo en el borde de la pantalla.
            (random.randrange(0, max(1, SX - self.w)), random.choice([-1 * self.h - 5, SY + 5])),
            (random.choice([-1 * self.w - 5, SX + 5]), random.randrange(0, max(1, SY - self.h)))
        ])

        self.x, self.y = self.ran_point

        # Determina la dirección de la estrella
        self.xdir = 1 if self.x < SX // 2 else -1
        self.ydir = 1 if self.y < SY // 2 else -1

        # Velocidad
        self.xv = self.xdir * HEAL_VEL
        self.yv = self.ydir * HEAL_VEL

        # Rectángulo de colisión
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        # Efecto de la estrella (restaurar vida)
        self.effect = 'morelife'

    def move(self) -> None:
        """
       Actualiza la posición de la estrella y su rectángulo de colisión.
        """
        self.x += self.xv
        self.y += self.yv
        self.rect.topleft = (self.x, self.y)  # Update collision rectangle

    def draw(self, display) -> None:
        """
    Dibuja la estrella en la ventana del juego.

    Argumentos:
    display (pygame.Surface): La superficie del juego donde se dibuja la estrella.
        """
        display.blit(self.img, (self.x, self.y))

def redraw_game_window() -> None:
    """
    Vuelve a dibujar todos los elementos del juego en la ventana del juego.

    Esta función actualiza la pantalla del juego dibujando el fondo, el jugador, 
    las balas, los asteroides, las estrellas y los elementos de la interfaz como vidas 
    y puntuación. También se encarga de mostrar los indicadores de mejoras y el mensaje 
    de "Juego Terminado" cuando sea aplicable.
    """

    display.blit(bg_big, (0, 0))
    lives_text = font_score.render('VIDAS: ' + str(lives), 1, (255, 255, 255))
    play_again_text = font_ingame.render('Apreta \u2423 para volver a jugar', 1, (255,255,255))
    score_text = font_score.render('SCORE: ' + str(score), 1, (255,255,255))
    player.draw(display)
    for pb in player_bullet:
        pb.draw(display)
    for a in asteroids:
        a.draw(display)
    for s in stars:
        s.draw(display)
    
    if fire_boost:
        pygame.draw.rect(display, (0, 0, 0), [SX//2 - 51, 19, 102, 22])
        pygame.draw.rect(display, (255, 255, 255), [SX//2 - 50, 20, 100 - 100*(count - f_boost)/500, 20])

    if gg:
        display.blit(play_again_text, (SX // 2 - play_again_text.get_width() // 2, SY // 2 - play_again_text.get_height() // 2))
    display.blit(lives_text, (25, 25))
    display.blit(score_text, (SX - score_text.get_width() - 10, 25))  
    pygame.display.update()



def save_score(name: str, score: int) -> None:
    """
    Agrega el nombre y la puntuación del jugador a un archivo de texto llamado 'scores.txt'.

    Args:
    nombre (str): El nombre del jugador.
    puntuación (int): La puntuación del jugador.
    """
    with open("puntuaciones.txt", "a") as file:
        file.write(f"{name}: {score}\n")


def read_scores() -> list:
    """
    Lee las puntuaciones del archivo 'puntuaciones.txt' y las devuelve como una lista de tuplas.

    Devuelve:
    list: Una lista de tuplas que contienen los nombres de los jugadores y sus puntuaciones, o una lista vacía si no se encuentra el archivo.
    """
    try:
        with open("puntuaciones.txt", "r") as file:
            scores = []
            for line in file:
                name, score = line.strip().split(": ")
                scores.append((name, int(score)))
            return scores
    except FileNotFoundError:
        return []

player = Player()

def show_game_over_screen() -> None:
    """
    Muestra la pantalla de 'Fin del juego' donde el jugador puede ingresar su nombre 
    y guardar su puntuación. También reinicia el juego cuando el jugador presiona 'Enter'.
    """
    global run, gg
    input_active = True
    name = ""

    while input_active:
        display.fill((0, 0, 0))  # Pantalla en Negro
        display.blit(bg_big , (0, 0))
        game_over_text = font_menu.render("GAME OVER", True, (255, 255, 255))
        enter_name_text = font_menu.render("Ingresa tu nombre:", True, (255, 255, 255))
        name_text = font_menu.render(name, True, (255, 255, 255))

        display.blit(game_over_text, (SX // 2 - game_over_text.get_width() // 2, 100))
        display.blit(enter_name_text, (SX // 2 - enter_name_text.get_width() // 2, 200))
        display.blit(name_text, (SX // 2 - name_text.get_width() // 2, 300))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                input_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.strip() != "":
                    save_score(name, score)
                    gg = False  # Reinicia el juego
                    input_active = False
                    show_top_5()
                    reset_game()  # Restablece variables del juego
                    startengine_sfx.play()
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode


def bubble_sort_scores(scores: list[tuple[str, int]]) -> None: #Bubble Sort como algoritmo de ordenamiento para ubicar los scores mayor a menor
    n = len(scores)
    for i in range(n):
        for j in range(0, n-i-1):
            if scores[j][1] < scores[j+1][1]:  
                scores[j], scores[j+1] = scores[j+1], scores[j]


def show_top_5() -> None:
    """
    Muestra los 5 jugadores con las puntuaciones más altas en la
    pantalla. El jugador puede presionar 'Enter' para volver al juego.
    """
    scores = read_scores()
    bubble_sort_scores(scores)
    top_5 = scores[:5]  # Top 5 scores mas altos

    showing_top_5 = True
    while showing_top_5:
        display.fill((BLACK))  
        display.blit(bg_big , (0, 0))
        title = font_menu.render("TOP 5 JUGADORES", True, (WHITE))
        display.blit(title, (SX // 2 - title.get_width() // 2, 50))

        for i, (name, score) in enumerate(top_5):
            score_text = font_menu.render(f"{i + 1}. {name}: {score}", True, (WHITE))
            display.blit(score_text, (SX // 2 - score_text.get_width() // 2, 150 + i * 50))

        exit_text = font_menu.render("Oprime ENTER para volver a jugar", True, (WHITE))
        display.blit(exit_text, (SX // 2 - exit_text.get_width() // 2, SY - 100))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                showing_top_5 = False
                global run
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    showing_top_5 = False

def reset_game() -> None:
    """
    Restablece las variables del juego a su estado inicial.
    """
    global lives, score, asteroids, player_bullet, stars
    lives = 3
    score = 0
    asteroids.clear()
    player_bullet.clear()
    stars.clear()

def start_game() -> None:
    """
    Bucle principal del juego que maneja toda la lógica del juego. 
    El juego continúa hasta que el jugador pierde todas las vidas, momento en el cual se muestra la pantalla de juego terminado.

    La función también verifica eventos como la pulsación de teclas y el cierre de la ventana.

    Controles:
    - 'A': Gira al jugador hacia la izquierda.
    - 'D': Gira al jugador hacia la derecha.
    - 'W': Mueve al jugador hacia adelante.
    - 'S': Mueve al jugador hacia atrás.
    - 'ESPACIO': Dispara una bala o dispara con el impulso de fuego si está activo.
    - 'M': Activa o desactiva el sonido.
    """
    global run, count, player_bullet, asteroids, lives, gg, score, stars, fire_boost, f_boost
    soundtrack_sfx.play(loops=-1)  # Repetir la música de fondo
    startengine_sfx.play()  # Reproducir el efecto de sonido de arranque del Motor

    while run:
        clock.tick(60)  # Limita la tasa de cuadros a 60 FPS
        count += 1  # Incrementar el contador del juego

        if not gg:  # El juego está en marcha
            if count % ASTEROID_CHANCE == 0:  # Cada 50 fotogramas
                ran = random.choice([1, 1, 1, 2, 2, 3])  # Clasificación aleatoria de asteroides
                asteroids.append(Asteroid(ran))  # Agregar un nuevo asteroide

            if count % STAR_CHANCE == 0:  # Cada 1000 fotogramas
                stars.append(Star())  # Agregar una nueva estrella

            if count % LIFESTAR_CHANCE == 0:  # Cada 2500 fotogramas
                stars.append(LifeStar())  # Añadir una estrella de vida

            for i in player_bullet:  # Movimiento de las Balas
                i.move()

            for a in asteroids:  # Movimiento de los Asteroides
                a.move()

                # Colisión entre el jugador y el asteroide
                if player.rect.colliderect(a.rect):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    hit_sfx.play()  # Reproducir sonido de impacto
                    break

                # Colisión entre una bala y un asteroide
                for b in player_bullet:
                    if b.rect.colliderect(a.rect):
                        if a.rank == 3:  # Asteroide grande
                            score += 10
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidL_sfx.play()  # Sonido de gran asteroide destruido
                        elif a.rank == 2:  # Asteroide mediano
                            score += 20
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x, na1.y = a.x, a.y
                            na2.x, na2.y = a.x, a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                            asteroidM_sfx.play()  # Sonido de asteroide mediano destruido
                        else:  # Pequeño asteroide
                            score += 50
                        asteroids.pop(asteroids.index(a))
                        player_bullet.pop(player_bullet.index(b))
                        asteroidS_sfx.play()  # Sonido de pequeño asteroide destruido
                        break

            for s in stars[:]:  # Itera sobre una copia de la lista para evitar problemas de modificación (copia superficial)
                s.move()

                # Eliminar estrellas fuera del área visible
                if s.x < -100 - s.w or s.x > SX + 100 or s.y > SY + 100 or s.y < -100 - s.h:
                    stars.remove(s)
                    continue

                # Colisión entre estrellas y balas
                for b in player_bullet[:]:
                    if s.rect.colliderect(b.rect):
                        if s.effect == 'boost':
                            fire_boost = True
                            f_boost = count
                            pickup_sfx.play()  # Efecto de sonido de recogida
                        elif s.effect == 'lesslife':
                            lives -= 1
                            hit_sfx.play()  # Efecto de sonido de golpe
                        elif s.effect == 'morelife':
                            lives += 1
                            powerup_sfx.play()  # Efecto de sonido de potenciación

                        stars.remove(s)
                        player_bullet.remove(b)
                        break

                # Colisión entre la estrella y el jugador
                to_remove = []
                if player.rect.colliderect(s.rect):
                    if s.effect == 'boost':
                        fire_boost = True
                        f_boost = count
                        pickup_sfx.play()  # Efecto de sonido de recogida
                    elif s.effect == 'lesslife':
                        lives -= 1
                        hit_sfx.play()  # Efecto de sonido de golpe
                    elif s.effect == 'morelife':
                        lives += 1
                        powerup_sfx.play()  # Efecto de sonido de potenciación
                    to_remove.append(s)
                    for s in to_remove:
                        stars.remove(s)  # Quita la estrella después de recogerla

            # Verifica si el jugador ha perdido todas las vidas
            if lives <= 0:
                dead_sfx.play()  # Sonido de hacerse el muerto
                gg = True  # Game over

            # Gestionar la expiración del aumento de fuego
            if f_boost != -1:
                if count - f_boost > 500:
                    powerdown_sfx.play()  # Power-down Efecto de sonido
                    fire_boost = False
                    f_boost = -1

            # Movimiento y disparo del jugador
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.rotate_left()
            if keys[pygame.K_RIGHT]:
                player.rotate_right()
            if keys[pygame.K_UP]:
                player.move_forward()
            if keys[pygame.K_DOWN]:
                player.move_backwards()
            if keys[pygame.K_SPACE]:
                if fire_boost:
                    player_bullet.append(Bullet())  # Fuego con impulso
                    rapidshoot_sfx.play()  # Sonido de disparos rápidos


        else:  # If game over
            show_game_over_screen()

        # Manejar eventos (por ejemplo, pulsaciones de teclas, cierre de ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Cerrar Juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gg: 
                        if not fire_boost:
                            player_bullet.append(Bullet())  # Bala de fuego
                            shoot_sfx.play()  # Efecto de sonido de disparo
                    else:
                        gg = False  # Reiniciar Juego
                        reset_game()  # Restablecer el estado del juego
                if event.key == pygame.K_m:
                    isSoundOn = not isSoundOn  # Activar/desactivar sonido

        redraw_game_window()  # Volver a dibujar la ventana del juego

    pygame.quit()  # Cierra el juego y termina el loop


