from os import system
from time import sleep

def codesend(code):

	for x in range(3):
                
		system("/var/www/html/rfoutlet/codesend {0}".format(code))
		sleep(.1)
