from moviepy import *

class Clip:
    def __init__(self, cl, dur, pos):
        self.cl = cl
        self.dur = int(dur)
        """match pos:
            case center:
                self.pos = (540, 1280)
        """
        positions = {"center" : (540, 1280), "center_l" : (360, 1280), "center_r" : (720, 1280)}
        self.pos = positions[pos]

    def opening_layout(self):
        # center = (540, 1280)
        # clip = VideoFileClip(self.cl).subclipped(0, self.dur).with_position(self.pos).resized(width=500)
        print(self.pos)


