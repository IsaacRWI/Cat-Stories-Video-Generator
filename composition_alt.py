from moviepy import *

class Clip:
    def __init__(self, cl, dur, posx, posy):
        self.cl = cl
        self.dur = int(dur)
        self.posx = posx
        self.posy = posy

    def opening_layout(self):
        clip = VideoFileClip(self.cl).subclipped(0, self.dur).with_position((self.posx, self.posy)).resized(width=500)


