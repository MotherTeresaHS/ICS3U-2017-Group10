# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the game.

from scene import *
import ui
import config

from paused_scene import *
from game_over_scene import *


class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        self.left_button_down = False
        self.right_button_down = False
        self.guen_speed = 20.0
        self.notes = []
        self.violists = []
        self.violists_attack_rate = 1
        self.violists_attack_speed = 20.0
        self.game_over = False
        self.score = 0
        
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#b9aaff', 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the score label
        score_label_position = Vector2()
        score_label_position.x = self.centre_of_screen_x - 410
        score_label_position.y = self.centre_of_screen_y + 325
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Party LET', 60),
                                     parent = self,
                                     position = score_label_position)
        
        # this shows the move left button                                                                 
        left_button_position = Vector2()
        left_button_position.x = self.centre_of_screen_x - 450
        left_button_position.y = self.centre_of_screen_y - 325
        self.left_button = SpriteNode('./assets/sprites/left_button.PNG',
                                       parent = self, 
                                       position = left_button_position,
                                       scale = 2) 
        
        # this shows the move right button                                                                 
        right_button_position = Vector2()
        right_button_position.x = self.centre_of_screen_x - 340
        right_button_position.y = self.centre_of_screen_y - 325
        self.left_button = SpriteNode('./assets/sprites/right_button.PNG',
                                       parent = self, 
                                       position = right_button_position,
                                       scale = 2) 
        
        # this shows the fire button                                                                 
        fire_button_position = Vector2()
        fire_button_position.x = self.centre_of_screen_x + 450
        fire_button_position.y = self.centre_of_screen_y - 325
        self.fire_button = SpriteNode('./assets/sprites/fire_button.PNG',
                                       parent = self, 
                                       position = fire_button_position,
                                       scale = 2) 
        
        # this shows the pause button                                                                 
        pause_button_position = Vector2()
        pause_button_position.x = self.centre_of_screen_x + 450
        pause_button_position.y = self.centre_of_screen_y + 325
        self.pause_button = SpriteNode('./assets/sprites/pause_button.PNG',
                                       parent = self, 
                                       position = pause_button_position,
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
        
        # tranitions to paused scene when the credits button is touched
        if self.pause_button.frame.contains_point(touch.location):
            sound.play_effect('8ve:8ve-beep-organ')
            self.present_modal_scene(PausedScene())
    
    
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
    
