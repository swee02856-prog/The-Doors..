import pygame
import random
pygame.init()
RandomSong1 = pygame.mixer.Sound("backrooms1.mp3")
RandomSong2 = pygame.mixer.Sound("backrooms2.mp3")
RandomSong3 = pygame.mixer.Sound("backrooms3.mp3")
RandomSong4 = pygame.mixer.Sound("backrooms4.mp3")

Nextsound = pygame.mixer.Sound("next.mp3")

RoomSongs = [RandomSong1, RandomSong2, RandomSong3, RandomSong4]
RandomPickedSong = random.choice(RoomSongs)
