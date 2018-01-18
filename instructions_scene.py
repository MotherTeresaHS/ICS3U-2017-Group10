# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the instructions scene.

from scene import *
import ui
import time 

class InstructionsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.start_time = time.time()
        self.centre_of_screen = self.size/2
        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        self.pause_button_down = False
        
        # add background color
        self.background = SpriteNode('./assets/sprites/instructions_scene_picture.JPG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)

        left_button_position = self.centre_of_screen
        left_button_position.x = self.centre_of_screen.x / 5.8
        left_button_position.y = self.centre_of_screen.y / 4
        self.left_button = SpriteNode('./assets/sprites/left_button.png',
                                       parent = self,
                                       position = left_button_position,
                                       alpha = 2)
                                     
        right_button_position = self.centre_of_screen
        right_button_position.x = self.centre_of_screen.x * 2.6
        right_button_position.y = self.centre_of_screen.y 
        self.right_button = SpriteNode('./assets/sprites/right_button.png',
                                       parent = self,
                                       position = right_button_position,
                                       alpha = 2)

        fire_button_position = Vector2()
        fire_button_position.x = self.centre_of_screen.x * 4.1
        fire_button_position.y = self.centre_of_screen.y 
        self.fire_button = SpriteNode('./assets/sprites/red_button.png',
                                       parent = self,
                                       position = fire_button_position,
                                       alpha = 2)

        pause_button_position = Vector2()
        pause_button_position.x = self.centre_of_screen.x * 4
        pause_button_position.y = self.centre_of_screen.y * 7.5
        self.pause_button = SpriteNode('./assets/sprites/help.png',
                                       parent = self,
                                       position = pause_button_position,
                                       scale = 0.5,
                                       alpha = 2)
        #screen.setBrightness_(0.1)
        self.explain_label = LabelNode(text = '',
                                      font=('Party LET', 40),
                                      parent = self,
                                      color = 'black',
                                      position = self.size/2)

    def update(self):
        # this method is called, hopefully, 60 times a second
        if self.left_button_down == True:
            self.left_button.alpha = (0.5)
            self.left_button.scale = 0.9
            self.explain_label.text = 'Moves your character to the left'

        if self.right_button_down == True:
            self.right_button.alpha = (0.5)
            self.right_button.scale = 0.9
            self.explain_label.text = 'Moves your character to the right'

        if self.fire_button_down == True:
            self.fire_button.alpha = (0.5)
            self.fire_button.scale = 0.9
            self.explain_label.text = 'Fires a note'

        if self.pause_button_down == True:
            self.pause_button.alpha = (0.5)
            self.pause_button.scale = 0.4
            self.explain_label.text = 'Pauses the game'
        pass

    def touch_began(self, touch):
        # this method is called, when user touches the screen

        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True

        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True

        if self.fire_button.frame.contains_point(touch.location):
            self.fire_button_down = True

        if self.pause_button.frame.contains_point(touch.location):
            self.pause_button_down = True
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        self.pause_button_down = False
        self.left_button.alpha = 2
        self.left_button.scale = 1
        self.right_button.alpha = 2
        self.right_button.scale = 1
        self.fire_button.alpha = 2
        self.fire_button.scale = 1
        self.pause_button.alpha = 2
        self.pause_button.scale = 0.5
        
        self.explain_label.text = ''
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
    
