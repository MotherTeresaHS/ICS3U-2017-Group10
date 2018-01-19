# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the instructions scene.

from scene import *
import ui
import config
from game_scene import *


class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        
        # this shows continue button                                                                 
        continue_button_position = Vector2()
        continue_button_position.x = self.centre_of_screen_x + 400
        continue_button_position.y = self.centre_of_screen_y 
        self.continue_button = SpriteNode('./assets/sprites/continue_button.PNG',
                                       parent = self, 
                                       position = continue_button_position,
                                       scale = 2)  
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # transitions to game scene when start button is touched
        if self.continue_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-beep-organ')
           self.present_modal_scene(GameScene())
        
    
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
    
