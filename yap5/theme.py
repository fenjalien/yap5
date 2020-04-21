from typing import Tuple, Union
from .color import Color

class Theme(object):
    fill_: Union[Color, None]
    stroke_: Union[Color, None]
    stoke_weight_: float

    def __init__(self, fill=None, stroke=Color('black'), stroke_weight=1):
        self.fill_ = fill
        self.stroke_ = stroke
        self.stroke_weight_ = stroke_weight

    @property
    def fill(self):
        return self.fill_
    
    @fill.setter
    def fill(self, value: Union[Color, None]):
        assert value is None or isinstance(value, Color)
        self.fill_ = value
    
    @property
    def stroke(self):
        return self.stroke_
    
    @stroke.setter
    def stroke(self, value: Union[Color, None]):
        assert value is None or isinstance(value, Color)
        self.stroke_ = value

    @property
    def stroke_weight(self):
        return self.stroke_weight_
    
    @stroke_weight.setter
    def stroke_weight(self, value: float):
        self.stroke_weight_ = value
