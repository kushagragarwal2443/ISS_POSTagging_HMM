import random

num = [0,2,3,6]
for i in range(0,4):
	for j in range(0,7):
		n = random.choice(num)
		print(round(n/6,2),end=" ")
	print()

print()

for i in range(0,5):
	for j in range(0,5):
		n = random.choice(num)
		print(round(n/6,2),end=" ")
	print()
