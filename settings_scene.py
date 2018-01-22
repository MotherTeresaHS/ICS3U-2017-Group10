# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the settings scene.

from scene import *
import ui
#import config
from main_menu_scene import *

class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
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
        
        # shows settings title label
        settings_label_position = Vector2()
        settings_label_position.x = self.centre_of_screen_x + 220
        settings_label_position.y = self.centre_of_screen_y + 300
        self.settings_label = LabelNode(text = 'Settings',
                                      font = ('Party LET', 125),
                                      parent = self,
                                      position = settings_label_position)
        
        # shows sound label
        sound_label_position = Vector2()
        sound_label_position.x = self.centre_of_screen_x + 220
        sound_label_position.y = self.centre_of_screen_y + 100
        self.sound_label = LabelNode(text = 'Sound',
                                      font = ('Party LET', 100),
                                      parent = self,
                                      position = sound_label_position)
        
        home_button_position = Vector2()
        home_button_position.x = self.centre_of_screen_x + 475
        home_button_position.y = self.centre_of_screen_y + 350
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                          parent = self, 
                                          position = home_button_position,
                                          scale = 1.5)
        
    
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
        
        # dismisses current scene if home button is touched
        if self.home_button.frame.contains_point(touch.location):
           sound.play_effect('8ve:8ve-beep-organ')
           self.dismiss_modal_scene()
    
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
    
