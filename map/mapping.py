import pygame, pyautogui, render

class map():
    def __init__(self, mapPath, mainCharacter, mapTileSize:tuple):
        self.map = render.loadTMX(mapPath)
        self.windowSize = pyautogui.size()[1]/1.5, pyautogui.size()[1]/1.5*.71
        self.tileSize = int(self.map.get_width()/mapTileSize[0]), int(self.map.get_height()/mapTileSize[1])
        self.mainCharacterSize = self.tileSize
        self.map = pygame.transform.scale
        self.mapPos = [0,0]
        self.mainCharacter = pygame.transform.scale(pygame.image.load(mainCharacter), self.mainCharacterSize)
        self.mainCharacterPos = [(self.windowSize[0]/2)-(self.mainCharacterSize[0]/2), (self.windowSize[1]/2)-(self.mainCharacterSize[1]/2)]
        self.mapMoving = True

    def drawMap(self, screen, mapPath):
        screen.blit(render.loadTMX(mapPath), self.mapPos)

    def drawMainCharacter(self, screen):
        screen.blit(self.mainCharacter, self.mainCharacterPos)

    def move(self, x, y):
        if self.mapMoving:
            self.mapPos[0] -= x
            self.mapPos[1] -= y
    
    def teleport(self, x, y):
        pass

    def get_mainCharacterSize(self):
        return self.mainCharacterSize