# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the credits scene.

from scene import *
import ui
import time
import config

from main_menu_scene import *

class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.start_time = time.time()
        self.centre_of_screen = self.size/2
        self.design_credit_position = Vector2()
        self.design_credit_position.x = self.centre_of_screen.x * 1.4
        self.design_credit_position.y = self.centre_of_screen.y/6
        self.game_credit_position = Vector2()
        self.game_credit_position.x = self.centre_of_screen.x * 1.4
        self.game_credit_position.y = self.centre_of_screen.y/20 
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        
        # this shows the default background
        self.background = SpriteNode('./assets/sprites/default_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the design label
        self.design_credit = LabelNode(text = 'Design by: James Lee',
                                       font=('Party LET', 40),
                                       parent = self,
                                       position = self.design_credit_position)
        
        # adds credit label
        self.game_credit = LabelNode(text = 'Design by: David Wang',
                                     font=('Party LET', 40),
                                     parent = self,
                                     position = self.game_credit_position)
        
        # this shows the home button
        home_button_position = Vector2()
        home_button_position.x = self.centre_of_screen_x + 475
        home_button_position.y = self.centre_of_screen_y + 350
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 1.5)
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        update_position = Action.move_by(0, 15)
        if not self.presented_scene and time.time() - self.start_time > 1:
            self.design_credit.run_action(update_position)
            self.game_credit.run_action(update_position)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # dismisses credits scene if home button is touched
        if self.home_button.frame.contains_point(touch.location):
           if config.mute == False:
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
    
