import pygame
import SoundsAndMusic
pygame.init()

BackroomsDialogue1 = "You stumble across a very interesting.. type of floor,"
BackroomsDialogue2 = "There are lots and lots, of hallways..."
BackroomsDialogue3 = "You look around and see something tall, looking at you..."
BackroomsDialogue4 = "To escape you must follow the arrows.."
BackroomsDialogue5 = "Survival Chance: 12%"

BackroomVoice1 = pygame.mixer.Sound("BackroomVoice1.mp3")
BackroomVoice2 = pygame.mixer.Sound("BackroomVoice2.mp3")
BackroomVoice3 = pygame.mixer.Sound("BackroomVoice3.mp3")
BackroomVoice4 = pygame.mixer.Sound("BackroomVoice4.mp3")
BackroomVoice5 = pygame.mixer.Sound("BackroomVoice5.mp3")

Voiceline = 0
Dialogue = 0

def backroomVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return BackroomVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        BackroomVoice1.stop()
        return BackroomVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        BackroomVoice2.stop()
        return BackroomVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        BackroomVoice3.stop()
        return BackroomVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        BackroomVoice4.stop()
        return BackroomVoice5.play()    
    if Voiceline == 5:
        BackroomVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()


def backrooms():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return BackroomsDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return BackroomsDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return BackroomsDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return BackroomsDialogue4
    elif Dialogue == 4:
        return BackroomsDialogue5