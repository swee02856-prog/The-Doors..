import SoundsAndMusic
import pygame
pygame.init()


NeighborhoodDialogue1 = "You end up in an empty neighborhood after walking through."
NeighborhoodDialogue2 = "Entities will always appear at night trying to enter."
NeighborhoodDialogue3 = "To escape you must find a floating house, it is miles away.."
NeighborhoodDialogue4 = "Eating too much or greedly eating is a death wish.."
NeighborhoodDialogue5 = "Survival Chance: 70%"

NeighborhoodVoice1 = pygame.mixer.Sound("NeighborhoodVoice1.mp3")
NeighborhoodVoice2 = pygame.mixer.Sound("NeighborhoodVoice2.mp3")
NeighborhoodVoice3 = pygame.mixer.Sound("NeighborhoodVoice3.mp3")
NeighborhoodVoice4 = pygame.mixer.Sound("NeighborhoodVoice4.mp3")
NeighborhoodVoice5 = pygame.mixer.Sound("NeighborhoodVoice5.mp3")

Voiceline = 0
Dialogue = 0

def neighborhoodVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return NeighborhoodVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        NeighborhoodVoice1.stop()
        return NeighborhoodVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        NeighborhoodVoice2.stop()
        return NeighborhoodVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        NeighborhoodVoice3.stop()
        return NeighborhoodVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        NeighborhoodVoice4.stop()
        return NeighborhoodVoice5.play()
    if Voiceline == 5:
        Voiceline += 1
        NeighborhoodVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()
def neighborhood():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return NeighborhoodDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return NeighborhoodDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return NeighborhoodDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return NeighborhoodDialogue4
    elif Dialogue == 4:
        Dialogue += 1
        return NeighborhoodDialogue5
    elif Dialogue == 5:
        return JumpscareEffect()