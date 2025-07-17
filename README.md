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

## Prompt for Generating JSON File  
Context:  
You are a talented video editor for a short form content account, your job is to write a script for a 60 second short form video about a cat gaining an unusual superpower which it initially finds useless, before finding interesting ways to use them.
In the setting of the story, the people in the world are all cats and other animals.
The video should start with a clip of a cat looking up at a lottery spinner in scene 1 which reveals what superpower it will have for the day, after receiving its superpower, the cat should claim that that superpower is useless with a remark similar to "what am i supposed to do with that?"
In scene 2, the main character should meet up with a friend of his called sniffles, where they discuss what power he got and how useless it would be in daily life.
In scene 3, the main character then goes and gets in a specific situation where its power is useful or finds a unique and previously unthought of way to use its power.
In scene 4, a twist is added to the story where the video ends on a cliffhanger.
The tone of the video should be informal and funny, where unexpected twists are more than welcome.
The use the main character of the story finds for the superpower cannot be a game, it must be a useful use of the power. For example if the cat can see the amount of kills a person has, it can avoid them and report them to the police.
This time the superpower the cat is getting is the ability to see the number of times a person has killed another person.  
Format:  
The format for your response should be split into the 4 scenes, with each scene having a background, the characters in it, and the dialogue with the dialogue not exceeding 5 sentences per scene.