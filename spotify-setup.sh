#!/usr/env/bin bash

setup(){
	local userprompt="Please enter your username:"
	local passprompt="Please enter your password:"

	printf "%30s" $userprompt
	read  spuser
	printf "%30s" $passprompt
	read -s sppass

	

