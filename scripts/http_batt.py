#!/usr/bin/env python
import subprocess
import sys
from flask import Flask

app = Flask("battery")
full=u'\uf240'
thre=u'\uf241'
half=u'\uf242'
quar=u'\uf243'
empt=u'\uf244'	
battery=[full,thre,half,quar,empt]
low_batt=[quar,empt]
charge_index=0
low_index=0

@app.route("/")
def get_batt(testing=0):
	battstat = subprocess.check_output(['upower','-i','/org/freedesktop/UPower/devices/DisplayDevice'])
	is_charging=False
	global charge_index
	for stat in battstat.strip().split(b'\n'):
		if(b"state" in stat):
			is_charging = False if (b"discharging" in stat) else True
		elif(b"percentage:" in stat):
			charge=int(stat.split()[1][:-1])
	
	if(testing):
		print("is_charging: %s"%is_charging)
		print("charge: %s"%charge)

	if is_charging:
		charge_index = (charge_index-1)%len(battery)
		return "{} {}%".format(battery[charge_index],charge)	
	else:
		if(charge>85):
			return "{} {}%".format(full,charge) # full battery
		elif(charge>60):
			return "{} {}%".format(thre,charge) # 3/4 battery
		elif(charge>35):
			return "{} {}%".format(half,charge) # half battery
		elif(charge>10):
			return "{} {}%".format(quar,charge) # quarter battery
		else:
			low_index = (low_index-1)%len(low_batt)
			return "{} {}%".format(low_batt[low_index],charge) # empty battery


if __name__=="__main__":
	app.run()
# 	testing = 1 if(len(sys.argv)>1 and sys.argv[1] in ("--test","-t")) else 0
# 	main(testing)
