# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the settings scene.

from scene import *
import ui
import config

from main_menu_scene import *

class SettingsScene(Scene):
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
        
        # this shows the title label
        settings_label_position = Vector2()
        settings_label_position.x = self.centre_of_screen_x + 220
        settings_label_position.y = self.centre_of_screen_y + 300
        self.settings_label = LabelNode(text = 'Settings',
                                        font = ('Party LET', 125),
                                        parent = self,
                                        position = settings_label_position)
        
        # this shows the sound label
        sound_label_position = Vector2()
        sound_label_position.x = self.centre_of_screen_x + 220
        sound_label_position.y = self.centre_of_screen_y + 175
        self.sound_label = LabelNode(text = 'Sound',
                                     font = ('Party LET', 100),
                                     parent = self,
                                     position = sound_label_position)
        
        # this shows the unmute label
        unmute_label_position = Vector2()
        unmute_label_position.x = self.centre_of_screen_x + 165
        unmute_label_position.y = self.centre_of_screen_y
        self.unmute_label = LabelNode(text = 'Unmute',
                                      font = ('Party LET', 40),
                                      parent = self,
                                      position = unmute_label_position)
        
        # this shows the mute label
        mute_label_position = Vector2()
        mute_label_position.x = self.centre_of_screen_x + 275
        mute_label_position.y = self.centre_of_screen_y
        self.mute_label = LabelNode(text = 'Mute',
                                    font = ('Party LET', 40),
                                    parent = self,
                                    position = mute_label_position)
        
        # this shows the sound FX label
        sound_fx_label_position = Vector2()
        sound_fx_label_position.x = self.centre_of_screen_x + 215
        sound_fx_label_position.y = self.centre_of_screen_y - 100
        self.sound_fx_label = LabelNode(text = 'Sound FX',
                                        font = ('Party LET', 100),
                                        parent = self,
                                        position = sound_fx_label_position)
        
        # this shows the sound FX on label
        fx_on_label_position = Vector2()
        fx_on_label_position.x = self.centre_of_screen_x + 165
        fx_on_label_position.y = self.centre_of_screen_y - 275
        self.fx_on_label = LabelNode(text = 'On',
                                     font = ('Party LET', 40),
                                     parent = self,
                                     position = fx_on_label_position)
        
        # this shows the sound FX off label
        fx_off_label_position = Vector2()
        fx_off_label_position.x = self.centre_of_screen_x + 275
        fx_off_label_position.y = self.centre_of_screen_y - 275
        self.fx_off_label = LabelNode(text = 'Off',
                                      font = ('Party LET', 40),
                                      parent = self,
                                      position = fx_off_label_position)
        
        # mutes or unmutes sound when buttons are clicked in settings scene
        #if config.mute == False:
           #config.main_menu_music.number_of_loops = -1
           #config.main_menu_music.play()
        #elif config.mute == True:
           #config.main_menu_music.pause()
        
        # this shows the home button
        home_button_position = Vector2()
        home_button_position.x = self.centre_of_screen_x + 475
        home_button_position.y = self.centre_of_screen_y + 350
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 1.5)
        
        # this shows the unmute button                                                                 
        unmute_button_position = Vector2()
        unmute_button_position.x = self.centre_of_screen_x + 165
        unmute_button_position.y = self.centre_of_screen_y + 75
        self.unmute_button = SpriteNode('./assets/sprites/unmute_button.PNG',
                                        parent = self, 
                                        position = unmute_button_position,
                                        scale = 1.5)        
        
        # this shows the mute button                                                                 
        mute_button_position = Vector2()
        mute_button_position.x = self.centre_of_screen_x + 275
        mute_button_position.y = self.centre_of_screen_y + 75    
        self.mute_button = SpriteNode('./assets/sprites/mute_button.PNG',
                                      parent = self, 
                                      position = mute_button_position,
                                      scale = 1.5)
        
        # this shows the sound fx on button                                                                 
        fx_on_button_position = Vector2()
        fx_on_button_position.x = self.centre_of_screen_x + 165
        fx_on_button_position.y = self.centre_of_screen_y - 200 
        self.fx_on_button = SpriteNode('./assets/sprites/fx_on_button.PNG',
                                       parent = self, 
                                       position = fx_on_button_position,
                                       scale = 1.5)        
        
        # this shows the sound fx off button                                                                 
        fx_off_button_position = Vector2()
        fx_off_button_position.x = self.centre_of_screen_x + 275
        fx_off_button_position.y = self.centre_of_screen_y - 200           
        self.fx_off_button = SpriteNode('./assets/sprites/fx_off_button.PNG',                                
                                        parent = self, 
                                        position = fx_off_button_position,
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
        
        # dismisses settings scene if home button is touched
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
    
