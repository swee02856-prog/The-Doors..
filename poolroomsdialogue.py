import pygame
import SoundsAndMusic
pygame.init()
PoolroomDialogue1 = "You walk into an area of.. pools? Lots of them.."
PoolroomDialogue2 = "You feel as if something big is approaching.."
PoolroomDialogue3 = "You find randomly placed food everywhere"
PoolroomDialogue4 = "To escape you must find 5 valves within this level.."
PoolroomDialogue5 = "Survival chance: 66%"

PoolroomVoice1 = pygame.mixer.Sound("PoolroomVoice1.mp3")
PoolroomVoice2 = pygame.mixer.Sound("PoolroomVoice2.mp3")
PoolroomVoice3 = pygame.mixer.Sound("PoolroomVoice3.mp3")
PoolroomVoice4 = pygame.mixer.Sound("PoolroomVoice4.mp3")
PoolroomVoice5 = pygame.mixer.Sound("PoolroomVoice5.mp3")

Voiceline = 0
Dialogue = 0

def poolroomVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return PoolroomVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        PoolroomVoice1.stop()
        return PoolroomVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        PoolroomVoice2.stop()
        return PoolroomVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        PoolroomVoice3.stop()
        return PoolroomVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        PoolroomVoice4.stop()
        return PoolroomVoice5.play()
    if Voiceline == 5:
        PoolroomVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()
def poolrooms():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return PoolroomDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return PoolroomDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return PoolroomDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return PoolroomDialogue4
    elif Dialogue == 4:
        return PoolroomDialogue5
