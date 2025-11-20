import pygame
import sys
from scripts.game import *
from scripts.sfx import *



# Crea la ventana del Juego
window = pygame.display.set_mode((SX, SY))
pygame.display.set_caption("Ethereum")


# Inicializa Pygame y Pygame Mixer
pygame.init()
pygame.mixer.init()

def main_menu() -> None:
    """
    Muestra el menú principal y gestiona la interacción del usuario para navegar a través de las opciones.
    """
    global selected_option

    bandera_menu = True
    while bandera_menu:
        # Rellena la ventana con el color de fondo
        window.fill(BLACK)
        display.blit(bg_bigmenu , (0, 0))

        # Renderiza y muestra el título
        title_text = font_title.render("Ethereum", True, WHITE) 
        window.blit(
            title_text, (SY // 2 - title_text.get_width() // 2, SX // 4)
        )               #posicion horizontal                   #posicion vertical

        # Renderiza y muestra cada opción del menú
        for i, option in enumerate(menu_options):
            if i == selected_option:
                color = WHITE 
            else: color = GRAY  
            option_text = font_menu.render(option, True, color)
            window.blit(
                option_text,
                (SY // 2 - option_text.get_width() // 2, SX // 2 + i * 60),
            )

        # Recibe la tecla que presione el usuario 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                    select_sfx.play()  # Emite el audio de seleccion
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()  # Emite el audio de confirmacion
                    if selected_option == 0:  # Inicia el juego
                        bandera_menu = False # Cierra el menu
                        start_game(player)
                    if selected_option == 2: # Muestra el menu de opciones
                        settings_menu()
                    elif selected_option == 1:  # Muestra la pantalla de creditos
                        show_credits()
                    elif selected_option == 3:  # Muestra la pantalla de controles
                        show_controls()
                    elif selected_option == 4:  # Cierra el programa
                        pygame.quit()
                        sys.exit()
                        return

        pygame.display.update()  # Actualiza la imagen al terminar el loop SIEMPRE

def show_controls() -> None:
    """
   Muestra la pantalla de controles y gestiona la interacción del usuario para volver al menú principal.
    """
    bandera_controles = True
    while bandera_controles:
        # Llena el fondo negro
        window.fill(BLACK)

        # Define el texto de la pantalla de controles
        controls_text = [
            "Controles",
            "Movimiento: \u2191 \u2193 \u2190 \u2192",
            "Disparar: \u2423",
            " ",
            "Presiona ESC para volver",
        ]

        # Renderiza y muuestra cada linea del texto de controles
        for i, line in enumerate(controls_text):
            text = font_control.render(line, True, WHITE) # Selecciona la fuente 
            window.blit(
                text, (SY // 2 - text.get_width() // 2, SX // 3 + i * 60) # Posicionamiento del texto
            )

        # Maneja la tecla que presione el usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # Percibe o recibe cuando el usuario presiona una tecla
                if event.key == pygame.K_ESCAPE: # Si la tecla es ESC 
                    returnselect_sfx.play()  
                    bandera_controles = False # Cierra el loop y con ello la ventana de controles

        pygame.display.update()  # Actualiza la imagen al terminar el loop SIEMPRE
    return

def show_credits() -> None:
    global naveselected_option

    nave_options = ["Leviathan", "Astra Nova", "Starlance"]

    bandera_credits = True

    while bandera_credits:
        window.fill(BLACK)
        window.blit(bg_seleccionave, (-380, -200))

        # Dibujar sprites de naves
        window.blit(player_sprite, (SY // 2.2, SX // 2))
        window.blit(player2_sprite, (SY // 5, SX // 2))
        window.blit(player3_sprite, (SY - 200, SX // 2))

        # Título
        title = font_menualternative.render("Selecciona tu Nave", True, WHITE)
        window.blit(title, (SY // 2 - title.get_width() // 2, SX // 6))

        # Opciones debajo de las naves
        for i, nombre in enumerate(nave_options):
            color = WHITE if i == naveselected_option else GRAY
            text = font_menualternative.render(nombre, True, color)

            # Posiciones según la nave correspondiente
            if i == 0:
                xpos = SY // 2.2
            elif i == 1:
                xpos = SY // 5
            else:
                xpos = SY - 200

            ypos = SX // 2 + 150
            window.blit(text, (xpos, ypos))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    naveselected_option = (naveselected_option - 1) % len(nave_options)
                    select_sfx.play()

                if event.key == pygame.K_LEFT:
                    naveselected_option = (naveselected_option + 1) % len(nave_options)
                    select_sfx.play()

                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()

                    if naveselected_option == 0:
                        player_param = Player1()
                        start_game(player_param)
                    elif naveselected_option == 1:
                        player_param = Player2()
                        start_game(player_param)
                    elif naveselected_option == 2:
                        player_param = Player3()
                        start_game(player_param)
                    return

                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()
                    bandera_credits = False

        pygame.display.update()
    return
        
def settings_menu() -> None:  
    settings_options = ["Tamaño de la ventana", "Opciones de volumen", "Presiona ESC para volver"]  
    selected_settings_option = 0  
    bandera_settings = True  
    
    while bandera_settings:  
        window.fill(BLACK)  

        for i, option in enumerate(settings_options):  
            if i == selected_settings_option:
                color = WHITE 
            else: color = GRAY  
            option_text = font_menu.render(option, True, color)  
            window.blit(option_text, (SY // 2 - option_text.get_width() // 2, SX // 3 + i * 60))  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()  
                sys.exit()  
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_UP:  
                    selected_settings_option = (selected_settings_option - 1) % len(settings_options)  
                    select_sfx.play()  
                if event.key == pygame.K_DOWN:  
                    selected_settings_option = (selected_settings_option + 1) % len(settings_options)  
                    select_sfx.play()  
                if event.key == pygame.K_RETURN:  
                    clickselect_sfx.play()  
                    if selected_settings_option == 0:  
                        screen_size_settings()  
                    elif selected_settings_option == 1:  
                        volume_settings()  
                    elif selected_settings_option == 2:  
                        returnselect_sfx.play()  
                        bandera_settings = False  
                if event.key == pygame.K_ESCAPE:  
                    returnselect_sfx.play()  
                    bandera_settings = False  

        pygame.display.update()
    return  

def volume_settings() -> None:
    global SFX_VOLUME_LEVELS, MUSIC_VOLUME_LEVELS, select_sfx, clickselect_sfx, returnselect_sfx, soundtrack_sfx
    
    volume_options = [
        "Aumentar volumen de efectos",
        "Disminuir volumen de efectos",
        "Aumentar volumen de musica",
        "Disminuir volumen de musica",
        "Presiona ESC para volver"
    ]
    selected_volume_option = 0
    bandera_volumen = True

    while bandera_volumen:
        window.fill(BLACK)

        for i, option in enumerate(volume_options):
            color = WHITE if i == selected_volume_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(option_text, (SX // 2 - option_text.get_width() // 2, SY // 3 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_volume_option = (selected_volume_option - 1) % len(volume_options)
                    select_sfx.play()
                if event.key == pygame.K_DOWN:
                    selected_volume_option = (selected_volume_option + 1) % len(volume_options)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()
                    if selected_volume_option == 0:  # Aumenta el volumen de efectos
                        SFX_VOLUME_LEVELS = min(10, SFX_VOLUME_LEVELS + 1)
                        update_sfx_volume()
                    elif selected_volume_option == 1:  # Disminuye el volumen de efectos
                        SFX_VOLUME_LEVELS = max(0, SFX_VOLUME_LEVELS - 1)
                        update_sfx_volume()
                    elif selected_volume_option == 2:  # Aumenta el volumen de la musica
                        MUSIC_VOLUME_LEVELS = min(10, MUSIC_VOLUME_LEVELS + 1)
                        update_music_volume()
                    elif selected_volume_option == 3:  # Disminuye el volumen de la musica
                        MUSIC_VOLUME_LEVELS = max(0, MUSIC_VOLUME_LEVELS - 1)
                        update_music_volume()
                    elif selected_volume_option == 4:  # Vuelve a la ventana de ajustes
                        returnselect_sfx.play()
                        bandera_volumen = False
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()
                    bandera_volumen = False

        pygame.display.update()

    settings_menu()  # Abre el menu de ajustes para volver

def update_sfx_volume()  -> None:
    global SFX_VOLUME_LEVELS
    select_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    clickselect_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    returnselect_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    shoot_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    rapidshoot_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidL_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidM_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    asteroidS_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    hit_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    pickup_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    powerup_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    powerdown_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)
    dead_sfx.set_volume(SFX_VOLUME_LEVELS * 0.1)

def update_music_volume() -> None:
    global MUSIC_VOLUME_LEVELS
    soundtrack_sfx.set_volume(MUSIC_VOLUME_LEVELS * 0.1)

def screen_size_settings() -> None:
    global SX, SY, window

    screen_size_options = ["1. 720x720", "2. 900x900", "3. 1000x1000", "Presiona ESC para volver"]
    selected_screen_size_option = 0
    screen_size_running = True

    while screen_size_running:
        window.fill(BLACK)

        for i, option in enumerate(screen_size_options):
            color = WHITE if i == selected_screen_size_option else GRAY
            option_text = font_menu.render(option, True, color)
            window.blit(option_text, (SX // 2 - option_text.get_width() // 2, SY // 3 + i * 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_screen_size_option = (selected_screen_size_option - 1) % len(screen_size_options)
                    select_sfx.play()
                if event.key == pygame.K_DOWN:
                    selected_screen_size_option = (selected_screen_size_option + 1) % len(screen_size_options)
                    select_sfx.play()
                if event.key == pygame.K_RETURN:
                    clickselect_sfx.play()
                    if selected_screen_size_option == 0:
                        SX, SY = 720, 720
                    elif selected_screen_size_option == 1:
                        SX, SY = 900, 900
                    elif selected_screen_size_option == 2:
                        SX, SY = 1000, 1000
                    elif selected_screen_size_option == 3:
                        returnselect_sfx.play()
                        screen_size_running = False
                    window = pygame.display.set_mode((SX, SY))
                if event.key == pygame.K_ESCAPE:
                    returnselect_sfx.play()
                    screen_size_running = False

        pygame.display.update()

    settings_menu()  # Abre el menu de ajustes para volver


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    main_menu()
