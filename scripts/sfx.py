import pygame
from .settings import *

pygame.mixer.init()
#Sonidos Laser
shoot_sfx = pygame.mixer.Sound("assets/sounds/laserShoot.wav")
shoot_sfx.set_volume(SFX_VOLUME_LEVELS)
rapidshoot_sfx = pygame.mixer.Sound("assets/sounds/rapidshoot.wav")
rapidshoot_sfx.set_volume(SFX_VOLUME_LEVELS)

#Sonidos Explosion
asteroidL_sfx = pygame.mixer.Sound("assets/sounds/explosion.wav")
asteroidL_sfx.set_volume(SFX_VOLUME_LEVELS)
asteroidM_sfx = pygame.mixer.Sound("assets/sounds/explosion_m.wav")
asteroidM_sfx.set_volume(SFX_VOLUME_LEVELS)
asteroidS_sfx = pygame.mixer.Sound("assets/sounds/explosion_s.wav")
asteroidS_sfx.set_volume(SFX_VOLUME_LEVELS)

# Volumen
hit_sfx = pygame.mixer.Sound("assets/sounds/hit.wav")
hit_sfx.set_volume(SFX_VOLUME_LEVELS)

pickup_sfx = pygame.mixer.Sound("assets/sounds/pickup.wav")
pickup_sfx.set_volume(SFX_VOLUME_LEVELS)

# Sonido POWER-UPs
powerup_sfx = pygame.mixer.Sound("assets/sounds/powerup.wav")
powerup_sfx.set_volume(SFX_VOLUME_LEVELS)
powerdown_sfx = pygame.mixer.Sound("assets/sounds/powerdown.wav")
powerdown_sfx.set_volume(SFX_VOLUME_LEVELS)

# Sonido Seleccion Menu
select_sfx = pygame.mixer.Sound("assets/sounds/select.wav")
select_sfx.set_volume(SFX_VOLUME_LEVELS)

# Sonido Muerte
dead_sfx = pygame.mixer.Sound("assets/sounds/dead.wav")
dead_sfx.set_volume(SFX_VOLUME_LEVELS)

soundtrack_sfx = pygame.mixer.Sound("assets/sounds/game_soundtrack.mp3")
soundtrack_sfx.set_volume(MUSIC_VOLUME_LEVELS)


clickselect_sfx = pygame.mixer.Sound("assets/sounds/blipSelect.wav")
clickselect_sfx.set_volume(SFX_VOLUME_LEVELS)

returnselect_sfx = pygame.mixer.Sound("assets/sounds/backSelect.wav")
returnselect_sfx.set_volume(SFX_VOLUME_LEVELS)

startengine_sfx = pygame.mixer.Sound("assets/sounds/startengine.wav")
startengine_sfx.set_volume(SFX_VOLUME_LEVELS)