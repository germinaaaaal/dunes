#smooth terrain generator

from random import *
#hello
#shades = ["█","▓","▒","░"," "]
shades = ["█"," "]

class Point():
	def __init__(self, x, y, state, north, south, west, east):
		self.x = x
		self.y = y
		self.state = state
		self.north = north
		self.south = south
		self.west = west
		self.east = east
		self.surroundings = [north, south, west, east]
	def __repr__(self):
		return("row %i, column %i\n %s\n%s%s%s\n %s\n" % (self.x, self.y, self.north, self.west, self.state, self.east, self.south))
	def coef(self):
		c = 0
		for cell in self.surroundings:
			if cell == self.state:
				c += 1
		return c

class Matrix(list):
	def display(self):
		for line in self:
			print("".join(line))

def matrix(x=15, y=27):
	matrix = []
	pr = choice(shades)
	l = 0
	for line in range(0,x):
		text = ""
		t = []
		c = 0
		for column in range(0,y):
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
				sh.append(matrix[-1][c])
			n = choice(sh)
			t.append(n)
			pr = n
			c += 1
		#print(text)
		l += 1
		matrix.append(t)
		#print(matrix)
	return(matrix)


"""
matrix = gen()

for line in matrix:
	print("".join(line))

print()


[
[x0y0,x0y1,x0y2]
[x1y0,x1y1,x1y2]
[x2y0,x2y1,x2y2]
]

   0 1 2 3 4 y
0 [_|_|_|_|_]
1 [_|_|_|_|_]
2 [_|_|_|_|_]
3 [_|_|_|_|_]
4 [ | | | | ]
x
"""

def get_surroundings(x, y, matrix):
	#provide coordinates of center with top left origin
	rows = len(matrix)-1
	#print(rows)
	columns = len(matrix[0])-1
	#print(columns)
	center = matrix[x][y]
	#nswe
	if x == 0:
		north = center
		south = matrix[x+1][y]
	elif x == rows:
		north = matrix[x-1][y]
		south = center
	else:
		north = matrix[x-1][y]
		south = matrix[x+1][y]
	if y == 0:
		west = center
		east = matrix[x][y+1]
	elif y == columns:
		west = matrix[x][y-1]
		east = center
	else:
		west = matrix[x][y-1]
		east = matrix[x][y+1]
	return Point(x, y, center, north, south, west, east)

def smooth(matrix, shade=False, advanced=False):
	allsh = ["█","▓","▒","░"," "]
	next = []
	x = 0
	for line in matrix:
		nline = []
		row = matrix.index(line)
		#print("ROW", x)
		y = 0
		for point in line:
			#print(y)
			point = get_surroundings(x, y, matrix)
			n = point.coef()
			if advanced:
				c = 0
				for cell in point.surroundings:
					if cell == "░":
						c += 1
				val = allsh[c]
			else:
				if n < 2:
					val = shades[(shades.index(point.state)+1)%2]
				elif n == 2 and shade:
					val = "▒"
				else:
					val = point.state
				#print("\n point:%s, surroundings: n%s, e%s, s%s, w%s, n:%i. next phase:%s" % (point, surroundings[0], surroundings[1], surroundings[2], surroundings[3], n, val))
			nline.append(val)
			y += 1
		next.append(nline)
		x += 1
	"""
	for line in next:
		print("".join(line))
	"""

	return next

def main():
	n = ""
	pr = "n"
	x = 5
	y = 9
	m = Matrix(matrix())
	while n != "q":
		n = input("> ")
		if not n:
			n = pr
		if "n" in n:
			xy = (input("x-y> ") or "15x27").split("x")
			x = int(xy[0])
			y = int(xy[1])
			m = Matrix(matrix(x, y))
			m.display()
		elif "p" in n:
			m = Matrix(smooth(m))
			m.display()
		elif "s" in n:
			m = Matrix(smooth(m, shade=True))
			m.display()
		elif "c" in n:
			Matrix(smooth(m, shade=True)).display()
			print("\n")
			Matrix(smooth(m, advanced=True)).display()
		pr = n

if __name__ == '__main__':
	main()

"""
▒   ▒   █  ░░ ░    ▒ ░░  ░░░█ ░▒▒ ▒░
░ ░  ░░    ▒   ▒▒░░ ▓▒▒ ░  ▒  ░  ▓▓
   █ ▒    ░    ░ ░█▒░  ▒   ▒ ░ ░█ ░▒
  ░▓▒░▒░░ ░▒▒░░ ░ ░ ▓ ░░▒░█▒░ ░▒   ░
▒ ▒░ ░░ ░░ ░ ▒░█  ▒ ░░   ▒ ░░█ ░░▓▒░
▓░ █ ▒░░░░░ ▓░▒▒  ░░ ░░░ ░     ░▒░▒
▒░░▒  ░░▒▒ ▓░  █ ░ ▓▒░   ▒  ▒▒░░  ░▓
 ▒░░░░░▓▒█░█▒▒▒▒▓░▒▒▓░░ █▒ ▒░ ▒ ░▒▒▒
 ▒▒░ ▒ ▒▒    ▒ ░░▒  ▒░▒█▒ ▒▒▒ ░█ ▒▒
▒ ▓▒░█ ░ ░░█▒░▓▒░░ ▒░▒░░░▓ ░▒  ▒ ▓▒
  ░ ▓ ░░█ ░▒ ░░▒ ░ ░▒  ▒   ░░ ░  ░
▓ ░   ░▓▓▒   ░██░▓ ▒   ░░░░   ░▒ ░░
▓ ░ █▒░ ░█ ▒▓  ▒▒░  ░░░ ▒▒██ █▒ █ ▒░
 ░░░░██   ░░░ ░ ▓░▓ ▓░░ █░▒█ █▒▒ ▒▓▒
 ░   ░▒░ ▒░ ░ ░▒█  ░ ░░  ▒▒░▒░ ░ ░▒░
▒░ ▓ █ ▒  █  ░ ░▓░░ █▓▓▓▓▒▒▒ ▒▒ ░░░▓
█ ░▒ ░░░▒▒   ▒░░█▓▒░▓░▒▓    ░░█ ▓  ░
  █░░ ▒░  ▒ ░░░ ▓   ░█ ░▒▓▒ ▒ ░ ░▓█
 ░░░▒▓░  ▓░ ░▒▒ ▒ █ ░▓▒▓  █▓░▒  ░▓ ▒
▒▒   ░ ░░░░ ▓ ▓▒ ▒▒ ░█    ▒░░▒▒░ ▓░
"""
