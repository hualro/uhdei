#!/bin/python

import time

base = time.time()
sleep = raw_input("Time to wait in seconds: ")
time.sleep(int(sleep))

if(time.time() - base <= 60):
	print("Too soon")
else:
	print("Ok")

