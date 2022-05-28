#things to include in the game. 
#play calling
#player stat percentages: speed, arm strength, strength, acceleration, juking, stamina, discipline, IQ, ball handling, grip strength
#player names, teams
#draft
#training
#fitting in the right systems/teams
#team chemistry
#coach skill

import tkinter as tk
import re
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Button

main_menu = tk.Tk()
main_menu.geometry('175x200')
main_menu.title('Main Menu')

menu = tk.Listbox(
    main_menu,
    height=0,
    selectmode='browse')

global teams
global user_team

user_team = ''

teams = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati",
         "Cleveland", "Dallas", "Denver", "Detroit", "Green Bay", "Houston", "Indianapolis",
         "Jacksonville", "Kansas City", "Las Vegas", "Los Angeles C", "Los Angeles R", 
         "Miami", "Minnesota", "New England", "New Orleans", "New York G", "New York J", 
         "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee",
         "Washington"]

def team_story(user_team):

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

    return team_dict.get(user_team, "")

def root():

    root = tk.Tk()
    root.geometry('200x750')
    root.title('Listbox')
 
    teams = ["Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago", "Cincinnati",
         "Cleveland", "Dallas", "Denver", "Detroit", "Green Bay", "Houston", "Indianapolis",
         "Jacksonville", "Kansas City", "Las Vegas", "Los Angeles C", "Los Angeles R", 
         "Miami", "Minnesota", "New England", "New Orleans", "New York G", "New York J", 
         "Philadelphia", "Pittsburgh", "San Francisco", "Seattle", "Tampa Bay", "Tennessee",
         "Washington"]

    teams_var = tk.StringVar(value=teams)

    listbox = tk.Listbox(
        root,
        listvariable = teams_var,
        height=32,
        selectmode='browse'
        )
    
    listbox.insert(0,*teams)

    listbox.grid(
        column=0,
        row=2,
        sticky='nwes'
        )

    def selected_item(user_team):
        for i in listbox.curselection():
            print(listbox.get(i))
            global my_team
            my_team = listbox.get(i)

    listbox.bind('<Button-1>',selected_item)

    button1=Button(root, text="Exit and Save", command = root.destroy)
    button1.grid(row=1,column=0)

    root.mainloop()

def new_game_menu():
    new_game_menu = tk.Tk()
    new_game_menu.geometry('300x300')
    new_game_menu.title('New Game')

    start=Button(new_game_menu, text="Start", command = root)
    start.grid(row=0,column=0)

    team_box = tk.Listbox(
    new_game_menu,
    height=5,
    selectmode='browse'
    )

    team_box.grid(
    column=0,
    row=1,
    sticky='nwes'
    )
    
    new_game_menu.mainloop()

def load_game_menu():
    load_game_menu = tk.Tk()
    load_game_menu.geometry('300x300')
    load_game_menu.title('Load Game')

    load_game_menu.mainloop()

button2=Button(main_menu, text="New Game", command = new_game_menu)
button2.grid(row=2,column=0)
button3=Button(main_menu, text="Load Game", command = load_game_menu)
button3.grid(row=3,column=0)

main_menu.mainloop()