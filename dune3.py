from random import *
#hello
shades = ["█","▓","▒","░"," "]

mx = []
key = ""

pr = choice(shades)
l = 0
for line in range(0,20):
	text = ""
	t = []
	c = 0
	for column in range(0,36):
		sh = shades[:]
		sh.append(pr)
		ind = shades.index(pr)
		if ind > 0:
			sh.append(shades[ind-1])
		else:
			sh.append(shades[0])
		if ind < len(shades)-1:
			sh.append(shades[ind+1])
		else:
			sh.append(shades[len(shades)-1])
		if l > 0:
			sh.append(mx[-1][c])
		n = choice(sh)
		t.append(n)
		pr = n
		c += 1
	l += 1
	mx.append(t)

for line in mx:
	print("".join(line))

print()

"""
for team in [ele for ind, ele in enumerate(shades,1) if ele not in shades[ind:]]:
    print("{} {}%".format(team,round(shades.count(team)/len(shades)*100)))

pr = choice(shades)
for line in range(0,20):
	text = ""
	for column in range(0,20):
		text += choice(shades)
	print(text)
"""
