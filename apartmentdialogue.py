import pygame
import SoundsAndMusic
pygame.init()


ApartmentDialogue1 = "You walk and see Apartments..?"
ApartmentDialogue2 = "You look around and see an infinite hallway.."
ApartmentDialogue3 = "To escape you must survive for 15 days.."
ApartmentDialogue4 = "An entity will spawn at night and wander the halls.."
ApartmentDialogue5 = "Survival Chance: 68%"

ApartmentVoice1 = pygame.mixer.Sound("ApartmentVoice1.mp3")
ApartmentVoice2 = pygame.mixer.Sound("ApartmentVoice2.mp3")
ApartmentVoice3 = pygame.mixer.Sound("ApartmentVoice3.mp3")
ApartmentVoice4 = pygame.mixer.Sound("ApartmentVoice4.mp3")
ApartmentVoice5 = pygame.mixer.Sound("ApartmentVoice5.mp3")

Voiceline = 0
Dialogue = 0

def apartmentVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return ApartmentVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        ApartmentVoice1.stop()
        return ApartmentVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        ApartmentVoice2.stop()
        return ApartmentVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        ApartmentVoice3.stop()
        return ApartmentVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        ApartmentVoice4.stop()
        return ApartmentVoice5.play()
    if Voiceline == 5:
        ApartmentVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()

def apartments():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return ApartmentDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return ApartmentDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return ApartmentDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return ApartmentDialogue4
    elif Dialogue == 4:
        return ApartmentDialogue5