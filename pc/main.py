import customtkinter as ctk
from tkinter import *

import dashboardGegevens as gegevens

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1000x750")

stat1 = ctk.CTkLabel(
    master=app,
    text="",
    width=15,
    height=3,
    font=("Arial", 20, "bold"),
    wraplength=900,
)
stat1.place(x=20, y=100)


def displayAchievements(appid):
    ach = gegevens.achievements(appid)
    stat1.configure(text=ach)


def displayFriendList():
    stat1.configure(text="Niet gelukt, sorry!")
    friends = gegevens.friendlist()
    stat1.configure(text=friends)


def refreshFriendList():
    stat1.configure(text="Niet gelukt, sorry!")
    gegevens.refreshFriendList()
    displayFriendList()


b1 = ctk.CTkButton(
    master=app,
    text="Top 5 Games",
    width=15,
    height=5,
    font=("Arial", 20, "bold"),
)
b1.pack(side=LEFT, anchor=NW, padx=(0, 5))

b2 = ctk.CTkButton(
    master=app,
    text="Achievements",
    width=15,
    height=5,
    font=("Arial", 20, "bold"),
    command=lambda: [stat1.configure(text="Loading..."), displayAchievements(221100)],
)
b2.pack(side=LEFT, anchor=NW, padx=(5, 0))

getFriendsCanvas = ctk.CTkCanvas(
    master=app,
    width=15,
    height=5,
)
getFriendsCanvas.pack(side=LEFT, anchor=NW, padx=(5))

friendsButton = ctk.CTkButton(
    master=getFriendsCanvas,
    text="Friends",
    width=15,
    height=5,
    font=("Arial", 20, "bold"),
    command=displayFriendList,
)
friendsButton.pack(side=LEFT, anchor=NW)

friendsRefresh = ctk.CTkButton(
    master=getFriendsCanvas,
    text="r",
    width=5,
    height=5,
    font=("Arial", 20, "bold"),
    command=refreshFriendList,
)
friendsRefresh.pack(side=LEFT, anchor=NW)

app.mainloop()
