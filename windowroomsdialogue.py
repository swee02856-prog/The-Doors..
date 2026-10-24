import SoundsAndMusic
import pygame
pygame.init()

WindowroomsDialogue1 = "You walk through the door and almost fall of the edge"
WindowroomsDialogue2 = "You see lots of abandoned office buildings..."
WindowroomsDialogue3 = "You know something is lurking.."
WindowroomsDialogue4 = "Food and water is in rooms. Do not try to escape." 
WindowroomsDialogue5 = "Survival Chance: 23%"

WindowroomVoice1 = pygame.mixer.Sound("WindowroomVoice1.mp3")
WindowroomVoice2 = pygame.mixer.Sound("WindowroomVoice2.mp3")
WindowroomVoice3 = pygame.mixer.Sound("WindowroomVoice3.mp3")
WindowroomVoice4 = pygame.mixer.Sound("WindowroomVoice4.mp3")
WindowroomVoice5 = pygame.mixer.Sound("WindowroomVoice5.mp3")

Voiceline = 0
Dialogue = 0

def windowroomVoicelines():
    global Voiceline
    if Voiceline == 0:
        Voiceline += 1
        return WindowroomVoice1.play()
    if Voiceline == 1:
        Voiceline += 1
        WindowroomVoice1.stop()
        return WindowroomVoice2.play()
    if Voiceline == 2:
        Voiceline += 1
        WindowroomVoice2.stop()
        return WindowroomVoice3.play()
    if Voiceline == 3:
        Voiceline += 1
        WindowroomVoice3.stop()
        return WindowroomVoice4.play()
    if Voiceline == 4:
        Voiceline += 1
        WindowroomVoice4.stop()
        return WindowroomVoice5.play()
    if Voiceline == 5:
        WindowroomVoice5.stop()
        SoundsAndMusic.RandomPickedSong.stop()
        return SoundsAndMusic.RandomPickedSong.play()
def windowrooms():
    global Dialogue
    if Dialogue == 0:
        Dialogue += 1
        return WindowroomsDialogue1
    elif Dialogue == 1:
        Dialogue += 1
        return WindowroomsDialogue2
    elif Dialogue == 2:
        Dialogue += 1
        return WindowroomsDialogue3
    elif Dialogue == 3:
        Dialogue += 1
        return WindowroomsDialogue4
    elif Dialogue == 4:
        Dialogue += 1
        return WindowroomsDialogue5