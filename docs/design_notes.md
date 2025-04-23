# Space Tracks Timer & Activity Tracker

A Simple Tool For Overworked Developers

Created: 2024/03/17

Updated: 2024/03/17

Author: jjradler

## Summary

As a neurodivergent technologist and developer, I run into manifold problems with quotidian tasks such as: 

	1. 	Time Blocking: 
	 	1. 	I ignore my timers
	 	2. 	I forget to reset my timers
	 	3. 	I don’t get up and stretch for hours on end and wind up feeling like garbage. 
	 	4. 	My timers are not flexible enough without manually resetting them each time, which is problematic and flow-destroying. 
	2. 	Time Tracking: 
	 	1. 	I know I did work, but I have no recollection of what exactly I did. It slips from my memory, especially if I solved a problem. 
	 	2. 	I work alone most of the time and therefore have nobody to say “good work” after putting in the time. 
	 	3. 	I have trouble remembering what it was I did all day when filling out a time card. I have tried to make notes as I go, but I lose them or forget I ever had them. 
	3. 	Checking my Reminders for things I had to do that day *besides my day job.*
	4. 	Remembering what day it is or what day of the week it is. 
	5. 	Remembering what it was I was doing and where I stopped when I took my time-blocking break. 
	6. 	Remembering how many time blocking cycles have already elapsed. 

Furthermore, I find most existing tools do not fit into my workflow very well. Either they require I use my phone, which is immensely distracting, or they are not “in my face” enough to keep me from straight-up ignoring them. If they are “in my face”, I find them discouraging or abrasive and I stop using them. 

I built this tool primarily for myself. The point is to keep it as simple as possible in scope, features, and requirements while providing extensability and flexability for other developers to add features without needing to radically alter the core application. 

## Features: 

1. A Pomodoro-type activity burst timer. 
2. A field for entering notes and reminders with a limited number of characters (inspired by Asana).
3. The timer asks you to describe what you were working on briefly. It uses this to help you drop back into context when you finish your break. 
4. The timer tells you when your break time has elapsed with an audible (eventually configurable) chime or other waveform/sound. 
5. A set of configurable responses and reminders for different times of the day. 
6. A configurable set of time-blocks that can be sequenced differently. 
7. A startup/reminder/checklist. 
8. A logging function that can generate a formatted plaintext report of activities. 
9. A VERY simple, but configurable UI with very few widgets. 
10. Multiple users can log in to the application, but there is a default user profile. 
11. Initial configuration is minimal. 
12. Time blocks can be altered on the fly, but the changes to the time blocks are tracked and recorded in the log. 
13. A reminder list for non-work related tasks. It asks when you need to have them done when you create the task. 

## Requirements: 

1. Minimal use of external libraries: use mainly Python internal libraries. 
2. Keep a `requirements.txt` file.