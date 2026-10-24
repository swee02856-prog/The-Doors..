import pygame
import random
import SoundsAndMusic
import Rooms
import RoomSys
import apartmentdialogue
import fielddialogue
import windowroomsdialogue
import Piperoomsdialogue
import neighborhooddialogue
import backroomsdialogue
import poolroomsdialogue
import os
import sys
def resource_path(path):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, path)

pygame.init()

window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
RedDoor = pygame.image.load("RedDoor.png").convert_alpha()
RedDoor = pygame.transform.scale(RedDoor, (300, 300))

RedDoorHover = pygame.image.load("RedDoorOpened.png").convert_alpha()
RedDoorHover = pygame.transform.scale(RedDoorHover, (300, 300))

BlueDoor = pygame.image.load("BlueDoor.png").convert_alpha()
BlueDoor = pygame.transform.scale(BlueDoor, (300, 300))

BlueDoorHover = pygame.image.load("BlueDoorOpened.png").convert_alpha()
BlueDoorHover = pygame.transform.scale(BlueDoorHover, (300, 300))
RedDoorRect = pygame.Rect(75, 100, 300, 300)
BlueDoorRect = pygame.Rect(400, 100, 300, 300)

TextboxBackground = pygame.image.load("Textbox.png").convert_alpha()
TextboxBackground = pygame.transform.scale(TextboxBackground, (500, 550))

Jumpscare = pygame.image.load("Jumpscare.png").convert_alpha()
Jumpscare = pygame.transform.scale(Jumpscare, (800, 600))

JumpscareSound = pygame.mixer.Sound("Jumpscare.mp3")

def JumpscareEffect():
    window.blit(Jumpscare, ((0, 0)))
    pygame.display.flip()
    JumpscareSound.play()
    pygame.time.delay(5000)

jumpscarechance = range(1, 8)
smallerjumpscarechance = range(1, 20)
ChooseRoomSound = pygame.mixer.Sound("choosingroom.mp3")

GameFont = pygame.font.Font("Fonts/PixelOperator.ttf", 21)

ChooseDoorText = GameFont.render("Choose a door..", True, (255, 255, 255))

ClicktoContinueText = GameFont.render("Click to Continue..", True, (255, 255, 255))

MusicPlaying = False
IsRedDoorHovering = False
IsBlueDoorHovering = False

while True:
    for event in pygame.event.get():
        MousePosition = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            quit(0)

        if RoomSys.CurrentArea == ["ChoosingRoom"]:
            if not MusicPlaying:
                ChooseRoomSound.play()
                MusicPlaying = True
            if RedDoorRect.collidepoint(MousePosition):
                if not IsRedDoorHovering:
                    window.blit(RedDoorHover, (75, 100))
                    IsRedDoorHovering = True
            else:
                IsRedDoorHovering = False
                window.blit(RedDoor, (75, 100))

            if BlueDoorRect.collidepoint(MousePosition):
                if not IsBlueDoorHovering:
                    window.blit(BlueDoorHover, (400, 100))
                    IsBlueDoorHovering = True

            else:
                IsBlueDoorHovering = False
                window.blit(BlueDoor, (400, 100))

            window.blit(ChooseDoorText, (280, 500))

            if event.type == pygame.MOUSEBUTTONDOWN:
                MousePosition = pygame.mouse.get_pos()
                if RedDoorRect.collidepoint(MousePosition):
                    if random.choice(jumpscarechance) == 1:
                        JumpscareEffect()
                    RoomSys.CurrentArea.remove("ChoosingRoom")
                    RoomSys.CurrentArea.append(RoomSys.RandomArea)
                    MusicPlaying = False
                    ChooseRoomSound.stop()
                if BlueDoorRect.collidepoint(MousePosition):
                    if random.choice(jumpscarechance) == 1:
                        JumpscareEffect()
                    RoomSys.CurrentArea.remove("ChoosingRoom")
                    RoomSys.CurrentArea.append(RoomSys.RandomArea)
                    MusicPlaying = False
                    ChooseRoomSound.stop()

        if RoomSys.CurrentArea == ["poolrooms"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = poolroomsdialogue.poolrooms()
                poolroomsdialogue.poolroomVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.poolrooms, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))
            
        if RoomSys.CurrentArea == ["backrooms"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = backroomsdialogue.backrooms()
                backroomsdialogue.backroomVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.backrooms, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

        if RoomSys.CurrentArea == ["neighborhood"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = neighborhooddialogue.neighborhood()
                neighborhooddialogue.neighborhoodVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.Neighborhood, (-200, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

        if RoomSys.CurrentArea == ["piperooms"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = Piperoomsdialogue.piperooms()
                Piperoomsdialogue.piperoomVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.piperooms, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

        if RoomSys.CurrentArea == ["WindowFloors"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = windowroomsdialogue.windowrooms()
                windowroomsdialogue.windowroomVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.Windowfloors, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

        if RoomSys.CurrentArea == ["Field"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = fielddialogue.field()
                fielddialogue.fieldVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.fieldfloor, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

        if RoomSys.CurrentArea == ["Apartments"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if random.choice(smallerjumpscarechance) == 1:
                    JumpscareEffect()
                SoundsAndMusic.Nextsound.play()
                CurrentText = apartmentdialogue.apartments()
                apartmentdialogue.apartmentVoicelines()
            Narratortext = GameFont.render(CurrentText, True, (255, 255, 255))
            window.blit(Rooms.Apartments, (0, 0))
            window.blit(TextboxBackground, (140, 275))
            window.blit(Narratortext, (170, 470))

    pygame.display.flip()