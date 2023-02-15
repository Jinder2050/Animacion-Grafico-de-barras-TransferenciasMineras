from sjvisualizer import DataHandler, Canvas, BarRace
import json

#Data
data  = 'assets\data\data.xlsx'

#barchart color
with open("assets\colors.json", encoding="utf8") as f:
    bar_color = json.load(f)

#Global colors (variable)
bg_colors = (13, 16, 23)
fonts_color = (255,255,255)

#=================================================================================#
#Container - tkinter
container = Canvas.canvas(bg=bg_colors)

#DataHandler
fps = 60 
duration = 0.5
df = DataHandler.DataHandler(excel_file=data, number_of_frames=fps*duration*60).df

#Add bar 

barchart = BarRace.bar_race(df=df, canvas=container.canvas, colors=bar_color, font_color=fonts_color, back_ground_color=bg_colors)
container.add_sub_plot(barchart)

# Add tittle / subtitle / time indicator
container.add_title("TRANSFERENCIA DE RECURSOS", color=fonts_color)
container.add_sub_title("2010-2022", color=fonts_color)
container.add_time(df=df, time_indicator="year", color=fonts_color)

#Play the animation
container.play(fps=fps)

# fonts color