from sjvisualizer import DataHandler, Canvas, BarRace
from typing import Optional
import json


class Animator():
    '''
    filepath: Absolute or relative location of data in (*.xlsx) file !important

    duration: Duration for number of frames

    fps: Frames per second for number of frames

    bars_colors: Dictionary that holds color information for each of the data categories. Default is {}
        parameters:
            key: (str) -> correspond to the name of the data category (column)
            value: -> should be the RGB values of the color

    bg_colors: Global variable -> background color for container and To hide bars that fall outside of the top X, a square is drawn at the bottom of the visualization.

    fonts_colors: Global variable -> font color for texts in the visualization
    '''
    def __init__(
            self,
            filepath: str | None = ...,
            duration: float | int = 0.5,
            fps: int | None = 30,
            bars_colors: Optional[str] = None,
            bg_colors: tuple[int, int, int] = None,
            fonts_colors:tuple[int,int,int] = None,
            anim_title: str ='BARCHART ANIMATION',
            anim_subtitle: str ="",
            data_unit : str = "") -> None:
        
        self.filepath = filepath
        self.duration = duration
        self.fps = fps
        self.bars_colors = bars_colors
        self.bg_colors = bg_colors
        self.fonts_colors = fonts_colors
        self.anim_title = anim_title
        self.anim_subtitle = anim_subtitle
        self.data_unit = data_unit
        self.container = Canvas.canvas(bg=bg_colors)
        try:
            if self.filepath is None:
                raise Exception(FileNotFoundError)
            elif self.bars_colors == None:
                self.bars_colors== {}
            elif (self.bg_colors or self.fonts_colors) is None:
                raise Exception('bg_colors or fonts_color -> incorrect value')
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
                            back_ground_color=self.bg_colors,
                            unit=self.data_unit)
        self.container.add_sub_plot(barchart)
    

    def add_texts(self) -> None:
        df = DataHandler.DataHandler(excel_file=self.filepath, number_of_frames=self.fps*self.duration*60).df
        self.container.add_title(self.anim_title, color=self.fonts_colors)
        self.container.add_sub_title(self.anim_subtitle, color=self.fonts_colors)
        self.container.add_time(df=df, time_indicator="year", color=self.fonts_colors)
    

    def play_animation(self) -> None:
        self.container.play(fps=self.fps)


class Darkanimation(Animator):

    def __init__(self, filepath: str | None = ..., duration: float | int = 0.5, fps: int | None = 30, bars_colors: Optional[str] = None, bg_colors: tuple[int, int, int] = [13,16,23], fonts_colors: tuple[int, int, int] = [255, 255, 255], anim_title: str = 'BARCHART ANIMATION', anim_subtitle: str = "", data_unit: str = "") -> None:
        super().__init__(filepath, duration, fps, bars_colors, bg_colors, fonts_colors, anim_title, anim_subtitle, data_unit)

    def add_bars(self) -> None:
        return super().add_bars()
    
    def add_texts(self) -> None:
        return super().add_texts()
    
    def play_animation(self) -> None:
        return super().play_animation()

    
class Lightanimation(Animator):

    def __init__(self, filepath: str | None = ..., duration: float | int = 0.5, fps: int | None = 30, bars_colors: Optional[str] = None, bg_colors: tuple[int, int, int] = [255, 255, 255], fonts_colors: tuple[int, int, int] = [0, 0, 0], anim_title: str = 'BARCHART ANIMATION', anim_subtitle: str = "", data_unit: str = "") -> None:
        super().__init__(filepath, duration, fps, bars_colors, bg_colors, fonts_colors, anim_title, anim_subtitle, data_unit)

    def add_bars(self) -> None:
        return super().add_bars()
    
    def add_texts(self) -> None:
        return super().add_texts()
    
    def play_animation(self) -> None:
        return super().play_animation()