# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the credits scene.

from scene import *
import ui
import time

from main_menu_scene import *

class CreditsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        self.start_time = time.time()

        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.center_of_screen = self.size/2
        self.design_credit_position = Vector2()
        self.design_credit_position.x = self.center_of_screen.x * 1.4
        self.design_credit_position.y = self.center_of_screen.y/6
        self.game_credit_position = Vector2()
        self.game_credit_position.x = self.center_of_screen.x * 1.4
        self.game_credit_position.y = self.center_of_screen.y/20 

        self.design_credit = LabelNode(text = 'Design by: James Lee',
                                      font=('Party LET', 40),
                                      parent = self,
                                      position = self.design_credit_position)
                                      

        self.game_credit = LabelNode(text = 'Design by: David Wang',
                                      font=('Party LET', 40),
                                      parent = self,
                                      position = self.game_credit_position)
                                      
    def update(self):
        # this method is called, hopefully, 60 times a second
        update_position = Action.move_by(0, 30)
        if not self.presented_scene and time.time() - self.start_time > 1:
             self.design_credit.run_action(update_position)
             self.game_credit.run_action(update_position)
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
