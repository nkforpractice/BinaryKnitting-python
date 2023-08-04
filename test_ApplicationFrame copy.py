import unittest
import tkinter as tk
from tkinter import *
from MassyTools import *
import atexit
from ApplicationFrame import KnittingApplication
from unittest.mock import Mock

class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = tk()
        self.root.bind('<Key>', lambda e: print(self.root, e.keysym))

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_enter(self):
        v = KnittingApplication(self.root)
        v.pack()
        self.root.update_idletasks()

        # info
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.info_button.invoke()

        # quit
        def cancel():
            self.root.event_generate('<Tab>')
            self.root.event_generate('<Return>')

        v.after(100, cancel)
        v.quit_button.invoke()
        self.assertTrue(v.winfo_ismapped())    
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.quit_button.invoke()
        with self.assertRaises(tk.TclError):
            v.winfo_ismapped()


if __name__ == "__main__":
    unittest.main()
