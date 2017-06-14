import tkinter as tk
import logging

from tkinter import *
from tkinter import ttk

VERSION="1.0"

class ToiletBooker:

    def setupGUI(self):

        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()

        self.root.wm_title("Toilet Room Booker v" + VERSION)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.resizable(1,1)

        # Header
        frame_header = tk.Frame(self.root)
        frame_header.pack(side = TOP, padx =3, pady=3, fill=X, expand = False)
        frame_header.config(relief = RIDGE, borderwidth = 3)

        tk.Label(frame_header, font=("Arial", 56, "bold"), justify=LEFT, text="LEVEL 3, Men's Toilet Stall Booker").pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_header, font=("Arial", 14, "bold"), justify=LEFT, text="For when discretion & preferences is a necessity.").pack(side=TOP, padx=3, pady=3, fill=X, expand=True, anchor='n')
                 
        # Main
        frame_main = tk.Frame(self.root)
        frame_main.pack(side = BOTTOM, padx =3, pady=3, fill=BOTH, expand = True)
        frame_main.config(relief = RIDGE, borderwidth = 3)

        # Set up Stalls
        frame_stalls = tk.Frame(frame_main)
        frame_stalls.pack(side = LEFT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_stalls.config(relief = RIDGE, borderwidth = 3)


        self.stall_1_var = StringVar()
        self.stall_1_var.set("Toilet Stall 1")
        self.button_stall_1 = tk.Button(frame_stalls, textvariable=self.stall_1_var, text="Toilet Stall 1", bg="green", font=("Arial", 48, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_stall__', 1))                                             
        self.button_stall_1.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        self.stall_2_var = StringVar()
        self.stall_2_var.set("Toilet Stall 2")
        self.button_stall_2 = tk.Button(frame_stalls, textvariable=self.stall_2_var, text = "Toilet Stall 2",  bg="green", font=("Arial", 48, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_stall__',2))                                             
        self.button_stall_2.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        self.stall_3_var = StringVar()
        self.stall_3_var.set("Toilet Stall 3")
        self.button_stall_3 = tk.Button(frame_stalls, textvariable=self.stall_3_var, text = "Toilet Stall 3", bg="green", font=("Arial", 48, "bold"),
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
        self.urinal_1_var.set("Urinal 1")
        self.button_urinal_1 = tk.Button(frame_Urinals_top, textvariable=self.urinal_1_var, text = "Urinal 1", bg="green", font=("Arial", 48, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__', 1))                                             
        self.button_urinal_1.pack(side = TOP, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")

        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_Urinals_top, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=X, expand=True, anchor='n')


        # Right Urinals
        frame_Urinals_side = ttk.Frame(frame_Urinals)
        frame_Urinals_side.pack(side = RIGHT, padx =3, pady=3, fill=BOTH, expand = True)
        frame_Urinals_side.config(relief = RIDGE, borderwidth = 3)

        tk.Label(frame_Urinals_side, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=X, expand=True, anchor='n')
        tk.Label(frame_Urinals_side, font=("Arial", 56, "bold"), justify=LEFT, text=" ").pack(side=BOTTOM, padx=3, pady=3, fill=X, expand=True, anchor='n')

        self.urinal_3_var = StringVar()
        self.urinal_3_var.set("Urinal 3")
        self.button_urinal_3 = tk.Button(frame_Urinals_side, textvariable=self.urinal_3_var, text = "Uniral 3", bg="green", font=("Arial", 48, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__',3))                                             
        self.button_urinal_3.pack(side = BOTTOM, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")        
        self.urinal_2_var = StringVar()
        self.urinal_2_var.set("Urinal 2")
        self.button_urinal_2 = tk.Button(frame_Urinals_side, textvariable=self.urinal_2_var, text = "Urinal 2", bg="green", font=("Arial", 48, "bold"),
                                                      command = lambda: self.handleButtonPress('__book_urinal__',2))                                             
        self.button_urinal_2.pack(side = BOTTOM, padx = 3, pady = 3, fill=BOTH, expand = True, anchor="w")


        self.root.mainloop()


    def handleButtonPress(self, command, stall_number):
        
        if command == '__book_stall__':
            if stall_number == 1: 
                if self.stall_1_var.get() == "Toilet Stall 1":
                    logging.debug("Booking Toilet Stall 1!")
                    self.button_stall_1.config(bg="red") 
                    self.stall_1_var.set("Toilet Stall 1: IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 1!")
                    self.button_stall_1.config( bg="green")
                    self.stall_1_var.set("Toilet Stall 1")
            elif stall_number == 2: 
                if self.stall_2_var.get() == "Toilet Stall 2":
                    logging.debug("Booking Toilet Stall 2!")
                    self.button_stall_2.config(bg="red") 
                    self.stall_2_var.set("Toilet Stall 2: IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 2!")
                    self.button_stall_2.config( bg="green")
                    self.stall_2_var.set("Toilet Stall 2")
            elif stall_number == 3: 
                if self.stall_3_var.get() == "Toilet Stall 3":
                    logging.debug("Booking Toilet Stall 3!")
                    self.button_stall_3.config(bg="red") 
                    self.stall_3_var.set("Toilet Stall 3: IN USE")
                else:
                    logging.debug("Releasing Toilet Stall 3!")
                    self.button_stall_3.config( bg="green")
                    self.stall_3_var.set("Toilet Stall 3")
                
        elif command == '__book_urinal__':
            if stall_number == 1:
                if self.urinal_1_var.get() == "Urinal 1":
                    logging.debug("Booking Urinal 1!")
                    self.button_urinal_1.config(bg="red") 
                    self.urinal_1_var.set("Urinal 1: IN USE")
                else:
                    logging.debug("Releasing Urinal 1!")
                    self.button_urinal_1.config(bg="green")
                    self.urinal_1_var.set("Urinal 1")
            elif stall_number == 2: 
                if self.urinal_2_var.get() == "Urinal 2":
                    logging.debug("Booking Urinal 2!")
                    self.button_urinal_2.config(bg="red") 
                    self.urinal_2_var.set("Urinal 2: IN USE")
                else:
                    logging.debug("Releasing Urinal 2!")
                    self.button_urinal_2.config( bg="green")
                    self.urinal_2_var.set("Urinal 2")
            elif stall_number == 3: 
                if self.urinal_3_var.get() == "Urinal 3":
                    logging.debug("Booking Urinal 3!")
                    self.button_urinal_3.config(bg="red") 
                    self.urinal_3_var.set("Urinal 3: IN USE")
                else:
                    logging.debug("Releasing Urinal 3!")
                    self.button_urinal_3.config( bg="green")
                    self.urinal_3_var.set("Urinal 3")

    def __init__(self):

        logging.basicConfig(level= logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')
        logging.debug('Start of toiletbooker.py')
        
        self.root = Tk()
        self.setupGUI()


def main():
        app = ToiletBooker()

if __name__ == "__main__": main()
