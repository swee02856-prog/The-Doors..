import pygame
import SoundsAndMusic
pygame.init()

PiperoomDialogue1 = "You go through the door & hit yourself on a pipe"
PiperoomDialogue2 = "You look and see an infinite array of pipes,"
PiperoomDialogue3 = "To escape you must follow the pipes.."
PiperoomDialogue4 = "There will be NO food or supplies, an Entity is there"
PiperoomDialogue5 = "Survival Chance: 10%"

PiperoomVoice1 = pygame.mixer.Sound("PiperoomsVoice1.mp3")
PiperoomVoice2 = pygame.mixer.Sound("PiperoomsVoice2.mp3")
PiperoomVoice3 = pygame.mixer.Sound("PiperoomsVoice3.mp3")
PiperoomVoice4 = pygame.mixer.Sound("PiperoomsVoice4.mp3")
PiperoomVoice5 = pygame.mixer.Sound("PiperoomsVoice5.mp3")

Voiceline = 0
Dialogue = 0

def piperoomVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return PiperoomVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        PiperoomVoice1.stop()
        return PiperoomVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        PiperoomVoice2.stop()
        return PiperoomVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        PiperoomVoice3.stop()
        return PiperoomVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        PiperoomVoice4.stop()
        return PiperoomVoice5.play()
    if Voiceline == 5:
        PiperoomVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()

def piperooms():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return PiperoomDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return PiperoomDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return PiperoomDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return PiperoomDialogue4
    elif Dialogue == 4:
        return PiperoomDialogue5