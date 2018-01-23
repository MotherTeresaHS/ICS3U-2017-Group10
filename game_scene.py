# Created by: David, James
# Created on: Dec 2017
# Created for: ICS3U
# This scene displays the game.

from scene import *
import ui
import config
import time

from numpy import random
from game_over_scene import *
from game_won_scene import *


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
        self.fire_button_down = False
        self.fire_button_enabled = True
        self.note_fired_time = time.time()
        self.speed_of_violin = 15.0
        self.notes = []
        self.violists = []
        self.violists_attack_rate = 1
        self.violists_attack_speed = 20.0
        self.game_over = False
        config.score = 0
        
        # this shows the game scene background
        self.background = SpriteNode('./assets/sprites/game_scene_background.PNG',
                                     position = self.size / 2, 
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
        self.right_button = SpriteNode('./assets/sprites/right_button.PNG',
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
        
        # this shows the guen                                                                
        violin_position = Vector2()
        violin_position.x = self.centre_of_screen_x - 425
        violin_position.y = self.centre_of_screen_y - 175
        self.violin = SpriteNode('./assets/sprites/violin.PNG',
                                       parent = self, 
                                       position = violin_position,
                                       scale = 0.20) 
        
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        if config.game_over == True:
            self.dismiss_modal_scene()
        
        if config.score == 25:
            self.present_modal_scene(GameWonScene())
        
        # sets scale and alpha lowe for each button when buttons are held down
        if self.left_button_down == True:
            self.left_button.alpha = 0.5
            self.left_button.scale = 1
        
        if self.right_button_down == True:
            self.right_button.alpha = 0.5
            self.right_button.scale = 1.5
        
        if self.fire_button_down == True:
            self.fire_button.alpha = 0.5
            self.fire_button.scale = 1.5
        
        # moves guen towards the left if left button is held down
        if self.left_button_down == True and self.violin.position.x > 100:
            self.violin.run_action(Action.move_by(-1*self.speed_of_violin, 0.0, 0.1))
        
        # moves guen towards the right if right button is held down
        if self.right_button_down == True and self.violin.position.x < self.size_of_screen_x - 100:
            self.violin.run_action(Action.move_by(self.speed_of_violin, 0.0, 0.1))
        
        # creates violist at random intervals
        violist_create_chance = (random.randint(1,150) - config.score / 10)
        if violist_create_chance <= self.violists_attack_rate and self.game_over == False:
            self.create_violist()
        
        # removes note
        for note in self.notes:
            if note.position.x > self.size_of_screen_x:
                note.remove_from_parent()
                self.notes.remove(note)
        
        # removes note if it collides with violist and increases score by one
        if len(self.notes) > 0 and len(self.violists) > 0:
            for note in self.notes:
                for violist in self.violists:
                    if violist.frame.contains_rect(note.frame):
                        note.remove_from_parent()
                        self.notes.remove(note)
                        violist.remove_from_parent()
                        self.violists.remove(violist)
                        config.score = config.score + 1
        
        # adds score to config score
        if not self.score_label.text == 'Score: ' + str(config.score) and self.game_over == False:
            self.score_label.text = 'Score: ' + str(config.score)
        
        # removes guen and violist when they collide
        for violist_shred in self.violists:
            if violist_shred.frame.intersects(self.violin.frame):
                self.violin.position = Vector2(-300, -500)
                self.violin.remove_from_parent()
                violist_shred.remove_from_parent()
                self.violists.remove(violist_shred)
                self.present_modal_scene(GameOverScene())
                time.sleep(0.1)
        
        # sets fire button to true if one second has passed
        if (time.time() - self.note_fired_time) > 1:
            self.fire_button_enabled = True
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        # sets button to true when button is touched and held down
        if self.left_button.frame.contains_point(touch.location):
            self.left_button_down = True
        
        if self.right_button.frame.contains_point(touch.location):
            self.right_button_down = True
        
        if self.fire_button.frame.contains_point(touch.location):
            self.fire_button_down = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # sets button down to false when button is released
        self.left_button_down = False
        self.right_button_down = False
        self.fire_button_down = False
        
        # sets buttons' scale to original
        self.left_button.scale = 2
        self.right_button.scale = 2
        self.fire_button.scale = 2
        
        # sets buttons' alpha to original
        self.left_button.alpha = 2
        self.right_button.alpha = 2
        self.fire_button.alpha = 2
        
        # fires a note when fire button is touched
        if self.fire_button.frame.contains_point(touch.location) and self.fire_button_enabled and self.game_over == False:
            self.note_fired_time = time.time()
            self.fire_button_enabled = False
            self.create_new_note()
    
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
    
    def create_violist(self):
        
        # creates new violist and adds it to an array when called
        violist_start_position = Vector2(self.size_of_screen_x, self.violin.position.y)
        violist_end_position = Vector2(self.size_of_screen_x, self.violin.position.y)
        self.violists.append(SpriteNode('./assets/sprites/violist.PNG',
                                        parent = self,
                                        position = violist_start_position,
                                        scale = 0.20))
        
        violist_move_action = Action.move_to(violist_end_position.x - random.randint(1000, 2000),
                                             violist_end_position.y,
                                             88)
        self.violists[len(self.violists) - 1].run_action(violist_move_action)
    
