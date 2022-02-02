from tkinter import *
from tkinter import messagebox

window = Tk()


# Functions
def display_selectedtime(choice):
    global time
    time = choice


def display_selectedmoney(choice):
    global money
    money = choice


def display_selectedlocation(choice):
    global location
    location = choice


def display_selectedage(choice):
    global age
    age = choice


def search():
    if time == "X" or money == "X" or location == "X" or age == "X":
        messagebox.showerror(title="Error", message="Please Select An Option For All The Dropdowns")
        return

    if time == "Night":
        if age == "0-17":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Tampa Riverwalk")
                    instruction.config(text="The Riverwalk is an connecting all of the exciting attractions\nand\nneighborhoods that make up the incredible downtown", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img2)
                elif location == "State":
                    place.config(text="ICON Park")
                    instruction.config(text="An Entertainment Complex Featuring Fun And Games For The Whole Family", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img3)
                elif location == "Nation":
                    place.config(text="San Diego Zoo")
                    instruction.config(text="A Zoo Housing Over 12,000 Animals Of More Than 650 Species", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img4)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Bush Gardens")
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img5)
                elif location == "State":
                    place.config(text="Sea World")
                    instruction.config(text="Experience Aquatic Animals and Thrill Rides At The Same Time", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img6)
                elif location == "Nation":
                    place.config(text="Monuments by Moonlight")
                    instruction.config(text="A Monuments Tour Around Washington DC", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img7)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Florida Aquarium")
                    instruction.config(text="Rated One Of The Best Aquariums In The US\nExperience A Wide Variety Of Aquatic Animals", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img8)
                elif location == "State":
                    place.config(text="Tampa Bay Grand Prix")
                    instruction.config(text="Indoor Go-Karting Providing Safe And Fun Races", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img9)
                elif location == "Nation":
                    place.config(text="National Museum of the US Air Force")
                    instruction.config(text="Includes More Than 360 Different Aircrafts And Missiles On Display", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img10)
        elif age == "18-50":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="The Dali")
                    instruction.config(text="An Art Museum Dedicated To The Works Of Salavdor Dali", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img11)
                elif location == "State":
                    place.config(text="A.J's Water Adventures")
                    instruction.config(text="A Cruise For 1.5 Hours\nWith Great Music And Exploring Dolphins", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img12)
                elif location == "Nation":
                    place.config(text="Monterey Bay Aquarium")
                    instruction.config(text="First Aquarium To Exhibit A Living Kelp Forest", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img13)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Club Prana")
                    instruction.config(text="A Splashy, Multilevel Venue With Different Vibes And Music", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img14)
                elif location == "State":
                    place.config(text="Wall Street Plaza")
                    instruction.config(text="Complex Of 8 Diverse Bars\nAnd\nLively Block Parties Every Weekend", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img15)
                elif location == "Nation":
                    place.config(text="National Aquarium")
                    instruction.config(text="One Of The Largest Aquariums, Housing Around 20,000 Animals", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img16)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Gaylord Resort")
                    instruction.config(text="Over 400,000 sq.ft\nWith 10-acre Paradise Springs Water Park and\nGlass Cactus Nightclub", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img17)
                elif location == "State":
                    place.config(text="Fort Lauderdale")
                    instruction.config(text="Known For Its Beaches And Boating Canals", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img18)
                elif location == "Nation":
                    place.config(text="Ripley's Aquarium of the Smokies")
                    instruction.config(text="Sprawling Aquarium Showcasing Sharks, Penguins & A Glass-Bottom Boat Ride", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img19)
        elif age == "50+":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Daytona Beach")
                    instruction.config(text="A Beach Where You Are Able To Drive On", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img20)
                elif location == "State":
                    place.config(text="A.J's Water Adventures")
                    instruction.config(text="A Cruise For 1.5 Hours\nWith Great Music And Exploring Dolphins",font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img12)
                elif location == "Nation":
                    place.config(text="Bush Gardens")
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img21)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Clearwater Beach")
                    instruction.config(text="A Beach With Some Of The Most Beautiful Waters You Will See", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img22)
                elif location == "State":
                    place.config(text="Destin City")
                    instruction.config(text="A City That Consists Of Many Gulf Courses", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img23)
                elif location == "Nation":
                    place.config(text="Knott's Berry Farm")
                    instruction.config(text="An 57-Acre Theme Park That Has 4 Million Visitors Per Year", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img24)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Daytona Beach")
                    instruction.config(text="A Beach Where You Are Able To Drive On", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img20)
                elif location == "State":
                    place.config(text="Delray Beach")
                    instruction.config(text="Voted On As The Most Fun Small Town In America", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img25)
                elif location == "Nation":
                    place.config(text="Cedar Point, Sandusky")
                    instruction.config(text="17 Different Rides For You To Enjoy", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img26)
    elif time == "Day":
        pass
        if age == "0-17":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Sky Zone")
                    instruction.config(text="A BIG Trampoline Park", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img27)
                elif location == "State":
                    place.config(text="IFly")
                    instruction.config(text="Experience Sky-Diving", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img28)
                elif location == "Nation":
                    place.config(text="Adler Planetarium")
                    instruction.config(text="A Museum Based Of Astronomy", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img29)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Tampa Bay Grand Prix")
                    instruction.config(text="Indoor Go-Karting Providing Safe And Fun Races", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img9)
                elif location == "State":
                    place.config(text="Xtreme Action Park")
                    instruction.config(text="Indoor Go-Karting Providing Safe And Fun Races", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img30)
                elif location == "Nation":
                    place.config(text="Empire State Building")
                    instruction.config(text="One Of The Biggest Buildings, Consisting Of 102 Stories", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img31)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Raymond James Stadium")
                    instruction.config(text="A Multi-Purpose Stadium For Sports Such As Baseball, Football, Etc.", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img32)
                elif location == "State":
                    place.config(text="Ripley's Aquarium of the Smokies")
                    instruction.config(text="Sprawling Aquarium Showcasing Sharks, Penguins & A Glass-Bottom Boat Ride", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img19)
                elif location == "Nation":
                    place.config(text="Bryce Canyon National Park")
                    instruction.config(text="A Canyon Park That Consists Of Many Trails To Take", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img33)
        elif age == "18-50":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Florida Aquarium")
                    instruction.config(text="Rated One Of The Best Aquariums In The US\nExperience A Wide Variety Of Aquatic Animals", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img8)
                elif location == "State":
                    place.config(text="Kennedy Space Center")
                    instruction.config(text="Features Exhibits And Displays SpaceCrafts", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img34)
                elif location == "Nation":
                    place.config(text="Yellow Stone National Park")
                    instruction.config(text="A Recreation Area Atop A Volcanic Hot Spot", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img35)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Bush Gardens")
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img5)
                elif location == "State":
                    place.config(text="Universal Studio")
                    instruction.config(text="A Theme Park For Movies, Televisions, And Other Entertainment Industries", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img36)
                elif location == "Nation":
                    place.config(text="Mount Rushmore")
                    instruction.config(text="A Mountain Engraved With US Presidents", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img37)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Orbital Paintball")
                    instruction.config(text="An Area Where You Can Battle Each Other With Paintball", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img38)
                elif location == "State":
                    place.config(text="Volcano Bay")
                    instruction.config(text="Universal's Volcano Bay Water Theme Park", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img39)
                elif location == "Nation":
                    place.config(text="Las Vegas Strip")
                    instruction.config(text="Lined Up With Upscale casino Hotels, the neon-soaked Strip is quintessential", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img40)
        elif age == "50+":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Daytona Beach")
                    instruction.config(text="A Beach Where You Are Able To Drive On", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img20)
                elif location == "State":
                    place.config(text="A.J's Water Adventures")
                    instruction.config(text="A Cruise For 1.5 Hours\nWith Great Music And Exploring Dolphins",font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img12)
                elif location == "Nation":
                    place.config(text="Bush Gardens")
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img21)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Clearwater Beach")
                    instruction.config(text="A Beach With Some Of The Most Beautiful Waters You Will See", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img22)
                elif location == "State":
                    place.config(text="Destin City")
                    instruction.config(text="A City That Consists Of Many Gulf Courses", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img23)
                elif location == "Nation":
                    place.config(text="Knott's Berry Farm")
                    instruction.config(text="An 57-Acre Theme Park That Has 4 Million Visitors Per Year", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img24)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Daytona Beach")
                    instruction.config(text="A Beach Where You Are Able To Drive On", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img20)
                elif location == "State":
                    place.config(text="Delray Beach")
                    instruction.config(text="Voted On As The Most Fun Small Town In America", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img25)
                elif location == "Nation":
                    place.config(text="Cedar Point, Sandusky")
                    instruction.config(text="17 Different Rides For You To Enjoy", font=("Courier", 10))
                    canvasPic.create_image(250, 137, image=img26)


window.maxsize(800, 500)
window.iconbitmap('./assets/logo.ico')
window.resizable(False, False)
window.config(bg="#36393F")
window.title("Attracion Finder")
  
left_frame = Frame(window, width=100, height=500, bg="#18191C")
left_frame.pack( side = "left")
bottom_frame = Frame(window, width=800, height=100, bg="#18191C")
bottom_frame.pack( side = "bottom")

time = "X"
money = "X"
location = "X"
age = "X"

#Text
title = Label(window, text="Attraction Finder", bg="#36393F", foreground="white")
title.place(x=350,y=20)
title.config(font =("Courier", 14))
author = Label(window, text="Made By Riyon Praveen, Aaron Bijoy, & Yash Vora", bg="#36393F", foreground="white")
author.place(x=280, y=40)
author.config(font=("Courier", 8))
place = Label(bottom_frame, text="", bg="#18191C", foreground="white")
place.place(relx=.5, y=10, anchor='center')
place.config(font=("Courier", 12))
instruction = Label(bottom_frame, text="Start By Click On The Dropdowns Located To The Left And Hit Search When You Are Done", bg="#18191C", foreground="white")
instruction.place(relx=.5, rely=.5, anchor='center')
instruction.config(font=("Courier", 10))


# FBLA Icon Image
canvas = Canvas(left_frame, width=100, height=100, background='#18191C', bd=0, highlightthickness=0)
canvas.place(x=0, y=400)
img = PhotoImage(file="./assets/fbla-logo.png")
canvas.create_image(0, 0, anchor=NW, image=img)

# Attraction CANVAS
img2 = PhotoImage(file="./assets/riverwalk.png")
img3 = PhotoImage(file="./assets/icon.png")
img4 = PhotoImage(file="./assets/diego.png")
img5 = PhotoImage(file="./assets/bushgardens.png")
img6 = PhotoImage(file="./assets/seaworld.png")
img7 = PhotoImage(file="./assets/monuments.png")
img8 = PhotoImage(file="./assets/aquarium.png")
img9 = PhotoImage(file="./assets/prix.png")
img10 = PhotoImage(file="./assets/museum.png")
img11 = PhotoImage(file="./assets/venue.png")
img12 = PhotoImage(file="./assets/boat.png")
img13 = PhotoImage(file="./assets/monterey.png")
img14 = PhotoImage(file="./assets/club.png")
img15 = PhotoImage(file="./assets/wallstreet.png")
img16 = PhotoImage(file="./assets/national.png")
img17 = PhotoImage(file="./assets/gaylord.png")
img18 = PhotoImage(file="./assets/fort.png")
img19 = PhotoImage(file="./assets/ripley.png")
img20 = PhotoImage(file="./assets/daytona.png")
img21 = PhotoImage(file="./assets/bushgardenswilliam.png")
img22 = PhotoImage(file="./assets/clearwater.png")
img23 = PhotoImage(file="./assets/destin.png")
img24 = PhotoImage(file="./assets/berry.png")
img25 = PhotoImage(file="./assets/delray.png")
img26 = PhotoImage(file="./assets/cedar.png")
img27 = PhotoImage(file="./assets/skyzone.png")
img28 = PhotoImage(file="./assets/ifly.png")
img29 = PhotoImage(file="./assets/adler.png")
img30 = PhotoImage(file="./assets/xtreme.png")
img31 = PhotoImage(file="./assets/empire.png")
img32 = PhotoImage(file="./assets/raymond.png")
img33 = PhotoImage(file="./assets/bryce.png")
img34 = PhotoImage(file="./assets/space.png")
img35 = PhotoImage(file="./assets/yellow.png")
img36 = PhotoImage(file="./assets/universal.png")
img37 = PhotoImage(file="./assets/mount.png")
img38 = PhotoImage(file="./assets/paintball.png")
img39 = PhotoImage(file="./assets/bay.png")
img40 = PhotoImage(file="./assets/las.png")
canvasPic = Canvas(window, width=500, height=275, background='#36393F', bd=0, highlightthickness=0)
canvasPic.place(x=200, y=100)


# Time
optionsTime = [
    "Day",
    "Night"
]

# datatype of menu text
clickedTime = StringVar()

# initial menu text
clickedTime.set("Time")

# Create Dropdown menu
dropTime = OptionMenu(left_frame, clickedTime, *optionsTime, command=display_selectedtime)
dropTime.place(x=10,y=25)
dropTime.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0, anchor="w", fg="white", activeforeground="white")

# Weather
optionsWeather = [
    "Hot",
    "Cold"
]

# datatype of menu text
clickedWeather = StringVar()

# initial menu text
clickedWeather.set("Weather")

# Create Dropdown menu
dropWeather = OptionMenu(left_frame, clickedWeather, *optionsWeather)
dropWeather.place(x=10,y=75)
dropWeather.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0, anchor="w", fg="white", activeforeground="white")

# Money
optionsMoney = [
    "$20-$50",
    "$60-$100",
    "$100+"
]

# datatype of menu text
clickedMoney = StringVar()

# initial menu text
clickedMoney.set("Money")

# Create Dropdown menu
dropMoney = OptionMenu(left_frame, clickedMoney, *optionsMoney, command=display_selectedmoney)
dropMoney.place(x=10,y=125)
dropMoney.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0, anchor="w", fg="white", activeforeground="white")

# Distance
optionsDistance = [
    "Regional",
    "State",
    "Nation"
]

# datatype of menu text
clickedDistance = StringVar()

# initial menu text
clickedDistance.set("Location")

# Create Dropdown menu
dropDistance = OptionMenu(left_frame, clickedDistance, *optionsDistance, command=display_selectedlocation)
dropDistance.place(x=10,y=175)
dropDistance.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0, anchor="w", fg="white", activeforeground="white")

# Age
optionsAge = [
    "0-17",
    "18-50",
    "50+"
]

# datatype of menu text
clickedAge = StringVar()

# initial menu text
clickedAge.set("Age")

# Create Dropdown menu
dropAge = OptionMenu(left_frame, clickedAge, *optionsAge, command=display_selectedage)
dropAge.place(x=10,y=225)
dropAge.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0, anchor="w", fg="white", activeforeground="white")

# Button
searchButton = Button(left_frame, text="Search", command=search)
searchButton.place(x=10,y=275)
searchButton.config(bd=0, relief=FLAT, bg="#36393F", activebackground="#36393F", fg="white", activeforeground="white")


# Execute tkinter
window.mainloop()