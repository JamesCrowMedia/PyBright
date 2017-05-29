from os import system
from time import sleep

def codesend(code):

	for x in range(code):
		system("/var/www/html/rfoutlet/codesend {0}".format(code))
		sleep(.1)
