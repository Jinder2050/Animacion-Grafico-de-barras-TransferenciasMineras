from sjvisualizer import DataHandler, Canvas, BarRace
import json

class Visualizer:
    def __init__(self, data_file: str = 'assets/data/data.xlsx', fps: int = 60, duration: float = 0.5, colors_file: str = 'assets/colors.json', bg_colors: tuple[int, int, int] = (13, 16, 23), font_colors: tuple[int, int, int] = (255, 255, 255)) -> None:
        self.data_file = data_file
        self.fps = fps
        self.duration = duration
        self.colors_file = colors_file
        self.bg_colors = bg_colors
        self.font_colors = font_colors
        self.container = Canvas.canvas(bg=self.bg_colors)

    def add_bars(self) -> None:
        df = DataHandler.DataHandler(excel_file=self.data_file, number_of_frames=self.fps * self.duration * 60).df

        with open(self.colors_file, encoding='utf8') as f:
            bar_color = json.load(f)

        barchart = BarRace.bar_race(df=df,
                                    canvas=self.container.canvas,
                                    colors=bar_color,
                                    font_color=self.font_colors,
                                    back_ground_color=self.bg_colors)

        self.container.add_sub_plot(barchart)

    def add_text(self) -> None:
        df = DataHandler.DataHandler(excel_file=self.data_file, number_of_frames=self.fps * self.duration * 60).df
        self.container.add_title('TRANSFERENCIA DE RECURSOS', color=self.font_colors)
        self.container.add_sub_title('2010-2022', color=self.font_colors)
        self.container.add_time(df=df, time_indicator='year', color=self.font_colors)

    def play_animation(self) -> None:
        self.container.play(fps=self.fps)

