filename = 'puzzle_one.txt'
with open(filename) as f:
	data = f.readlines()

for counter in range(len(data)):
	data[counter] = int(data[counter].rstrip('\n'))

# First solutions to day1
	
pair = [] 
for number in data:
	remainder = 2020 - number
	if remainder in data:
		pair.append(number)
		pair.append(remainder)
print(pair[0] * pair[1])

triple = []
for counter in range(len(data)):
	remainder = 2020 - data[counter]
	for counter2 in range(len(data)):
		if counter2 == counter:
			continue
		else:
			remainder2 = remainder - data[counter2]
			if remainder2 in data:
				triple.append(data[counter])
				triple.append(data[counter2])
				triple.append(remainder2)
print(triple[0] * triple[1] * triple[2])

## Better solution to part one

def part_1(data: list) -> int:
	for number in data:
		if (2020-number) in data:
			return (2020-number) * number

def part_2(data: list) -> int:
	for number1 in data:
		for number2 in data:
			if (2020 - number2 - number1) in data:
				return (2020 - number2 - number1) * number1 * number2

answer1 = part_1(data)
answer2 = part_2(data)

print(f'The answer to part 1 is {answer1}.')
print(f'The answer to part 2 is {answer2}.')
