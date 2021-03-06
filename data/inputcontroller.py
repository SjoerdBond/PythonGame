import pygame as pg
from . import constants as c
from . import main as m
from . import GUI as GUI

def playerInput(control):
    for event in pg.event.get():

        if  (event.type == pg.QUIT):
            control.done = True
            
        elif event.type == pg.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                control.GUI.leftMouseClick()
            elif event.button == 2:
                control.GUI.middleMouseClick()
            elif event.button == 3:
                control.GUI.rightMouseClick()
            elif event.button == 4:
                control.GUI.hotbarSelected += 1
                if control.GUI.hotbarSelected > 9:
                    control.GUI.hotbarSelected = 1
            elif event.button == 5:
                control.GUI.hotbarSelected -= 1
                if control.GUI.hotbarSelected < 1:
                    control.GUI.hotbarSelected = 9
                    
        elif event.type == pg.MOUSEMOTION:    
            control.GUI.updateMousePos(pg.mouse.get_pos())         
                    
        #do other stuff
        # mousePos = pg.mouse.get_pos()
    
        #     mouseColliders = [s for s in m.icon_sprites if s.rect.collidepoint(mousePos)]
        #     if mouseColliders:
        #         if gameControl.player.colliders:
        #             if mouseColliders[0].inventory == gameControl.player.inventory:
        #                 gameControl.player.colliders[0].inventory.add_item(mouseColliders[0].item)
        #                 gameControl.player.inventory.remove_item(mouseColliders[0].item)
        #             
        #             elif mouseColliders[0].inventory == gameControl.player.colliders[0].inventory:
        #                 gameControl.player.colliders[0].inventory.remove_item(mouseColliders[0].item)
        #                 gameControl.player.inventory.add_item(mouseColliders[0].item)
        #                 
        #             
        #         elif mouseColliders[0].inventory == gameControl.player.equipped:
        #             gameControl.player.equipped[mouseColliders[0].item.type] = []
        #             gameControl.player.inventory.add_item(mouseColliders[0].item) 
        #               
        #         else:
        #             gameControl.player.equipped[mouseColliders[0].item.type] = mouseColliders[0].item
        #             gameControl.player.inventory.remove_item(mouseColliders[0].item)
                
                
                        
                        
                        
            
        elif event.type == pg.KEYDOWN:
            if not control.GUI.mainMenuOpen:
                if(event.key == pg.K_RIGHT) or (event.key == pg.K_LEFT) or (event.key == pg.K_DOWN) or (event.key == pg.K_UP):
                    control.world.player.add_direction(event.key)
                
            if control.GUI.mainMenuOpen:
                if(event.key == pg.K_DOWN):
                    control.GUI.menu_selecting(1)
                
                if(event.key == pg.K_UP):
                    control.GUI.menu_selecting(-1)
            
            #Select hotbar 1
            if(event.key == pg.K_1):
                control.GUI.hotbarSelected=1
            #Select hotbar 2
            if(event.key == pg.K_2):
                control.GUI.hotbarSelected=2
            #Select hotbar 3
            if(event.key == pg.K_3):
                control.GUI.hotbarSelected=3
            #Select hotbar 4
            if(event.key == pg.K_4):
                control.GUI.hotbarSelected=4
            #Select hotbar 5
            if(event.key == pg.K_5):
                control.GUI.hotbarSelected=5
            #Select hotbar 6
            if(event.key == pg.K_6):
                control.GUI.hotbarSelected=6
            #Select hotbar 7
            if(event.key == pg.K_7):
                control.GUI.hotbarSelected=7
            #Select hotbar 8
            if(event.key == pg.K_8):
                control.GUI.hotbarSelected=8
            #Select hotbar 9
            if(event.key == pg.K_9):
                control.GUI.hotbarSelected=9
            #Select hotbar -
            if(event.key == pg.K_KP_MINUS):
                control.GUI.inventory_selecting(-1)
            #Select hotbar =
            if(event.key == pg.K_KP_PLUS):
                control.GUI.inventory_selecting(1)
            #Select hotbar =
            if(event.key == pg.K_KP_MULTIPLY):
                if len(control.world.player.inventory.items) and control.GUI.inventoryOpen :
                   control.world.player.inventory.remove_item(control.world.player.inventory.items[control.GUI.inventorySelection])
                
            #Cast Fireball 
            if(event.key == pg.K_KP1):
                control.world.player.castFireball()
            
            #Create NPC
            if(event.key == pg.K_KP2):
                mousePos = pg.mouse.get_pos()
                worldPos = mousePos[0]+control.viewport[0],mousePos[1]+control.viewport[1]
                control.world.create_NPC(worldPos)
            
            #Create Stone Resource
            if(event.key == pg.K_KP3):
                mousePos= pg.mouse.get_pos()
                worldPos = [mousePos[0]+control.viewport.x, mousePos[1]+control.viewport.y]
                
                mouseColliders = [s for s in control.world.tilemap if s.rect.collidepoint(worldPos)]
                currentTile = mouseColliders[0]
                control.world.generate_resource('Stone', currentTile)
                
                
            #Create Chest
            if(event.key == pg.K_KP4):
                mousePos= pg.mouse.get_pos()
                worldPos = [mousePos[0]+control.viewport.x, mousePos[1]+control.viewport.y]
                
                mouseColliders = [s for s in control.world.tilemap if s.rect.collidepoint(worldPos)]
                currentTile = mouseColliders[0]
                control.world.create_chest(currentTile)
                
            #Create Tree Resource
            if(event.key == pg.K_KP5):
                mousePos= pg.mouse.get_pos()
                worldPos = [mousePos[0]+control.viewport.x, mousePos[1]+control.viewport.y]
                
                mouseColliders = [s for s in control.world.tilemap if s.rect.collidepoint(worldPos)]
                currentTile = mouseColliders[0]
                control.world.generate_resource('Tree', currentTile)
                
            #Change Tile
            # if(event.key == pg.K_5):
            #     mousePos= pg.mouse.get_pos()
            #     worldPos = [mousePos[0]+control.viewport.x, mousePos[1]+control.viewport.y]
            #     
            #     mouseColliders = [s for s in control.world.tilemap if s.rect.collidepoint(worldPos)]
            #     currentTile = mouseColliders[0]
            #     control.world.change_tileType(currentTile, 'Dirt')
                
            #Interact
            if(event.key == pg.K_e):
                control.world.player.startAction()  
                
            #Inventory Screen
            if(event.key == pg.K_i):
                control.GUI.toggleInventory()
                
            #Character Screen        
            if(event.key == pg.K_c):
                control.GUI.toggleCharacterScreen()
                
            #Crafting Screen        
            if(event.key == pg.K_p):
                control.GUI.toggleCraftingScreen() 
                

                
            #Main Menu        
            if(event.key == pg.K_ESCAPE):
                if len(control.GUI.menu_stack):
                    control.GUI.menu_stack.pop(-1)
                else:
                    control.GUI.toggleMainMenu()
    
                    
        elif event.type == pg.KEYUP:
            if(event.key == pg.K_RIGHT) or (event.key == pg.K_LEFT) or (event.key == pg.K_DOWN) or (event.key == pg.K_UP):
                control.world.player.pop_direction(event.key)
                    
            if(event.key == pg.K_e):
                control.world.player.stopAction()

        