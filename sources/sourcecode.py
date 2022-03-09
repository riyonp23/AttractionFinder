# Attraction Finder by Riyon Praveen and Yash Vora Ap Submission 
# All credit given to Yash is labled in comments
# AP Classroom Submission  


# importing different library
from tkinter import *
from tkinter import messagebox
import os
import webbrowser
from gtts import gTTS
from playsound import playsound
import time as times

window = Tk()


# Defining functions

# Time variable functions
def display_selectedtime(choice):
    global time
    time = choice


# Money variable function
def display_selectedmoney(choice):
    global money
    money = choice


# Location variable function
def display_selectedlocation(choice):
    global location
    location = choice


# Age variable function
def display_selectedage(choice):
    global age
    age = choice


# Weather variable function
def display_selectedweather(choice):
    global weather
    weather = choice


# Background Functions
def on_enterplace(e):
    place.config(foreground="blue")


def on_leaveplace(e):
    place.config(foreground="white")


def callback(url):
    webbrowser.open_new_tab(url)


# Reset button function - Yash Vora
def reset():
    global time
    global money
    global location
    global age
    global weather
    clickedTime.set("Time")
    time = "Time"
    clickedMoney.set("Money")
    money = "Money"
    clickedDistance.set("Location")
    location = "Location"
    clickedAge.set("Age")
    age = "Age"
    clickedWeather.set("Weather")
    weather = "Weather"
    instruction.config(text="Start By Clicking On The Dropdowns Located To The Left And Hit Search When You Are Done")
    place.config(text="")
    canvaspic.delete("all")


# Function for deciding which attraction gets displayed through if - else statements - Yash Vora
def search():
    if time == "X" or money == "X" or location == "X" or age == "X" or weather == "X":
        messagebox.showerror(title="Error", message="Please Select An Option For All The Dropdowns")
        return
    if time == "Time" or money == "Money" or location == "Location" or age == "Age" or weather == "Weather":
        messagebox.showerror(title="Error", message="Please Select An Option For All The Dropdowns")
        return
    if time == "Night":
        if age == "0-17":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Tampa Riverwalk")
                    place.bind("<Button-1>", lambda e: callback("https://thetampariverwalk.com/"))
                    instruction.config(
                        text="The Riverwalk is an connecting all of the exciting attractions\nand\nneighborhoods that make up the incredible downtown",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img0)
                elif location == "State":
                    place.config(text="ICON Park")
                    place.bind("<Button-1>", lambda e: callback("https://iconparkorlando.com/"))
                    instruction.config(text="An Entertainment Complex Featuring Fun And Games For The Whole Family",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img1)
                elif location == "Nation":
                    place.config(text="San Diego Zoo")
                    place.bind("<Button-1>", lambda e: callback("https://sandiegozoowildlifealliance.org/"))
                    instruction.config(text="A Zoo Housing Over 12,000 Animals Of More Than 650 Species",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img2)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Bush Gardens Tampa")
                    place.bind("<Button-1>", lambda e: callback("https://buschgardens.com/"))
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img3)
                elif location == "State":
                    place.config(text="Sea World")
                    place.bind("<Button-1>", lambda e: callback("https://seaworld.com/orlando/"))
                    instruction.config(text="Experience Aquatic Animals and Thrill Rides At The Same Time",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img4)
                elif location == "Nation":
                    place.config(text="Monuments by Moonlight")
                    place.bind("<Button-1>", lambda e: callback(
                        "https://www.trolleytours.com/washington-dc/monuments-by-moonlight-tickets"))
                    instruction.config(text="A Monuments Tour Around Washington DC", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img5)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Florida Aquarium")
                    place.bind("<Button-1>", lambda e: callback("https://www.flaquarium.org/"))
                    instruction.config(
                        text="Rated One Of The Best Aquariums In The US\nExperience A Wide Variety Of Aquatic Animals",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img6)
                elif location == "State":
                    place.config(text="Tampa Bay Grand Prix")
                    place.bind("<Button-1>", lambda e: callback("https://tampabaygp.com/"))
                    instruction.config(text="Indoor Go-Karting Providing Safe And Fun Races", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img7)
                elif location == "Nation":
                    place.config(text="National Museum of the US Air Force")
                    place.bind("<Button-1>", lambda e: callback("https://www.nationalmuseum.af.mil/"))
                    instruction.config(text="Includes More Than 360 Different Aircraft And Missiles On Display",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img8)
        elif age == "18-50":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Club Prana")
                    place.bind("<Button-1>", lambda e: callback("https://clubprana.com/"))
                    instruction.config(text="A Splashy, Multilevel Venue With Different Vibes And Music",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img9)
                elif location == "State":
                    place.config(text="King's Island")
                    place.bind("<Button-1>", lambda e: callback("https://www.visitkingsisland.com/"))
                    instruction.config(text="From The Big Thrills Of Orion And Diamondback To Family Rides",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img10)
                elif location == "Nation":
                    place.config(text="Six Flags Magic Mountain")
                    place.bind("<Button-1>", lambda e: callback("https://www.sixflags.com/magicmountain"))
                    instruction.config(text="From Massive Monster Coasters To Family Fun Attractions",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img11)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Tiki Docks River Bar & Grill")
                    place.bind("<Button-1>", lambda e: callback("https://tikidocks.com/"))
                    instruction.config(text="Amazing Food With A Great View Of The Docks", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img12)
                elif location == "State":
                    place.config(text="Wall Street Plaza")
                    place.bind("<Button-1>", lambda e: callback("https://www.wallstplaza.net/"))
                    instruction.config(text="Complex Of 8 Diverse Bars\n&\nLively Block Parties Every Weekend",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img13)
                elif location == "Nation":
                    place.config(text="Hershey Park")
                    place.bind("<Button-1>", lambda e: callback("https://www.hersheypark.com/"))
                    instruction.config(
                        text="Thrilling Rides & Chocolate Adventure To Premier Dining And Spa Treatments",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img14)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Rox Rooftop Bar")
                    place.bind("<Button-1>", lambda e: callback("https://www.yelp.com/biz/rox-rooftop-bar-tampa"))
                    instruction.config(text="Tampa's Tallest Rooftop Bar Offers Smoked Cocktails And Unreal Views",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img15)
                elif location == "State":
                    place.config(text="Disney Park")
                    place.bind("<Button-1>", lambda e: callback("https://disneyparks.disney.go.com/"))
                    instruction.config(text="World's Most Magical Place", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img16)
                elif location == "Nation":
                    place.config(text="Ripley's Aquarium of the Smokies")
                    place.bind("<Button-1>", lambda e: callback("https://www.ripleyaquariums.com/gatlinburg/"))
                    instruction.config(text="Sprawling Aquarium Showcasing Sharks, Penguins & A Glass-Bottom Boat Ride",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img17)
        elif age == "50+":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Daytona Beach")
                    place.bind("<Button-1>", lambda e: callback("https://www.daytonabeach.com/"))
                    instruction.config(text="A Beach Where You Are Able To Drive On", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img18)
                elif location == "State":
                    place.config(text="Jingle Jam")
                    place.bind("<Button-1>", lambda e: callback("https://www.jinglejam.co.uk/"))
                    instruction.config(text="World's Biggest Charity Gaming Event", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img19)
                elif location == "Nation":
                    place.config(text="Bush Gardens WilliamsBurg")
                    place.bind("<Button-1>", lambda e: callback("https://buschgardens.com/"))
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img20)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Clearwater Beach")
                    place.bind("<Button-1>", lambda e: callback("https://visitclearwaterflorida.com/"))
                    instruction.config(text="A Beach With Some Of The Most Beautiful Waters You Will See",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img21)
                elif location == "State":
                    place.config(text="Destin City")
                    place.bind("<Button-1>", lambda e: callback("https://www.cityofdestin.com/"))
                    instruction.config(text="A City That Consists Of Many Gulf Courses", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img22)
                elif location == "Nation":
                    place.config(text="Knott's Berry Farm")
                    place.bind("<Button-1>", lambda e: callback("https://www.knotts.com/"))
                    instruction.config(text="An 57-Acre Theme Park That Has 4 Million Visitors Per Year",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img23)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Disney Cruise")
                    place.bind("<Button-1>", lambda e: callback("https://disneycruise.disney.go.com/"))
                    instruction.config(text="Onboard Is Equivalent To An Entirely Different Fairytale",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img24)
                elif location == "State":
                    place.config(text="Delray Beach")
                    place.bind("<Button-1>", lambda e: callback("https://www.delraybeachfl.gov/"))
                    instruction.config(text="Voted On As The Most Fun Small Town In America", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img25)
                elif location == "Nation":
                    place.config(text="Cedar Point, Sandusky")
                    place.bind("<Button-1>", lambda e: callback("https://www.cedarpoint.com/"))
                    instruction.config(text="17 Different Rides For You To Enjoy", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img26)
    elif time == "Day":
        pass
        if age == "0-17":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Lowry Park Zoo, Tampa")
                    place.bind("<Button-1>", lambda e: callback("https://zootampa.org/"))
                    instruction.config(text="A Fun And Interactive Zoo For All Ages At A Low Cost",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img27)
                elif location == "State":
                    place.config(text="Everglades")
                    place.bind("<Button-1>", lambda e: callback("https://www.nps.gov/ever/index.htm"))
                    instruction.config(text="A Tour Of The Incredible Variety Of Wildlife In Florida",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img28)
                elif location == "Nation":
                    place.config(text="Georgia Aquarium")
                    place.bind("<Button-1>", lambda e: callback("https://www.georgiaaquarium.org/"))
                    instruction.config(text="A View Of The Oceans Incredible Wildlife", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img29)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Top Golf")
                    place.bind("<Button-1>", lambda e: callback("https://topgolf.com/us/tampa/"))
                    instruction.config(text="A Fun Golfing And Dining Experience All In One", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img30)
                elif location == "State":
                    place.config(text="Fort Myers")
                    place.bind("<Button-1>", lambda e: callback("https://cityftmyers.com/"))
                    instruction.config(text="A Clean And Peaceful Beach With An Exquisite View", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img31)
                elif location == "Nation":
                    place.config(text="Coca Cola Factory")
                    place.bind("<Button-1>", lambda e: callback("https://www.worldofcoca-cola.com/"))
                    instruction.config(text="A Tour Of The History Of Coca Cola", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img32)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Adventure Island")
                    place.bind("<Button-1>", lambda e: callback(
                        "https://adventureisland.com/?gclid=CjwKCAiAo4OQBhBBEiwA5KWu_58TZQGnJi3IDnbvqg2OceZzxMYirsdqbQ3134HOGw5vC-nljgUIyxoC5WsQAvD_BwE&gclsrc=aw.ds"))
                    instruction.config(text="A Park Filled With Water Rides For All Ages", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img33)
                elif location == "State":
                    place.config(text="Magic Kingdom")
                    place.bind("<Button-1>", lambda e: callback("https://disneyparks.disney.go.com/"))
                    instruction.config(text="World's Most Magical Place", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img16)
                elif location == "Nation":
                    place.config(text="Smokey Mountain National Park")
                    place.bind("<Button-1>", lambda e: callback("https://www.nps.gov/grsm/index.htm"))
                    instruction.config(text="A National Park Like None Other With Amazing Hikes And Breathtaking Views",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img34)
        elif age == "18-50":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Florida Aquarium")
                    place.bind("<Button-1>", lambda e: callback("https://www.flaquarium.org/"))
                    instruction.config(
                        text="Rated One Of The Best Aquariums In The US\nExperience A Wide Variety Of Aquatic Animals",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img6)
                elif location == "State":
                    place.config(text="Kennedy Space Center")
                    place.bind("<Button-1>", lambda e: callback("https://www.kennedyspacecenter.com/"))
                    instruction.config(text="Features Exhibits And Displays SpaceCrafts", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img35)
                elif location == "Nation":
                    place.config(text="Yellow Stone National Park")
                    place.bind("<Button-1>", lambda e: callback("https://www.nps.gov/yell/index.htm"))
                    instruction.config(text="A Recreation Area Atop A Volcanic Hot Spot", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img36)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Bush Gardens WilliamsBurg")
                    place.bind("<Button-1>", lambda e: callback("https://buschgardens.com/"))
                    instruction.config(text="Experience Animals and Thrill Rides At The Same Time",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img20)
                elif location == "State":
                    place.config(text="Universal Studio")
                    place.bind("<Button-1>", lambda e: callback("https://www.universalorlando.com/web/en/us"))
                    instruction.config(text="A Theme Park For Movies, Televisions, And Other Entertainment Industries",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img37)
                elif location == "Nation":
                    place.config(text="Mount Rushmore")
                    place.bind("<Button-1>", lambda e: callback("https://www.nps.gov/moru/index.htm"))
                    instruction.config(text="A Mountain Engraved With US Presidents", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img38)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Orbital Paintball")
                    place.bind("<Button-1>", lambda e: callback("https://orbitalpaintball.com/"))
                    instruction.config(text="An Area Where You Can Battle Each Other With Paintball",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img39)
                elif location == "State":
                    place.config(text="St.Augustine")
                    place.bind("<Button-1>", lambda e: callback("https://www.citystaug.com/"))
                    instruction.config(text="An Amazing Historic City With A Major Background", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img40)
                elif location == "Nation":
                    place.config(text="Las Vegas Strip")
                    place.bind("<Button-1>", lambda e: callback("https://www.visitlasvegas.com/"))
                    instruction.config(
                        text="Lined Up With Upscale casino Hotels, the neon-soaked Strip is quintessential",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img41)
        elif age == "50+":
            pass
            if money == "$20-$50":
                pass
                if location == "Regional":
                    place.config(text="Tampa Museum Of Arts")
                    place.bind("<Button-1>", lambda e: callback("https://tampamuseum.org/"))
                    instruction.config(text="A Collection Of Old And New Art Work With Breathtaking Architecture",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img42)
                elif location == "State":
                    place.config(text="Orlando Science Center")
                    place.bind("<Button-1>", lambda e: callback("https://www.osc.org/"))
                    instruction.config(text="A Massive Museum That Allows People To Explore Science",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img43)
                elif location == "Nation":
                    place.config(text="Grand Canyon")
                    place.bind("<Button-1>", lambda e: callback("https://www.nps.gov/grca/index.htm"))
                    instruction.config(text="A National Park With Breathtaking Views And Hiking Trails",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img44)
            elif money == "$60-$100":
                pass
                if location == "Regional":
                    place.config(text="Tampa Bay History Center")
                    place.bind("<Button-1>", lambda e: callback("https://tampabayhistorycenter.org/"))
                    instruction.config(text="A Museum Of The History Of Tampa", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img45)
                elif location == "State":
                    place.config(text="Phillip and Patricia Frost Museum")
                    place.bind("<Button-1>", lambda e: callback("https://www.frostscience.org/"))
                    instruction.config(text="A Museum Full Of Ways To Explore Thrilling Science", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img46)
                elif location == "Nation":
                    place.config(text="Mall Of America")
                    place.bind("<Button-1>", lambda e: callback("https://www.mallofamerica.com/"))
                    instruction.config(text="A Mall With Many Shops And Activities To Keep You Busy All Day",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img47)
            elif money == "$100+":
                pass
                if location == "Regional":
                    place.config(text="Straz Center Show")
                    place.bind("<Button-1>", lambda e: callback("https://www.strazcenter.org/"))
                    instruction.config(text="A Center To Watch Amazing Performing Arts And Talent",
                                       font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img48)
                elif location == "State":
                    place.config(text="Gaylord Resort")
                    place.bind("<Button-1>", lambda e: callback(
                        "https://www.marriott.com/en-us/hotels/mcogp-gaylord-palms-resort-and-convention-center/photos/"))
                    instruction.config(
                        text="Over 400,000 sq.ft\nWith 10-acre Paradise Springs Water Park and\nGlass Cactus Nightclub",
                        font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img49)
                elif location == "Nation":
                    place.config(text="Library Of Congress")
                    place.bind("<Button-1>", lambda e: callback("https://www.loc.gov/"))
                    instruction.config(text="A Collection Of The Most Books In All Of America", font=("Courier", 10))
                    canvaspic.create_image(250, 137, image=img50)


# Attraction CANVAS
# Stores the images used in the program
images = ["riverwalk.png", "icon.png", "diego.png", "bushgardens.png", "seaworld.png", "monuments.png", "aquarium.png",
          "prix.png", "museum.png", "club.png", "kings-island.png", "flags.png", "docks.png", "wallstreet.png",
          "hershey.png", "rox.png", "disney.png", "ripley.png", "daytona.png", "jingle.png", "bushgardenswilliam.png",
          "clearwater.png", "destin.png", "berry.png", "disneycruise.png", "delray.png", "cedar.png", "zoo.png",
          "everglades.png", "georgia.png", "topgolf.png", "fortmyers.png", "coke.png", "adventure.png", "smoky.png",
          "space.png", "yellow.png", "universal.png", "mount.png", "paintball.png", "augustine.png", "las.png",
          "art.png", "orlando.png", "canyon.png", "history.png", "frost.png", "mall.png", "straz.png", "gaylord.png",
          "library.png"]

img0 = None
img1 = None
img2 = None
img3 = None
img4 = None
img5 = None
img6 = None
img7 = None
img8 = None
img9 = None
img10 = None
img11 = None
img12 = None
img13 = None
img14 = None
img15 = None
img16 = None
img17 = None
img18 = None
img19 = None
img20 = None
img21 = None
img22 = None
img23 = None
img24 = None
img25 = None
img26 = None
img27 = None
img28 = None
img29 = None
img30 = None
img31 = None
img32 = None
img33 = None
img34 = None
img35 = None
img36 = None
img37 = None
img38 = None
img39 = None
img40 = None
img41 = None
img42 = None
img43 = None
img44 = None
img45 = None
img46 = None
img47 = None
img48 = None
img49 = None
img50 = None

def imageCreator(list):
    
    # A For loop that automatically takes all the images in the list and places them in variables to be used later
    if len(list) > 50:
        for i in range(len(list)):
            globals()['img%s' % i] = PhotoImage(file="./assets/images/{}".format(list[i]))

imageCreator(images)

# Setting the screen 
window.maxsize(800, 500)
window.iconbitmap('./assets/application/logo.ico')
window.resizable(False, False)
window.config(bg="#36393F")
window.title("Attraction Finder")

left_frame = Frame(window, width=100, height=500, bg="#18191C")
left_frame.pack(side="left")
bottom_frame = Frame(window, width=800, height=100, bg="#18191C")
bottom_frame.pack(side="bottom")

time = "X"
money = "X"
location = "X"
age = "X"
weather = "X"

# Base Texts - Yash Vora
title = Label(window, text="Attraction Finder", bg="#36393F", foreground="white")
title.place(x=350, y=20)
title.config(font=("Courier", 14))
author = Label(window, text="Riyon Praveen & Yash Vora", bg="#36393F", foreground="white")
author.place(x=355, y=40)
author.config(font=("Courier", 8))
place = Label(bottom_frame, text="", bg="#18191C", foreground="white")
place.place(relx=.5, y=10, anchor='center')
place.config(font=("Courier", 12))
place.bind('<Enter>', on_enterplace)
place.bind('<Leave>', on_leaveplace)
instruction = Label(bottom_frame,
                    text="Start By Clicking On The Dropdowns Located To The Left And Hit Search When You Are Done",
                    bg="#18191C", foreground="white")
instruction.place(relx=.5, rely=.5, anchor='center')
instruction.config(font=("Courier", 10))

# AP Classroom Icon Image - Yash Vora
canvas = Canvas(left_frame, width=100, height=100, background='#18191C', bd=0, highlightthickness=0)
canvas.place(x=0, y=390)
img = PhotoImage(file="./assets/application/ap-logo.png")
canvas.create_image(0, 0, anchor=NW, image=img)

canvaspic = Canvas(window, width=500, height=275, background='#36393F', bd=0, highlightthickness=0)
canvaspic.place(x=200, y=100)

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
dropTime.place(x=10, y=25)
dropTime.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0,
                anchor="w", fg="white", activeforeground="white")

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
dropWeather = OptionMenu(left_frame, clickedWeather, *optionsWeather, command=display_selectedweather)
dropWeather.place(x=10, y=75)
dropWeather.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0,
                   anchor="w", fg="white", activeforeground="white")

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
dropMoney.place(x=10, y=125)
dropMoney.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0,
                 anchor="w", fg="white", activeforeground="white")

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
dropDistance.place(x=10, y=175)
dropDistance.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F",
                    highlightthickness=0, anchor="w", fg="white", activeforeground="white")

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
dropAge.place(x=10, y=225)
dropAge.config(width=7, height=1, bd=0, relief=FLAT, activebackground="#36393F", bg="#36393F", highlightthickness=0,
               anchor="w", fg="white", activeforeground="white")


# Functions for button - Yash
def about():
    messagebox.showinfo("Information",
                        "            2022 Attraction Finder\nCreated By Riyon Praveen & Yash Vora\n\nAny Questions or Bugs? Contact us now!\nemail: riyonpraveen23@gmail.com\nphone: 813-438-9484")

# Function for opening source.txt - Yash
def source():
    filepath = r'./sources/sources.txt'
    sources = messagebox.askyesno("Sources", "Open Source.txt?")
    if sources:
        os.startfile(os.path.normpath(filepath))
        return
    else:
        return


def on_enterabout(e):
    aboutButton.config(foreground="black")


def on_leaveabout(e):
    aboutButton.config(foreground="white")


def on_entersource(e):
    sourceButton.config(foreground="black")


def on_leavesource(e):
    sourceButton.config(foreground="white")


# Takes The Place name and Description Of Place and Plays A Text To Speech Audio
def texttospeech():
    try:
        path = "./assets/temp"
        file = "temp.txt"
        mainpath = "./assets/temp/temp.txt"
        lang = 'en'
        mp3name = 'output'
        with open(os.path.join(path, file), 'w') as fp:
            fp.write(place.cget("text") + "," + instruction.cget("text"))
        fh = open(mainpath, "r")
        myText = fh.read().replace("\n", " ")
        output = gTTS(text=myText, lang=lang, slow=False)
        output.save("%s.mp3" % os.path.join(path, mp3name))
        fh.close()
        playsound('./assets/temp/output.mp3', block=False)
        times.sleep(3)
        deletefiles()
    except PermissionError:
        messagebox.showerror("Error", "Please Don't Spam The Button")


# Deletes The Temp Files
def deletefiles():
    try:
        if os.path.exists("./assets/temp/temp.txt"):
            os.remove("./assets/temp/temp.txt")
        if os.path.exists("./assets/temp/output.mp3"):
            os.remove("./assets/temp/output.mp3")
    except PermissionError:
        deletefiles()


# Button Search
searchButton = Button(left_frame, text="Search", command=search)
searchButton.place(x=10, y=275)
searchButton.config(bd=0, relief=FLAT, bg="#36393F", activebackground="#36393F", fg="white", activeforeground="white")

# Button Reset
resetButton = Button(left_frame, text="Reset", command=reset)
resetButton.place(x=60, y=275)
resetButton.config(bd=0, relief=FLAT, bg="#36393F", activebackground="#36393F", fg="white", activeforeground="white")

# Button About
aboutButton = Button(window, text="ABOUT", command=about)
aboutButton.place(x=755, y=0)
aboutButton.config(bd=0, relief=FLAT, bg="#36393F", activebackground="#36393F", fg="white", activeforeground="white",
                   font=("Courier", 10))
aboutButton.bind('<Enter>', on_enterabout)
aboutButton.bind('<Leave>', on_leaveabout)

# Button Sources
sourceButton = Button(window, text="SOURCE", command=source)
sourceButton.place(x=700, y=0)
sourceButton.config(bd=0, relief=FLAT, bg="#36393F", activebackground="#36393F", fg="white", activeforeground="white",
                    font=("Courier", 10))
sourceButton.bind('<Enter>', on_entersource)
sourceButton.bind('<Leave>', on_leavesource)

# Button Text To Speech
speechIcon = PhotoImage(file="./assets/application/speaker.png")
img_label = Label(image=speechIcon)
speechButton = Button(bottom_frame, image=speechIcon, command=texttospeech)
speechButton.config(background="#18191C", foreground="#18191C", activebackground="#18191C", activeforeground="#18191C",
                    bd=0)
speechButton.place(x=0, y=0)

# Execute tkinter
window.mainloop()
