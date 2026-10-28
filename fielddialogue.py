import pygame
import SoundsAndMusic
pygame.init()

FieldDialogue1 = "You walk through the door and fall onto grass"
FieldDialogue2 = "A sign says 'Be weary of the night'.."
FieldDialogue3 = "To escape you must cross 5 miles"
FieldDialogue4 = "Enities are at night, there is no supplies."
FieldDialogue5 = "Survival Chance: 22%"

FieldVoice1 = pygame.mixer.Sound("FieldVoice1.mp3")
FieldVoice2 = pygame.mixer.Sound("FieldVoice2.mp3")
FieldVoice3 = pygame.mixer.Sound("FieldVoice3.mp3")
FieldVoice4 = pygame.mixer.Sound("FieldVoice4.mp3")
FieldVoice5 = pygame.mixer.Sound("FieldVoice5.mp3")

Voiceline = 0
Dialogue = 0

def fieldVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return FieldVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        FieldVoice1.stop()
        return FieldVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        FieldVoice2.stop()
        return FieldVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        FieldVoice3.stop()
        return FieldVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        FieldVoice4.stop()
        return FieldVoice5.play()
    if Voiceline == 5:
        FieldVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()

def field():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return FieldDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return FieldDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return FieldDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return FieldDialogue4
    elif Dialogue == 4:
        return FieldDialogue5