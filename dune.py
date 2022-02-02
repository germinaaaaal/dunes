from random import *
#hello
shades = ["▓","▒","░"]

for line in range(0,10):
	text = ""
	for column in range(0,18):
		text += shades[randint(0,2)]
	print(text)

print("\n")

for line in range(0,10):
	text = ""
	for column in range(0,10):
		text += shades[randint(0,2)]
	print(text)
