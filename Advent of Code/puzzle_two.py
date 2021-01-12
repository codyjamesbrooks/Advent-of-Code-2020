filename = 'puzzle_two.txt'
with open(filename) as f:
	data = f.readlines()

for counter in range(len(data)):
	data[counter] = data[counter].rstrip('\n')

valid_passwords = 0

for item in data: 
	left_range = int(item.split(' ')[0].split('-')[0]) 
	right_range = int(item.split(' ')[0].split('-')[1])
	char = item.split(' ')[1][0]
	password = item.split(' ')[2]
	count = 0

	for letter in password:
		if letter == char:
			count +=1

	if count >= left_range and count <= right_range:
		valid_passwords += 1
print(valid_passwords)

valid_passwords = 0

for item in data: 
	left_index = int(item.split(' ')[0].split('-')[0]) - 1 
	right_index = int(item.split(' ')[0].split('-')[1]) - 1
	char = item.split(' ')[1][0]
	password = item.split(' ')[2]
	count = 0

	if password[left_index] == char:
		count += 1
	if password[right_index] == char:
		count += 1


	if count == 1:
		valid_passwords += 1
print(valid_passwords)


# Second attempt at Day two. Goal is cleaner code

def part_1(data: list) -> int:
	good_pass = 0
	for pswd in data:
		count = 0
		char = pswd.split(' ')[1][0]
		min_char = int(pswd.split(' ')[0].split('-')[0])
		max_char = int(pswd.split(' ')[0].split('-')[1])
		for letter in pswd.split(' ')[2]:
			if letter == char:
				count += 1
		if min_char <= count <= max_char:
			good_pass += 1
	return good_pass

def part_2(data: list) -> int:
	good_pass = 0
	for pswd in data:
		char = pswd.split(' ')[1][0]
		left_index = int(pswd.split(' ')[0].split('-')[0]) - 1
		right_index = int(pswd.split(' ')[0].split('-')[1]) - 1
		password = pswd.split(' ')[2]
		if password[left_index] == char and password[right_index] == char:
			continue
		elif password[left_index] == char or password[right_index] == char:
			good_pass += 1
	return good_pass

print(f'The answer to part 1 is {part_1(data)}.')
print(f'The answer to part 2 is {part_2(data)}.')


