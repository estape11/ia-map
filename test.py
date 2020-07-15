def h(dist, calle, peligrosidad):
	return dist * ( (dist/400)/4 + 2*(peligrosidad/5)/4 - (calle/10)/4)

def h2(dist, calle, peligrosidad):
	return dist * ( 2*(peligrosidad/5)/3 - (calle/10)/3)

print(h(300, 6, 2))
print(h(300, 6, 5))
print(h(151, 8, 5))
print(h(151, 8, 3))

print(h2(300, 6, 2))
print(h2(300, 6, 5))
print(h2(151, 8, 5))
print(h2(151, 8, 3))