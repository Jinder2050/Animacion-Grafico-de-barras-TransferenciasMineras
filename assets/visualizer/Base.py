from sjvisualizer import DataHandler, BarRace
from sjvisualizer import Canvas as cv
from typing import Optional, Dict, Tuple
import json


class Animator():

    def __init__(
            self,
            filepath: str | None = ...,
            duration: float | int = 0.5,
            fps: int | None = 30,
            bars_colors: Optional[Dict[str, Tuple[int, int, int]]] = None,
            bg_colors: tuple[int, int, int] = None,
            fonts_colors:tuple[int,int,int] = None,
            anim_title: str ='BARCHART ANIMATION',
            anim_subtitle: str ="",
            data_unit : str = "",
            ) -> None:
        
        self.filepath = filepath
        self.duration = duration
        self.fps = fps
        self.bars_colors = bars_colors
        self.bg_colors = bg_colors
        self.fonts_colors = fonts_colors
        self.anim_title = anim_title
        self.anim_subtitle = anim_subtitle
        self.container = cv.canvas(bg=bg_colors)


    def add_bars(self) -> None:
        """
        This method adds the bar graph
        """
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
                            back_ground_color=self.bg_colors)
        self.container.add_sub_plot(barchart)
    
    def add_bar_stripe(self):
        pass

    def add_texts(self) -> None:
        """
        Add title and subtitle
        """
        df = DataHandler.DataHandler(excel_file=self.filepath, number_of_frames=self.fps*self.duration*60).df
        self.container.add_title(self.anim_title, color=self.fonts_colors)
        self.container.add_sub_title(self.anim_subtitle, color=self.fonts_colors)
        self.container.add_time(df=df, time_indicator="year", color=self.fonts_colors)
    
    def play_animation(self) -> None:
        '''
        Run animation
        '''
        self.container.play(fps=self.fps)

    def methods(self) -> None:
        """
        Run all methods:
        -> add bars()
        -> add texts()
        -> play animation()
        """
        self.add_bars()
        self.add_texts()
        self.play_animation()

