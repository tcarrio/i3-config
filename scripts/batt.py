#!/usr/bin/env python
import subprocess
import sys


full=u'\uf240'
thre=u'\uf241'
half=u'\uf242'
quar=u'\uf243'
empt=u'\uf244'

battery=[full,thre,half,quar,empt]

def main():
	battstat = subprocess.check_output(['upower','-i','/org/freedesktop/UPower/devices/DisplayDevice'])

	is_charging=False
	for stat in battstat.strip().split(b'\n'):
		if(b"charging" in stat):
			is_charging=True
		elif(b"percentage:" in stat):
			charge=int(stat.split()[1][:-1])
	
	if(testing):
		print("is_charging: %s"%is_charging)
		print("charge: %s"%charge)
	charge_index=0
	
	if is_charging:
		print(battery[charge_index])
		charge_index = (charge_index+1)%len(battery)
	else:
		if(charge>85):
			print(full) # full battery
		elif(charge>60):
			print(thre) # 3/4 battery
		elif(charge>35):
			print(half) # half battery
		elif(charge>10):
			print(quar) # quarter battery
		else:
			print(empt) # empty battery
	
	
if __name__=="__main__":
	testing = 1 if(len(sys.argv)>1 and sys.argv[1] in ("--test","-t")) else 0
	main()
