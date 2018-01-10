# Created by: David, James
# Created on: Sep 2016
# Created for: ICS3U
# This scene displays the main menu.

from scene import *
import ui

from instructions_scene import *
from credits_scene import *
from settings_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.score_position = Vector2()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
        # add background color
        self.background = SpriteNode('./assets/sprites/main_menu_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        
         # sound
        #if SettingsScene.MusicOn == True:
           #SettingsScene.MainMenuMusic.play()
        #elif SettingsScene.MusicOn == False:
           #SettingsScene.MainMenuMusic.pause()
        

    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
    def rotate(self, orientation):
        allowed_orientations = ['LANDSCAPE']
        if orientation.upper() in allowed_orientations:
            self.execute(Command.SET_SCREEN_ORIENTATION, {'orientation': orientation})
        else:
            raise WebDriverException("You can only set the orientation to 'LANDSCAPE' or 'PORTRAIT'.")


