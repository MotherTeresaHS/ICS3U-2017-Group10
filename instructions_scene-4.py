# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the instructions scene.

from scene import *
import ui
import time
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
        self.start_time = time.time()
        self.centre_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        self.pause_button_down = False
        
        # this shows the background
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the score label
        score_label_position = Vector2()
        score_label_position.x = self.centre_of_screen_x - 410
        score_label_position.y = self.centre_of_screen_y + 325
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Party LET', 60),
                                     parent = self,
                                     color = 'black',
                                     position = score_label_position)
        
        # this shows the explanations of buttons when buttons are held down 
        self.explanation_label = LabelNode(text = '',
                                           font=('Party LET', 75),
                                           parent = self,
                                           color = 'black',
                                           position = self.size/2)
        
        # this shows the left button
        left_button_position = Vector2()
        left_button_position.x = self.centre_of_screen_x - 450
        left_button_position.y = self.centre_of_screen_y - 325
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                      parent = self,
                                      position = left_button_position,
                                      scale = 2,
                                      alpha = 2)
        
        # this sows the right button
        right_button_position = Vector2()
        right_button_position.x = self.centre_of_screen_x - 340
        right_button_position.y = self.centre_of_screen_y - 325
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
                                       parent = self,
                                       position = right_button_position,
                                       scale = 2,
                                       alpha = 2)
        
        # this shows the fire button
        fire_button_position = Vector2()
        fire_button_position.x = self.centre_of_screen_x + 450
        fire_button_position.y = self.centre_of_screen_y - 325
        self.fire_button = SpriteNode('./assets/sprites/fire_button.PNG',
                                      parent = self,
                                      position = fire_button_position,
                                      scale = 2,
                                      alpha = 2)
        
        # this shows the pause button
        pause_button_position = Vector2()
        pause_button_position.x = self.centre_of_screen_x + 450
        pause_button_position.y = self.centre_of_screen_y + 325
        self.pause_button = SpriteNode('./assets/sprites/pause_button.PNG',
                                       parent = self,
                                       position = pause_button_position,
                                       scale = 2,
                                       alpha = 2)
        
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
    
