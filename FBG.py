#These are all of the imports I used in order to create this program. They are used to read and write files, open the web browser and enable the Tkinter GUI.

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
import Gambling_game
import top_players
import footballGameMenu
import comboGame


#This is the first Tkinter window, it is created with the Tk function and the size/shape is determined by the geometry function.
#The title is the top part of the window and is determined by the title function.

main_menu = tk.Tk()
main_menu.geometry('500x200')
main_menu.title('Main Menu')

#This label is a short text section that is inserted into the main_menu window.

main_label=Label(main_menu,text="Welcome to my football game!\n "
+ "This is an early attempt at making the GUI for what will eventually be\n "
+ "a fully fledged football/betting simulator.")
main_label.pack()

#Here I set two global variables which will be used within other methods later.

global teams
global my_team

#Initializing the variable.

my_team = ''

#This method uses the user selected team and connects it to a background story via a dictionary. All of the background stories are sourced from wikipedia.

def team_story(my_team):

    team_dict = {
        "Arizona": "\n  The Arizona Cardinals are a professional American football team based in the Phoenix metropolitan area.\n" 
            + "The Cardinals compete in the National Football League (NFL) as a member club of the National Football Conference (NFC) West division.\n"
            + "The team was founded as the Morgan Athletic Club in 1898, and is the oldest continuously run professional football team in the United States.\n"
            + "The Cardinals play their home games at State Farm Stadium, which opened in 2006 and is located in the northwestern suburb of Glendale.\n",

        "Atlanta": "\n  The Atlanta Falcons are a professional American football team based in Atlanta.\n"
            + "The Falcons compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) South division.\n"
            + "The Falcons joined the NFL in 1965[5] as an expansion team, after the NFL offered then-owner Rankin Smith a franchise to keep him from joining the rival American Football League (AFL).\n",

        "Baltimore": "\n    The Baltimore Ravens are a professional American football team based in Baltimore.\n"
            + "The Ravens compete in the National Football League (NFL) as a member club of the American Football Conference (AFC) North division.\n"
            + "The team plays its home games at M&T Bank Stadium and is headquartered in Owings Mills, Maryland.\n",

        "Buffalo": "\n     The Buffalo Bills are a professional American football team based in the Buffalo–Niagara Falls metropolitan area.\n"
            + "They compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) East division.\n"
            + "The team plays its home games at Highmark Stadium in Orchard Park, New York.\n"
            + "Founded in 1960 as a charter member of the American Football League (AFL), they joined the NFL in 1970 following the AFL–NFL merger.\n"
            + "The Bills' name is derived from an All-America Football Conference (AAFC) franchise from Buffalo that was in turn named after western frontiersman Buffalo Bill.\n"
            + "Drawing much of its fanbase from Western New York, the Bills are the only NFL team that plays home games in that state.\n"
            + "The franchise is owned by Terry and Kim Pegula, who purchased the Bills after the death of original owner Ralph Wilson in 2014.",

        "Carolina": "\n     The Carolina Panthers are a professional American football team based in Charlotte, North Carolina.\n"
            + "The Panthers compete in the National Football League (NFL), as a member club of the league's National Football Conference (NFC) South division.\n"
            + "The team is headquartered in Bank of America Stadium in Uptown Charlotte; the stadium also serves as the team's home field.\n"
            + "The Panthers are supported throughout the Carolinas; although the team has played its home games in Charlotte since 1996,\n"
            + "they played their home games at Memorial Stadium in Clemson, South Carolina during its first season.\n"
            + "The team hosts its annual training camp at Wofford College in Spartanburg, South Carolina.",

        "Chicago": "\n     The Chicago Bears are a professional American football team based in Chicago.\n"
            + "The Bears compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) North division.\n"
            + "The Bears have won nine NFL Championships, including one Super Bowl,\n"
            + "and hold the NFL record for the most enshrinees in the Pro Football Hall of Fame and the most retired jersey numbers.\n"
            + "The Bears have also recorded more victories than any other NFL franchise.",

        "Cincinnati": "\n   The Cincinnati Bengals are a professional American football franchise based in Cincinnati.\n"
            + "The Bengals compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) North division.\n"
            + "The club's home stadium is Paul Brown Stadium, located in downtown Cincinnati.\n"
            + "Cincinnati's divisional opponents are the Baltimore Ravens, Cleveland Browns and Pittsburgh Steelers.",

        "Cleveland": "\n    The Cleveland Browns are a professional American football team based in Cleveland.\n"
            + "Named after original coach and co-founder Paul Brown, they compete in the National Football League (NFL) as a member club of the American Football Conference (AFC)\n"
            + "North division. The Browns play their home games at FirstEnergy Stadium, which opened in 1999, with administrative offices and training facilities in Berea,\n"
            + "Ohio. The Browns' official club colors are brown, orange, and white. They are unique among the 32 member franchises of the NFL in that they do not have a logo\n"
            + "on their helmets.",

        "Dallas": "\n   The Dallas Cowboys are a professional American football team based in the Dallas–Fort Worth metroplex.\n"
            + "The Cowboys compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) East division.\n"
            + "The team is headquartered in Frisco, Texas, and plays its home games at AT&T Stadium in Arlington, Texas, which opened for the 2009 season.\n"
            + "The stadium took its current name prior to the 2013 season. In January 2020 it was announced that Mike McCarthy had been hired as head coach of the Cowboys.\n"
            + "He is the ninth in the team’s history. McCarthy follows Jason Garrett, who coached the team from 2010–2019.",

        "Denver": "\n   The Denver Broncos are a professional American football franchise based in Denver.\n"
            + "The Broncos compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) West division.\n"
            + "The team is headquartered in Dove Valley, Colorado and plays home games at Empower Field at Mile High in Denver, Colorado.",

        "Detroit": "\n  The Detroit Lions are a professional American football team based in Detroit.\n"
            + "The Lions compete in the National Football League (NFL) as a member of the National Football Conference (NFC) North division.\n"
            + "The team plays its home games at Ford Field in Downtown Detroit.",

        "Green Bay": "\n    The Green Bay Packers are a professional American football team based in Green Bay, Wisconsin.\n"
            + "The Packers compete in the National Football League (NFL) as a member club of the National Football Conference (NFC) North division.\n"
            + "It is the third-oldest franchise in the NFL, dating back to 1919, and is the only non-profit, community-owned major league professional\n"
            + "sports team based in the United States. Home games have been played at Lambeau Field since 1957.",

        "Houston": "\n   The Houston Texans are a professional American football team based in Houston.\n"
            + "The Texans compete in the National Football League (NFL) as a member club of the American Football Conference (AFC) South division.\n"
            + "The team plays its home games at NRG Stadium.",

        "Indianapolis": "\n     The Indianapolis Colts are an American football team based in Indianapolis.\n"
            + "The Colts compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) South division.\n"
            + "Since the 2008 season, the Colts have played their games in Lucas Oil Stadium.\n"
            + "Previously, the team had played for over two decades (1984–2007) at the RCA Dome.\n" 
            + "Since 1987, the Colts have served as the host team for the NFL Scouting Combine.",

        "Jacksonville": "\n     The Jacksonville Jaguars are a professional football franchise based in Jacksonville, Florida.\n"
            + "The Jaguars compete in the National Football League (NFL) as a member club of the American Football Conference (AFC) South division.\n"
            + "The team plays its home games at TIAA Bank Field. Founded alongside the Carolina Panthers in 1995 as an expansion team,\n"
            + "the Jaguars originally competed in the AFC Central until they were realigned to the AFC South in 2002.\n"
            + "The franchise is owned by Shahid Khan, who purchased the team from original majority owner Wayne Weaver in 2011.",

        "Kansas City": "\n      The Kansas City Chiefs are a professional American football team based in Kansas City, Missouri.\n"
            + "They compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) west division.",

        "Las Vegas": "\n    The Las Vegas Raiders are a professional American football team based in the Las Vegas metropolitan area.\n"
            + "The Raiders compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) West division.\n"
            + "The Raiders play their home games at Allegiant Stadium in Paradise, Nevada, and are headquartered in Henderson, Nevada.",

        "Los Angeles C": "\n    The Los Angeles Chargers are a professional American football team based in the Los Angeles metropolitan area.\n"
            + "The Chargers compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) West division.\n"
            + "The Chargers play their home games at SoFi Stadium in Inglewood, California, which the club shares with the Los Angeles Rams.",

        "Los Angeles R": "\n    The Los Angeles Rams are a professional American football team based in the Los Angeles metropolitan area.\n"
            + "The Rams compete in the National Football League (NFL) as a member of the National Football Conference (NFC) West division.\n"
            + "The Rams play their home games at SoFi Stadium in Inglewood, which they share with the Los Angeles Chargers.",

        "Miami": "\n    The Miami Dolphins are a professional American football team based in the Miami metropolitan area.\n"
            + "They compete in the National Football League (NFL) as a member team of the league's American Football Conference (AFC) East division.\n"
            + "The team plays its home games at Hard Rock Stadium, located in the northern suburb of Miami Gardens, Florida.\n"
            + "The team is currently owned by Stephen M. Ross. The Dolphins are the oldest professional sports team in Florida.\n"
            + "Of the four AFC East teams, the Dolphins are the only team in the division that was not a charter member of the American Football League (AFL).\n"
            + "The Dolphins were also the first football team in the southeast, along with the Atlanta Falcons.",

        "Minnesota": "\n    The Minnesota Vikings are a professional American football team based in Minneapolis.\n"
            + "They compete in the National Football League (NFL) as a member club of the National Football Conference (NFC) North division.\n"
            + "Founded in 1960 as an expansion team, the team began play the following year. They are named after the vikings of ancient Scandinavia,\n"
            + "reflecting the prominent Scandinavian American culture of Minnesota. The team plays its home games at U.S. Bank Stadium in the Downtown East section of Minneapolis.",

        "New England": "\n      The New England Patriots are a professional American football team based in the Greater Boston area.\n"
            + "The Patriots compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) East division.\n"
            + "The team plays its home games at Gillette Stadium in Foxborough, Massachusetts, which is 22 miles (35 km)[5] southwest of downtown Boston.",

        "New Orleans": "\n      The New Orleans Saints are a professional American football team based in New Orleans.\n"
            + "The Saints compete in the National Football League (NFL) as a member of the league's National Football Conference (NFC) South division.\n"
            + "Since 1975, the team plays its home games at Caesars Superdome after utilizing Tulane Stadium during its first eight seasons.\n"
            + "Founded by John W. Mecom Jr., David Dixon, and the city of New Orleans on November 1, 1966, the Saints joined the NFL as an expansion team in 1967.\n"
            + "They are named after the jazz music heritage of New Orleans and the spiritual hymn 'When the Saints Go Marching In'.",

        "New York G": "\n       The New York Giants are a professional American football team based in the New York metropolitan area.\n"
            + "The Giants compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) East division.\n"
            + "The team plays its home games at MetLife Stadium (shared with the New York Jets) in East Rutherford, New Jersey, 5 miles (8 km) west of New York City.\n"
            + "The Giants hold their summer training camp at the Quest Diagnostics Training Center at the Meadowlands Sports Complex.",

        "New York J": "\n       The New York Jets are a professional American football team based in the New York metropolitan area.\n"
            + "The Jets compete in the National Football League (NFL) as a member club of the league's American Football Conference (AFC) East division.\n"
            + "The Jets play their home games at MetLife Stadium (shared with the New York Giants) in East Rutherford, New Jersey, 5 miles (8.0 km) west of New York City.\n"
            + "The team is headquartered in Florham Park, New Jersey. The franchise is legally organized as a limited liability company under the name New York Jets, LLC.",

        "Philadelphia": "\n     The Philadelphia Eagles are a professional American football team based in Philadelphia.\n"
            + "The Eagles compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) East division.\n"
            + "The team plays its home games at Lincoln Financial Field.",

        "Pittsburgh": "\n       The Pittsburgh Steelers are a professional American football team based in Pittsburgh.\n"
            + "The Steelers compete in the National Football League (NFL) as a member club of the American Football Conference (AFC) North division.\n"
            + "Founded in 1933, the Steelers are the seventh-oldest franchise in the NFL, and the oldest franchise in the AFC.",

        "San Francisco": "\n        The San Francisco 49ers are a professional American football team based in the San Francisco Bay Area.\n"
            + "The 49ers compete in the National Football League (NFL) as a member of the league's National Football Conference (NFC) West division.\n"
            + "The team plays its home games at Levi's Stadium in Santa Clara, California, located 38 miles (61 km) southeast of San Francisco in the heart of Silicon Valley.\n"
            + "Since 1988, the 49ers have been headquartered in Santa Clara. The name '49ers' comes from the prospectors who arrived in Northern California in the 1849 Gold Rush.",

        "Seattle": "\n      The Seattle Seahawks are a professional American football team based in Seattle.\n"
            + "The Seahawks compete in the National Football League (NFL) as a member club of the league's NFC West, which they joined in 2002.\n"
            + "The club entered the NFL as an expansion team in 1976. From 1977 to 2001 Seattle was assigned to the AFC West.\n"
            + "They have played their home games at Lumen Field in Seattle's SoDo neighborhood since 2002,\n"
            + "having previously played home games in the Kingdome (1976–1999) and Husky Stadium (1994 and 2000–2001). They are currently coached by Pete Carroll.",

        "Tampa Bay": "\n      The Tampa Bay Buccaneers are a professional American football team based in Tampa, Florida.\n"
            + "The Buccaneers compete in the National Football League (NFL) as a member club of the league's National Football Conference (NFC) South division.\n"
            + "The club joined the NFL in 1976 as an expansion team, along with the Seattle Seahawks,\n"
            + "and played its first season in the American Football Conference (AFC) West division. Prior to the 1977 season,\n"
            + "Tampa Bay switched conferences and divisions with Seattle, becoming a member of the NFC Central division. During the 2002 league realignment,\n"
            + "the Buccaneers joined three former NFC West teams to form the NFC South.\n"
            + "The club is owned by the Glazer family and plays its home games at Raymond James Stadium in Tampa.",

        "Tennessee": "\n    The Tennessee Titans are a professional American football team based in Nashville, Tennessee.\n"
            + "The Titans compete in the National Football League (NFL) as a member club of the American Football Conference (AFC) South division.",

        "Washington": "\n   The Washington Football Team is a professional American football team based in the Washington metropolitan area.\n"
            + "Formerly known as the Washington Redskins, the team competes in the National Football League (NFL) as a member club of the NFC East division.\n"
            + "The team plays its home games at FedExField in Landover, Maryland; its headquarters and training facility are in Ashburn, Virginia.\n"
            + "The team has played more than 1,000 games and is one of only five in the NFL with more than 600 total victories.\n" 
            + "It was the first NFL franchise with an official marching band and a fight song, 'Hail to the Redskins'.\n"
            + "Washington is valued at roughly US$4.2 billion according to Forbes, making them the fifth-most valuable franchise in the NFL.",
    }

    return team_dict.get(my_team, "")

#The new game menu creates a window in the same fashion that the main menu does, but then has off-branching windows and methods within.

def new_game_menu():
    main_menu.destroy()
    new_game_menu = tk.Tk()
    new_game_menu.geometry('150x150')
    new_game_menu.title('New Game')
    new_label=Label(new_game_menu,text="Choose your team!")
    new_label.pack()

    #The root method creates a window with a listbox which the user will be able to interact with in order to select their team of choice.

    def root():
        root = tk.Tk()
        root.geometry('300x750')
        root.title('Listbox')
 
        #This is a list of teams that the user will be able to choose from.

        teams = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati",
            "Cleveland", "Dallas", "Denver", "Detroit", "Green Bay", "Houston", "Indianapolis",
            "Jacksonville", "Kansas City", "Las Vegas", "Los Angeles C", "Los Angeles R", 
            "Miami", "Minnesota", "New England", "New Orleans", "New York G", "New York J", 
            "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee",
            "Washington"]

        #The teams_var variable is set to a string variable with this method.

        teams_var = tk.StringVar(value=teams)

        #This creates the listbox, which will be placed within the window with the ".pack()" function.

        listbox = tk.Listbox(
            root,
            listvariable = teams_var,
            height=32,
            selectmode='browse'
            )
    
        #"insert" places all the of the values from the teams list into the listbox starting from index 0.

        listbox.insert(0,*teams)
        listbox.pack()

        #This method is used to determine which item the user selected within the listbox. It then takes that selection and puts it into a global variable.
        #Putting the selection into a global variable allows it to be used later in the code.

        def selected_item(user_team):
            for i in listbox.curselection():
                print(listbox.get(i))
                global my_team
                my_team = listbox.get(i)
                global flavor_text
                flavor_text = team_story(listbox.get(i))
        
        #The listbox is bound to the double click of an item. Once this occurs the "selected_item" method will run.

        listbox.bind('<Button-1>',selected_item)

        #The game_menu method opens after a team has been selected and closes the previous windows. It will use the same functions as before in order to display the users team.

        def game_menu():
            new_game_menu.destroy()
            root.destroy()
            game_menu = tk.Tk()
            game_menu.geometry('1250x500')
            game_menu.title('Menu')
            new_label=Label(game_menu,text=my_team)
            new_label.pack()
            new_flavor_label=Label(game_menu, text = flavor_text)
            new_flavor_label.pack()

            #Because the user is starting a new game the program checks whether there is a previous save file or not.
            #If there is an old save file it will be overwritten.
            #These save files are text files created by the program and the users previously chosen team is written in the file.

            if os.path.isfile('savefile1.txt'):
                save_file = open("savefile1.txt", "w")
                save_file.write(my_team)
                save_file.close()
            else:
                save_file = open("savefile1.txt", "x")
                save_file.close()
                save_file = open("savefile1.txt", "w")
                save_file.write(my_team)
                save_file.close()
            
            #This method is used to open a website if the user wants more information.

            def webstats():webbrowser.open('https://www.nfl.com/')
            
            #Buttons are created and placed within the window lasts in order for the program to recognize the previously written methods they redirect to.
            #These buttons are placed within the window and once clicked activate the connected method.

            stats=Button(game_menu, text="Current News and Record", command = webstats)
            stats.pack()
            fantasy=Button(game_menu, text="Top Fantasy Players", command = top_players.top_players)
            fantasy.pack()
            gambling_game2=Button(game_menu, text="New Gambling Game", command = Gambling_game.gambling_menu)
            gambling_game2.pack()
            football_game2=Button(game_menu, text="New Football Only Game", command = footballGameMenu.football_menu)
            football_game2.pack()
            combo_game2=Button(game_menu, text="New Combo Game", command = comboGame.combo_menu)
            combo_game2.pack()

            #The "mainloop" of the method is closed so that once the code runs through it is certain to have completed.

            game_menu.mainloop()

        button1=Button(root, text="Start", command = game_menu)
        button1.pack()

        root.mainloop()

    start=Button(new_game_menu, text="Start", command = root)
    start.pack()
    back=Button(new_game_menu, text="Quit", command = new_game_menu.destroy)
    back.pack()

    new_game_menu.mainloop()

#The load_game_menu is the same as the new_game_menu except it skips the team selection process and looks for a save file.
#If it finds a savefile it will take the users team and directly bring the user to the team menu.

def load_game_menu():
    def game_menu():
            game_menu = tk.Tk()
            game_menu.geometry('1250x500')
            game_menu.title('Menu')
            if os.path.isfile('savefile1.txt'):
                save_file = open("savefile1.txt", "r")
                my_team = save_file.read()
            else:
                print("There is no save file")
                quit()

            new_label=Label(game_menu,text=my_team)
            new_label.pack()
            flavor_text = team_story(my_team)
            new_flavor_label=Label(game_menu,text=flavor_text)
            new_flavor_label.pack()
            
            def webstats():webbrowser.open('https://www.nfl.com/')
                
            stats=Button(game_menu, text="Current News and Record", command = webstats)
            stats.pack()
            fantasy=Button(game_menu, text="Top Fantasy Players", command = top_players.top_players)
            fantasy.pack()
            gambling_game1=Button(game_menu, text="Continue Gambling Game", command = Gambling_game.gambling_menu)
            gambling_game1.pack()
            football_game1=Button(game_menu, text="Continue Football Only Game", command = footballGameMenu.football_menu)
            football_game1.pack()
            combo_game1=Button(game_menu, text="Continue Combo Game", command = comboGame.combo_menu)
            combo_game1.pack()
            game_menu.mainloop()
    game_menu()

button2=Button(main_menu, text="New Game", command = new_game_menu)
button2.pack()
button3=Button(main_menu, text="Continue", command = load_game_menu)
button3.pack()

main_menu.mainloop()
