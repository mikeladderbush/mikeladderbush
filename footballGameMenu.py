import tkinter as tk
import sys
import re
import datetime
import time
import webbrowser
import os.path
from tkinter import ttk
from tkinter import *
import random
from tkinter.messagebox import showinfo
from tkinter import Button

#This method is designed to find a teams top 5 players, display their stats and computer their fantasy points.
#I plan on looking for a variable such as fantasy points from the url and displaying it back to the user.

def football_menu():
       
    football_menu = tk.Tk()
    football_menu.geometry('1250x500')
    football_menu.title('Football Game')
    football_menu_intro = Label(football_menu, text="Welcome to the Football Game Menu")
    football_menu_intro.pack()


