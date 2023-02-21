from visualizer.Base import Animator
from typing import Optional, Dict, Tuple

class Darkanimation(Animator):
    """
    filepath: Absolute or relative location of data in (*.xlsx) file !important

    duration: Duration for number of frames

    fps: Frames per second for number of frames

    bars_colors: Dictionary that holds color information for each of the data categories. Default is {}
        parameters:
            key: (str) -> correspond to the name of the data category (column)
            value: -> should be the RGB values of the color

    bg_colors: Global variable -> background color for container and To hide bars that fall outside of the top X, a square is drawn at the bottom of the visualization.

    fonts_colors: Global variable -> font color for texts in the visualization

    anim title: Main animation title

    anim_subtitle: Animation subtitle


    """

    def __init__(self, filepath: str | None = ..., duration: float | int = 0.5, fps: int | None = 30, bars_colors: Optional[Dict[str, Tuple[int, int, int]]] = None, bg_colors: tuple[int, int, int] = (13,16,23), fonts_colors: tuple[int, int, int] = [255, 255, 255], anim_title: str = 'BARCHART ANIMATION', anim_subtitle: str = "") -> None:
        super().__init__(filepath, duration, fps, bars_colors, bg_colors, fonts_colors, anim_title, anim_subtitle)

    def methods(self) -> None:
        return super().methods()

class Lightanimation(Animator):
    """
    filepath: Absolute or relative location of data in (*.xlsx) file !important

    duration: Duration for number of frames

    fps: Frames per second for number of frames

    bars_colors: Dictionary that holds color information for each of the data categories. Default is {}
        parameters:
            key: (str) -> correspond to the name of the data category (column)
            value: -> should be the RGB values of the color

    bg_colors: Global variable -> background color for container and To hide bars that fall outside of the top X, a square is drawn at the bottom of the visualization.

    fonts_colors: Global variable -> font color for texts in the visualization

    anim title: Main animation title

    anim_subtitle: Animation subtitle


    """

    def __init__(self, filepath: str | None = ..., duration: float | int = 0.5, fps: int | None = 30, bars_colors: Optional[Dict[str, Tuple[int, int, int]]] = None, bg_colors: tuple[int, int, int] = (255, 255, 255), fonts_colors: tuple[int, int, int] = [0, 0, 0], anim_title: str = 'BARCHART ANIMATION', anim_subtitle: str = "") -> None:
        super().__init__(filepath, duration, fps, bars_colors, bg_colors, fonts_colors, anim_title, anim_subtitle)
    
    def methods(self) -> None:
        return super().methods()