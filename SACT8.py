# %%


#   DEPRACATED
#   SWITCH TO simonGame.ipynb for full proyect



import ipywidgets as widgets
import time
import random
from IPython.display import display

#TODO Fix imports related to google collab

#---- Colors ----
colors = ["red", "blue", "green", "yellow"]

normalColors = {"red" : "#820707",
                "blue" : "#071782",
                "green" : "#055c0d",
                "yellow" : "#5c5a05"}

brightColors = {"red" : "#D51212",
                "blue" : "#132BC1",
                "green" : "#11bb22",
                "yellow" : "#bebb0b"}

#---- Game configuration ----
gameSequence = [] #List of colors the game is choosing
userSequence = []
score = 0
gameStatus = "Waiting" #Maybe an enum with Waiting, showing and playing

#---- UI ----

#Instruction label
label = widgets.HTML(
    value = "<h1>Presiona <b>JUGAR</b> para comenzar</h1>",
    layout = widgets.Layout(margin = "10px")
)


#Button
play_button = widgets.Button(
    description = "PLAY",
    button_style = "success",
    layout = widgets.Layout(width="150px", height="40px", margin="10px")
)

#Game buttons
game_buttons = {}

for color in colors:
    game_buttons[color] = widgets.Button(
        description = "",
        layout = widgets.Layout(width="100px", height="100px", margin="5px")
    )
    #Assign color for each button
    game_buttons[color].style.button_color = normalColors[color]

#Button rows
row1 = widgets.HBox([game_buttons["red"], game_buttons["blue"]])
row2 = widgets.HBox([game_buttons["green"], game_buttons["yellow"]])

#Container for UI elements
gameContainer = widgets.VBox([
    label,
    row1,
    row2,
    play_button
], layout = widgets.Layout(align_items = "center", background_color = "#222222", padding = "15px", border_radius = "10px", width = "300px"))

display(gameContainer)
# %%
