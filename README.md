# Cat-Stories-Video-Generator

## Project Overview

## Preliminary Outline
Each location will be a 1080x1920 png with each location being one scene, each scene will contain one character with it 
switching between different car memes to convey different emotions (shock, thinking, anger, determined).
The character will be a transparent video of the car, with the sound effect being part of the clip, lasting 5 to 7 seconds per clip.  

## JSON Input Format
Each video will be generated from a json file containing the backgrounds of the scenes, the clips used, the subtitles and 
their durations.  
Preliminary format:   
`
[
{
"scene_number": 1
"scene_background": "background.jpg"
"scene_duration": 15
"scene_start": 0
"clip_1": "car_looking_up_1.akm"
"clip_1_dur": 5
"clip_1_start": 0
"clip_2": "car_talking_1.akm"
"clip_2_dur": 5
"clip_2_start": 5
"title_1": "Your Super Power Is"
"title_1_dur": 15
"sub_1": "Can refill containers?"
"sub_1_dur": 4
"sub_1_start": 5
"sub_2": "What am I supposed to do with that?"
"sub_2_dur": 5
"sub_2_start": 9
"fx_1": "spinner.akm"
"fx_1_dur": 4.9
"fx_1_start": 0
}
{
"scene_number": 2
"scene_background": "school.jpg"
......
}
]
`
