import random
input = ["A", 'C','D','E','B']
copied = input[:]
for i in range(len(copied)):
	index = random.randint(i, len(copied)-1)
	copied[index], copied[i] = copied[i], copied[index]
print copied