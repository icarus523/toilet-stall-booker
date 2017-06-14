#!/bin/env python3

import tkinter as tk
import logging
import time

from tkinter import *
from tkinter import ttk
from datetime import datetime, timedelta

VERSION="1.0"
BUTTON_TEXT_SIZE = 36
STALL_TIMEOUT = 3600 # 1 Hour
TOILET_STALL_STRINGS = ['Toilet Stall 1', 'Toilet Stall 2', 'Toilet Stall 3']
URINAL_STALL_STRINGS = ['Urinal 1', 'Urinal 2', 'Urinal 3']

class ToiletBooker(tk.Frame):

    def generate_notable_times(self):
        generated_string = "*** Noteable Times *** "
        
        generated_string += "Toilet: " + str(self.achievements_stall['date']) + " Timer: " + self.convert_seconds_to_time(self.achievements_stall['value'])
        generated_string += " | Urinal: " + str(self.achievements_urinal['date']) + " Timer: " + self.convert_seconds_to_time(self.achievements_urinal['value'])
        
        return generated_string

    def setupGUI(self):

        w = self.root.winfo_screenwidth() # full screen mode. 
        h = self.root.winfo_screenheight()

        #w = 1024 # fixed for CRT display, testing only
        #h = 768
        
        self.root.wm_title("Toilet Room Booker v" + VERSION)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.resizable(1,1)
        self.clock = StringVar()
        
        # Header
        frame_header = tk.Frame(self.root)
        frame_header.pack(side = TOP, padx =3, pady=3, fill=X, expand = False)
        frame_header.config(relief = RIDGE, borderwidth = 3)

        tk.Label(frame_header, font=("Arial", 38, "bold"), justify=LEFT, text="LEVEL 3, Men's Toilet Stall Booker").pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_header, font=("Arial", 38, "bold"), justify=LEFT, textvariable=self.clock).pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_header, font=("Arial", 14, "bold"), justify=LEFT, text="For when discretion & stall preferences is a necessity.").pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='n')

        # Achievement Messages
        frame_achievement = tk.Frame(self.root)
        frame_achievement.pack(side = BOTTOM, padx =3, pady=3, fill=X, expand = False)
        frame_achievement.config(relief = RIDGE, borderwidth = 3)

        self.achievement_string = StringVar()
        self.achievement_string.set(self.generate_notable_times)
        tk.Label(frame_achievement, textvariable=self.achievement_string, font=("Arial", 18, "bold"), 
            justify=LEFT, text="Noteable Times:").pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='s')
                
        # Main
        frame_main = tk.Frame(self.root)
        frame_main.pack(side = BOTTOM, padx =3, pady=3, fill=BOTH, expand = True)
        frame_main.config(relief = RIDGE, borderwidth = 3)

        # Set up Stalls
        frame_stalls = tk.Frame(frame_main)
        frame_stalls.pack(side = LEFT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_stalls.config(relief = RIDGE, borderwidth = 3)


        self.stall_1_var = StringVar()
        self.stall_1_var.set(TOILET_STALL_STRINGS[0])
        self.button_stall_1 = tk.Button(frame_stalls, textvariable=self.stall_1_var, text=TOILET_STALL_STRINGS[0], bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_stall__', 1))                                             
        self.button_stall_1.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        self.stall_2_var = StringVar()
        self.stall_2_var.set(TOILET_STALL_STRINGS[1])
        self.button_stall_2 = tk.Button(frame_stalls, textvariable=self.stall_2_var, text = TOILET_STALL_STRINGS[1],  bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_stall__',2))                                             
        self.button_stall_2.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        self.stall_3_var = StringVar()
        self.stall_3_var.set(TOILET_STALL_STRINGS[2])
        self.button_stall_3 = tk.Button(frame_stalls, textvariable=self.stall_3_var, text = TOILET_STALL_STRINGS[2], bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_stall__',3))                                             
        self.button_stall_3.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        # Set up Urinals
        frame_Urinals = ttk.Frame(frame_main)
        frame_Urinals.pack(side = RIGHT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_Urinals.config(relief = RIDGE, borderwidth = 3)

        # Top Urinal Frame
        frame_Urinals_top = ttk.Frame(frame_Urinals)
        frame_Urinals_top.pack(side = LEFT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_Urinals_top.config(relief = RIDGE, borderwidth = 3)

        self.urinal_1_var = StringVar()
        self.urinal_1_var.set(URINAL_STALL_STRINGS[0])
        self.button_urinal_1 = tk.Button(frame_Urinals_top, textvariable=self.urinal_1_var, text = URINAL_STALL_STRINGS[0], bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__', 1))                                             
        self.button_urinal_1.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')
        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')
        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')


        # Right Urinals
        frame_Urinals_side = ttk.Frame(frame_Urinals)
        frame_Urinals_side.pack(side = RIGHT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_Urinals_side.config(relief = RIDGE, borderwidth = 3)

        tk.Label(frame_Urinals_side, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')
        tk.Label(frame_Urinals_side, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')

        self.urinal_3_var = StringVar()
        self.urinal_3_var.set(URINAL_STALL_STRINGS[2])
        self.button_urinal_3 = tk.Button(frame_Urinals_side, textvariable=self.urinal_3_var, text = URINAL_STALL_STRINGS[2], bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__',3))                                             
        self.button_urinal_3.pack(side = BOTTOM, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")        
        
        self.urinal_2_var = StringVar()
        self.urinal_2_var.set(URINAL_STALL_STRINGS[1])
        self.button_urinal_2 = tk.Button(frame_Urinals_side, textvariable=self.urinal_2_var, text = URINAL_STALL_STRINGS[1], bg="green", font=("Arial", BUTTON_TEXT_SIZE, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__',2))                                             
        self.button_urinal_2.pack(side = BOTTOM, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        tk.Label(frame_Urinals_side, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=BOTH, expand=True, anchor='n')

        self.update_clock() # initial time display

    def convert_seconds_to_time(self, input_seconds):
        sec = timedelta(seconds=int(input_seconds))
        d = datetime(1,1,1) + sec
        
        return("%2d min:%2d sec" % (d.minute, d.second))
        

    def update_clock(self):
        self.clock.set(time.strftime("%H:%M:%S"))
        self.achievement_string.set(self.generate_notable_times())

        if self.stall_1_var.get() != TOILET_STALL_STRINGS[0]:
            # Occupied, update timer. 
            self.timers['stall_1'] += 1
            if self.timers['stall_1'] == STALL_TIMEOUT: # hit timeout
                self.stall_1_var.set(TOILET_STALL_STRINGS[0])
                self.timers['stall_1'] = 0
            else:
                self.stall_1_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['stall_1']))

        if self.stall_2_var.get() != TOILET_STALL_STRINGS[1]:
            self.timers['stall_2'] += 1
            if self.timers['stall_2'] == STALL_TIMEOUT:
                self.stall_2_var.set(TOILET_STALL_STRINGS[1])
                self.timers['stall_2'] = 0
            else:
                self.stall_2_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['stall_2']))

        if self.stall_3_var.get() != TOILET_STALL_STRINGS[2]:
            # Occupied, update timer. 
            self.timers['stall_3'] += 1
            if self.timers['stall_3'] == STALL_TIMEOUT:
                self.stall_3_var.set(TOILET_STALL_STRINGS[2])
                self.timers['stall_3'] = 0
            else:
                self.stall_3_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['stall_3']))

        if self.urinal_1_var.get() != URINAL_STALL_STRINGS[0]:
            # Occupied, update timer. 
            self.timers['urinal_1'] += 1
            if self.timers['urinal_1'] == STALL_TIMEOUT:
                self.urinal_1_var.set(URINAL_STALL_STRINGS[0])
                self.timers['urinal_1'] = 0
            else:
                self.urinal_1_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['urinal_1']))

        if self.urinal_2_var.get() != URINAL_STALL_STRINGS[1]:
            # Occupied, update timer. 
            self.timers['urinal_2'] += 1
            if self.timers['urinal_2'] == STALL_TIMEOUT:
                self.urinal_2_var.set(URINAL_STALL_STRINGS[1])
                self.timers['urinal_2'] = 0
            else:
                self.urinal_2_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['urinal_2']))

        if self.urinal_3_var.get() != URINAL_STALL_STRINGS[2]:
            # Occupied, update timer. 
            self.timers['urinal_3'] += 1
            if self.timers['urinal_3'] == STALL_TIMEOUT:
                self.urinal_3_var.set(URINAL_STALL_STRINGS[2])
                self.timers['urinal_3'] = 0
            else:
                self.urinal_3_var.set("IN USE\n" + self.convert_seconds_to_time(self.timers['urinal_3']))

        self.root.after(1000, self.update_clock)

    def log_possible_achivement(self, type, stall_number, value): 
        current_date = datetime.now()
        
        if type == '__book_stall__':
            if value > int(self.achievements_stall['value']):
                self.achievements_stall['date'] = current_date.strftime("%Y-%m-%d")
                self.achievements_stall['value'] = value
                logging.debug("Wow! New Stall Record: " + self.achievements_stall['date'] + " Timer: " + str(self.achievements_stall['value']))
        elif type == '__book_urinal__':
            if value > int(self.achievements_urinal['value']):
                self.achievements_urinal['date'] = current_date.strftime("%Y-%m-%d")
                self.achievements_urinal['value'] = value            
                logging.debug("Wow! New Urinal Record: " + self.achievements_urinal['date'] + " Timer: " + str(self.achievements_urinal['value']))



    def handleButtonPress(self, command, stall_number):
        
        if command == '__book_stall__':
            if stall_number == 1: 
                if self.stall_1_var.get() == "Toilet Stall 1":
                    logging.debug("Booking Toilet Stall 1!")
                    self.button_stall_1.config(bg="red") 
                    self.stall_1_var.set("IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 1!")
                    self.button_stall_1.config(bg="green")
                    self.stall_1_var.set("Toilet Stall 1")
                    self.log_possible_achivement(command, stall_number, self.timers['stall_1'])

                    self.timers['stall_1'] = 0

            elif stall_number == 2: 
                if self.stall_2_var.get() == "Toilet Stall 2":
                    logging.debug("Booking Toilet Stall 2!")
                    self.button_stall_2.config(bg="red") 
                    self.stall_2_var.set("IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 2!")
                    self.button_stall_2.config(bg="green")
                    self.stall_2_var.set("Toilet Stall 2")
                    self.log_possible_achivement(command, stall_number, self.timers['stall_2'])
                    self.timers['stall_2'] = 0
                    
            elif stall_number == 3: 
                if self.stall_3_var.get() == "Toilet Stall 3":
                    logging.debug("Booking Toilet Stall 3!")
                    self.button_stall_3.config(bg="red") 
                    self.stall_3_var.set("IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 3!")
                    self.button_stall_3.config(bg="green")
                    self.stall_3_var.set("Toilet Stall 3")
                    self.log_possible_achivement(command, stall_number, self.timers['stall_3'])
                    self.timers['stall_3'] = 0



        elif command == '__book_urinal__':
            if stall_number == 1:
                if self.urinal_1_var.get() == "Urinal 1":
                    logging.debug("Booking Urinal 1!")
                    self.button_urinal_1.config(bg="red") 
                    self.urinal_1_var.set("IN USE")
                else:
                    logging.debug("Releasing Urinal 1!")
                    self.button_urinal_1.config(bg="green")
                    self.urinal_1_var.set("Urinal 1")
                    self.log_possible_achivement(command, stall_number, self.timers['urinal_1'])
                    self.timers['urinal_1'] = 0
                    
            elif stall_number == 2: 
                if self.urinal_2_var.get() == "Urinal 2":
                    logging.debug("Booking Urinal 2!")
                    self.button_urinal_2.config(bg="red") 
                    self.urinal_2_var.set("IN USE")
                else:
                    logging.debug("Releasing Urinal 2!")
                    self.button_urinal_2.config( bg="green")
                    self.urinal_2_var.set("Urinal 2")
                    self.log_possible_achivement(command, stall_number, self.timers['urinal_2'])
                    self.timers['urinal_2'] = 0
                    
            elif stall_number == 3: 
                if self.urinal_3_var.get() == "Urinal 3":
                    logging.debug("Booking Urinal 3!")
                    self.button_urinal_3.config(bg="red") 
                    self.urinal_3_var.set("IN USE")
                else:
                    logging.debug("Releasing Urinal 3!")
                    self.button_urinal_3.config( bg="green")
                    self.urinal_3_var.set("Urinal 3")
                    self.log_possible_achivement(command, stall_number, self.timers['urinal_3'])
                    self.timers['urinal_3'] = 0

    def __init__(self):
        today = datetime.now()
        
        logging.basicConfig(level= logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
        logging.debug('Start of toiletbooker.py')
        
        self.root = Tk()
        self.timers = { 'stall_1' : 0, 
                        'stall_2': 0,
                        'stall_3': 0,
                        'urinal_1' : 0,
                        'urinal_2' : 0,
                        'urinal_3' : 0 }

        self.achievements_stall = { 'date' : today.strftime("%Y-%m-%d"), 
                                    'value' : 0 }

        self.achievements_urinal = { 'date' : today.strftime("%Y-%m-%d"), 
                                    'value' : 0 }
                        
        self.setupGUI()
        self.root.mainloop()


def main():
        app = ToiletBooker()

if __name__ == "__main__": main()
