#Jue Wu
#12/6/2022
#CS5001
#Final Project
#Using tkinter to implement the application frame

#importing the tkinter module
import tkinter as tk
from tkinter import *
from tkinter import messagebox
#import function from message
from message import removeSpace
from message import toBinary
#import BinaryKnitting class
from BinaryKnitting import BinaryKnitting

class KnittingApplication(Frame):
    def __init__(self, master = None ):
        '''Constructor'''
        #inherit from the Frame 
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        '''
        Create the widgets of the application
        '''
        #using Label to build a text input instruction
        self.inputLabel = Label(self, text = "Please enter the text you want to knit in binary below: ", width = 150)
        self.inputLabel.pack()
        #using Entry function to build the text input box
        self.entry = Entry(self)
        self.entry.pack()
        
        #Using Button function to build a button which can implement the command that start 'knitting'
        self.button = tk.Button(text = 'Start knitting', command = self.knittingApp, height = 3, borderwidth = 2)
        self.button.pack()

        #using StringVar and Label function to make the window to represent the result
        self.t = tk.StringVar()
        self.t1 = tk.StringVar()
        self.t2 = tk.StringVar()
        self.l = tk.Label(self, textvariable = self.t, height = 3)
        self.l1 = tk.Label(self, textvariable = self.t1, height = 3)
        self.l2 = tk.Label(self, textvariable = self.t2, height = 13)
        self.l.pack()
        self.l1.pack()
        self.l2.pack()
        
    
    def knittingApp(self):
        try:
            #Get the message from the user then return to app 
            message = self.entry.get()
            #using conditional to handle error
            if not message.isascii():
                raise ValueError
            else:
                noSpaceM = removeSpace(message)
                finalM =  toBinary(noSpaceM)
                #build a new BinaryKnitting object
                knit = BinaryKnitting(finalM)
                #get the result and represent in show window
                self.t1.set(knit.knit())
                self.t.set(finalM)
                self.t2.set(knit.pattern(finalM))
        
        #Exception handling
        except ValueError:
            messagebox.showinfo("Warning","Invalid input!")
        

