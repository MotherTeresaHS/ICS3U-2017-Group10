# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the instructions scene.

from scene import *
import ui
import time 
from objc_util import *

UIScreen = ObjCClass('UIScreen')
screen = UIScreen.mainScreen()

class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.start_time = time.time()
        self.centre_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        
        # add background color
        self.background = SpriteNode('./assets/sprites/instructions_scene_picture.JPG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)

        left_button_position = self.centre_of_screen
        left_button_position.x = 100
        left_button_position.y = 100
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 0.5)
                                     
        #screen.setBrightness_(0.1)
            
    def update(self):
        # this method is called, hopefully, 60 times a second
        if self.left_button_down == True:
            screen.setBrightness_(0.1)
        else:
            screen.setBrightness_(0.6)
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        #screen.setBrightness_(0.1)
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        screen.setBrightness_(0.6)
        self.left_button_down = False
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
    
