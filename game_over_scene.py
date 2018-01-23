# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene sisplays the game over scene.

from scene import *
import ui
import config
import sound

class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        config.score = config.score
        config.game_over = False
        
        # this shows the game scene background
        self.background = SpriteNode('./assets/sprites/game_scene_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the title
        title_label_position = Vector2()
        title_label_position.x = self.centre_of_screen_x
        title_label_position.y = self.centre_of_screen_y + 300
        self.title_label = LabelNode(text = 'GAME OVER',
                                     font = ('Party LET', 100),
                                     parent = self,
                                     color = 'black',
                                     position = title_label_position)
        
        # this shows the score label
        score_label_position = Vector2()
        score_label_position.x = self.centre_of_screen_x
        score_label_position.y = self.centre_of_screen_y + 100
        self.score_label = LabelNode(text = 'Score: ' + str(config.score),
                                     font = ('Party LET', 100),
                                     parent = self,
                                     color = 'black',
                                     position = score_label_position)
        
        # this shows the retry button                                                                 
        main_menu_button_position = Vector2()
        main_menu_button_position.x = self.centre_of_screen_x
        main_menu_button_position.y = self.centre_of_screen_y
        self.main_menu_button = SpriteNode('./assets/sprites/main_menu_button.PNG',
                                       parent = self, 
                                       position = main_menu_button_position,
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
        
        # dismisses game over scene when the retry button is touched
        if self.main_menu_button.frame.contains_point(touch.location):
            if config.mute == False:
                sound.play_effect('8ve:8ve-beep-organ')
            config.game_over = True
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
    
