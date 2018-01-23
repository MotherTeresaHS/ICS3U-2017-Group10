# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the main menu.

from scene import *
import ui
import sound
import config

from game_scene import *
from settings_scene import *
from instructions_scene import *
from credits_scene import *

class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        
        # this shows the default background
        self.background = SpriteNode('./assets/sprites/default_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the title
        title_label_position = Vector2()
        title_label_position.x = self.centre_of_screen_x + 220
        title_label_position.y = self.centre_of_screen_y + 200
        self.title_label = LabelNode(text = 'Violin Attack',
                                     font = ('Party LET', 125),
                                     parent = self,
                                     position = title_label_position)
        
        # this shows the start button
        start_button_position = Vector2()
        start_button_position.x = self.centre_of_screen_x + 220
        start_button_position.y = self.centre_of_screen_y + 50
        self.start_button = SpriteNode('./assets/sprites/play_button.PNG',
                                       parent = self,
                                       position = start_button_position,
                                       scale = 1.60)
        
        # this shows the settings button
        settings_button_position = Vector2()
        settings_button_position.x = self.centre_of_screen_x + 220
        settings_button_position.y = self.centre_of_screen_y - 50
        self.settings_button = SpriteNode('./assets/sprites/settings_button.PNG',
                                          parent = self,
                                          position = settings_button_position,
                                          scale = 1.5)
        
        # this shows the instructions button
        instructions_button_position = Vector2()
        instructions_button_position.x = self.centre_of_screen_x + 220
        instructions_button_position.y = self.centre_of_screen_y - 150
        self.instructions_button = SpriteNode('./assets/sprites/instructions_button.PNG',
                                              parent = self,
                                              position = instructions_button_position,
                                              scale = 1.85)
        
        # this shows the credits button
        credits_button_position = Vector2()
        credits_button_position.x = self.centre_of_screen_x + 220
        credits_button_position.y = self.centre_of_screen_y - 250
        self.credits_button = SpriteNode('./assets/sprites/credits_button.PNG',
                                         parent = self,
                                         position = credits_button_position,
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
        
        # transitions to instructions scene when start button is touched
        if self.start_button.frame.contains_point(touch.location):
           if config.mute == False:
               sound.play_effect('8ve:8ve-beep-organ')
           config.score = 0
           config.game_over = False
           self.present_modal_scene(GameScene())
        
        # transitions to settings scene when the settings button is touched
        if self.settings_button.frame.contains_point(touch.location):
           if config.mute == False:
               sound.play_effect('8ve:8ve-beep-organ')
           self.present_modal_scene(SettingsScene())
        
         # tranitions to credits scene when the credits button is touched
        if self.instructions_button.frame.contains_point(touch.location):
            if config.mute == False:
                sound.play_effect('8ve:8ve-beep-organ')
            self.present_modal_scene(InstructionsScene())
        
        # tranitions to credits scene when the credits button is touched
        if self.credits_button.frame.contains_point(touch.location):
            if config.mute == False:
                sound.play_effect('8ve:8ve-beep-organ')
            self.present_modal_scene(CreditsScene())
    
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
    
