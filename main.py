# -*- coding: utf-8 -*-

#===========================================================
# будильник с мелодией = случайный трек из плейлиста на youtube
#===========================================================

import os
import time as basetime # для избежания конфликта с datetime.time
from datetime import datetime, date, time, timedelta

import youtube_random_track

#===========================================================
# url плейлиста

# Top Tracks - Finland
playlist_url = 'https://www.youtube.com/playlist?list=PLFgquLnL59anFWmHlKJxf_px-u1TQ9SGy'
#===========================================================

def get_time_from_input(str_time):

	input_time_list = [int(item) for item in str_time.split()] 

	while len(input_time_list) < 3: 
		input_time_list.append(0)

	return input_time_list # всегда список с 3мя компонентами


def alarm_clock():

	print(datetime.now().strftime("The current time is: %H:%M:%S\n"))

	# mm, ss - опционально
	alarm_input_time_str = input("Type the 'hh mm ss' (separated by space) when you want to wake up: ")

	hh, mm, ss = get_time_from_input(alarm_input_time_str)
	alarm_time = time(hh, mm, ss)

	alarm_datetime = datetime.combine(date.today(), alarm_time)

	if alarm_datetime < datetime.now():
		alarm_datetime = alarm_datetime + timedelta(days=1)

	print("\nAlarm time:", alarm_datetime)

	time_to_wake_up = datetime.combine(date.today(), time()) + (alarm_datetime - datetime.now())
	print(time_to_wake_up.strftime("Remaining time to wake up: %H hours, %M minutes"))

	print("\nProcessing ...")

	while True:
		basetime.sleep(1)
		# print(current_datetime)
		current_datetime = datetime.now()
		if current_datetime > alarm_datetime:

			print("Alarm!")
			youtube_random_track.alarm(playlist_url)
			confirm = input("Press any key to confirm you wake up:\n")

			break

#===========================================================

alarm_clock()

#===========================================================