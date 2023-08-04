#Jue Wu
#12/6/2022
#CS5001
#Final Project
#Testing the application Frame

#importing the tkinter module
import tkinter as tk
from tkinter import *
from tkinter import messagebox
#import Application class
from ApplicationFrame import KnittingApplication


def test_ApplicationFrame():
    #create a knitting application
    testapp = KnittingApplication()
    #name the title of the application
    testapp.master.title('This is the test application')
    testapp.label1 = tk.Label(text = "If there is a popped out application with entry box and 'Start knitting' submit botton. Then the application works.", bg = 'white', height = 3, width = 150)
    testapp.label1.pack()
    testapp.mainloop()



if __name__ == "__main__":
    test_ApplicationFrame()
    print()