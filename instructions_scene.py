# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the instructions scene.

from scene import *
import ui
import config

from main_menu_scene import *
import time

class InstructionsScene(Scene):
    def setup(self):

        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.centre_of_screen_x = self.size_of_screen_x/2
        self.centre_of_screen_y = self.size_of_screen_y/2 
        self.scale_size = 0.4
        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        self.pause_button_down = False
        self.speed_of_violin = 15.0
        self.notes = []
        
        # this shows the game scene background
        self.background = SpriteNode('./assets/sprites/game_scene_background.PNG',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        
        # this shows the title
        title_label_position = Vector2()
        title_label_position.x = self.centre_of_screen_x
        title_label_position.y = self.centre_of_screen_y + 300
        self.title_label = LabelNode(text = 'Instructions Scene',
                                     font = ('Party LET', 100),
                                     parent = self,
                                     color = 'black',
                                     position = title_label_position)
        
        # this shows the title
        underline_label_position = Vector2()
        underline_label_position.x = self.centre_of_screen_x
        underline_label_position.y = self.centre_of_screen_y + 305
        self.underline_label = LabelNode(text = '__________',
                                     font = ('Party LET', 100),
                                     parent = self,
                                     color = 'black',
                                     position = underline_label_position)
        
        # this shows the score label
        score_label_position = Vector2()
        score_label_position.x = self.centre_of_screen_x - 410
        score_label_position.y = self.centre_of_screen_y + 325
        self.score_label = LabelNode(text = 'Score: 0',
                                     font = ('Party LET', 60),
                                     parent = self,
                                     color = 'black',
                                     position = score_label_position)
        
        # this shows the exit label
        exit_label_position = Vector2()
        exit_label_position.x = self.centre_of_screen_x + 450
        exit_label_position.y = self.centre_of_screen_y + 75
        self.exit_label = LabelNode(text = 'Exit',
                                     font = ('Party LET', 60),
                                     parent = self,
                                     color = 'black',
                                     position = exit_label_position)
        
        
        # this shows the explanations of buttons when buttons are held down 
        self.explanation_label = LabelNode(text = 'Touch a Button for Instructions',
                                           font = ('Party LET', 55),
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
        
        # this shows the right button
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
        
        # this shows the home button
        home_button_position = Vector2()
        home_button_position.x = self.centre_of_screen_x + 450
        home_button_position.y = self.centre_of_screen_y
        self.home_button = SpriteNode('./assets/sprites/home_button.PNG',
                                      parent = self, 
                                      position = home_button_position,
                                      scale = 1.8)
        
        # this shows the violin                                                                
        violin_position = Vector2()
        violin_position.x = self.centre_of_screen_x - 425
        violin_position.y = self.centre_of_screen_y - 175
        self.violin = SpriteNode('./assets/sprites/violin.PNG',
                                       parent = self, 
                                       position = violin_position,
                                       scale = 0.20) 
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # shows the explanation of each button when buttons are held down
        if self.left_button_down == True:
            self.left_button.alpha = 0.5
            self.left_button.scale = 1
            self.explanation_label.text = 'Moves your character to the left'
        
        if self.right_button_down == True:
            self.right_button.alpha = 0.5
            self.right_button.scale = 1.5
            self.explanation_label.text = 'Moves your character to the right'
        
        if self.fire_button_down == True:
            self.fire_button.alpha = 0.5
            self.fire_button.scale = 1.5
            self.explanation_label.text = 'Fires a note'
        
        if self.pause_button_down == True:
            self.pause_button.alpha = 0.5
            self.pause_button.scale = 1.5
            self.explanation_label.text = 'Pauses the game'
        
        # moves guen towards the left if left button is held down
        if self.left_button_down == True and self.violin.position.x > 100:
            self.violin.run_action(Action.move_by(-1*self.speed_of_violin, 0.0, 0.1))
        
        # moves guen towards the right if right button is held down
        if self.right_button_down == True and self.violin.position.x < self.size_of_screen_x - 100:
            self.violin.run_action(Action.move_by(self.speed_of_violin, 0.0, 0.1))
       
       # removes note
        for note in self.notes:
            if note.position.x > self.size_of_screen_x:
                note.remove_from_parent()
                self.notes.remove(note)
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # sets button to true when button is touched and held down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        
        if self.fire_button.frame.contains_point(touch.location):
            self.fire_button_down = True
        
        if self.pause_button.frame.contains_point(touch.location):
            self.pause_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        
        # sets button down to false when button is released

        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        self.pause_button_down = False
        
        # sets buttons' scale to original
        self.left_button.scale = 2
        self.right_button.scale = 2
        self.fire_button.scale = 2
        self.pause_button.scale = 2
        
        # sets buttons' alpha to original
        self.left_button.alpha = 2
        self.right_button.alpha = 2
        self.fire_button.alpha = 2
        self.pause_button.alpha = 2
        
        # sets explanation back to original text
        self.explanation_label.text = 'Touch a Button for Instructions'
        
        # fires a note when fire button is touched
        if self.fire_button.frame.contains_point(touch.location):
            self.create_new_note()
        
        # dismisses settings scene if home button is touched
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
    
    def create_new_note(self):
        
        # creates new note and adds it to an array when called
        note_start_position = self.violin.position
        note_end_position = Vector2(self.size_of_screen_x, self.violin.position.y)
        self.notes.append(SpriteNode('./assets/sprites/note.PNG',
                                     parent = self,
                                     position = note_start_position,
                                     scale = 0.25))
        
        note_move_action = Action.move_to(note_end_position.x + 500,
                                          note_end_position.y,
                                          8.0)
        self.notes[len(self.notes) - 1].run_action(note_move_action)
        
        if config.mute == False:
            sound.play_effect('8ve:8ve-beep-organ')
    
