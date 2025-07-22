from moviepy import *

class Scene:
    def __init__(self, sn_bg, sn_dur, cl1, cl1_dur, cl1_pos, cl2, cl2_dur, cl2_pos, cl3, cl3_dur, cl3_pos, cl4, cl4_dur, cl4_pos, cl5, cl5_dur, cl5_pos, cl6, cl6_dur, cl6_pos,
                 ttl1, ttl1_dur,
                 sub1, sub1_dur, sub1_pos, sub2, sub2_dur, sub2_pos, sub3, sub3_dur, sub3_pos, sub4, sub4_dur, sub4_pos,
                 sub5, sub5_dur,sub5_pos, sub6, sub6_dur, sub6_pos, sub7, sub7_dur, sub7_pos, sub8, sub8_dur, sub8_pos):
        self.bg = sn_bg
        self.dur = sn_dur
