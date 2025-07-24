from moviepy import *

class Clip:
    def __init__(self, cl, dur, pos):
        self.cl = cl
        self.dur = int(dur)
        self.pos = pos

    def opening_layout(self):
        clip = VideoFileClip(self.cl).subclipped(0, self.dur).with_position((self.posx, self.posy)).resized(width=500)


