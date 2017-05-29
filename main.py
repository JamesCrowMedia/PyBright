from os import system
from time import sleep

for x in range(3):
	system("/var/www/html/rfoutlet/codesend 4543795")
	sleep(.1)

sleep(10)

for x in range(3):
        system("/var/www/html/rfoutlet/codesend 4543804")
        sleep(.1)

