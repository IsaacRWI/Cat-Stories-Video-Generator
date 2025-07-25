from moviepy import *

class Clip:
    def __init__(self, cl, dur, pos):
        self.cl = cl
        self.dur = int(dur)
        self.pos = pos

    def opening_layout(self):
        pos_center = (540, 1280)
        clip = VideoFileClip(self.cl).subclipped(0, self.dur).with_position(pos_center).resized(width=500)


