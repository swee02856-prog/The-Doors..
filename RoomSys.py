import pygame
import random
pygame.init()

CurrentArea = ["ChoosingRoom"]
Areas = ["poolrooms", "backrooms", "neighborhood", "piperooms", "WindowFloors", "Field", "Apartments"]
RandomArea = random.choice(Areas)