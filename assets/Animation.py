from sjvisualizer import DataHandler, Canvas, BarRace
from typing import Optional
import json


class animator():
    '''
    filepath: Ubicacion absoluta o relativa de los datos en archivo .xlsx

    duration: duracion en milisegundos

    fps: fotogramas por segundo
    '''
    def __init__(
            self,
            filepath: str = None, 
            duration: float | int = 0.5,
            fps: int | None = 30,
            bars_colors: Optional[str] = None,
            bg_colors: tuple[int, int, int] = [13,16,23],
            fonts_colors:tuple[int,int,int] = [255,255,255]) -> None:
        
        self.filepath = filepath
        self.duration = duration
        self.fps = fps
        self.bars_colors = bars_colors
        self.bg_colors = bg_colors
        self.fonts_colors = fonts_colors
        self.container = Canvas.canvas(bg=bg_colors)
        try:
            if self.filepath == None:
                raise Exception(FileNotFoundError)
            elif self.bars_colors == None:
                self.bars_colors== {}
        except:
            pass
    

    def add_bars(self) -> None:
        df = DataHandler.DataHandler(excel_file=self.filepath, number_of_frames=self.fps*self.duration*60).df

        #Open json file
        bar_color = {}
        if self.bars_colors is not None:
            with open(self.bars_colors, encoding="utf8") as f:
                bar_color = json.load(f)

        #Create barchart
        barchart = BarRace.bar_race(df=df,
                            canvas = self.container.canvas,
                            colors = bar_color,
                            font_color = self.fonts_colors,
                            back_ground_color=self.bg_colors )
        self.container.add_sub_plot(barchart)
    

    def add_texts(self) -> None:
        df = DataHandler.DataHandler(excel_file=self.filepath, number_of_frames=self.fps*self.duration*60).df
        self.container.add_title("TRANSFERENCIA DE RECURSOS", color=self.fonts_colors)
        self.container.add_sub_title("2010-2022", color=self.fonts_colors)
        self.container.add_time(df=df, time_indicator="year", color=self.fonts_colors)
    

    def play_animation(self) -> None:
        self.container.play(fps=self.fps)