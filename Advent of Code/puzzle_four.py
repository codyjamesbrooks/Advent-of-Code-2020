filename = 'puzzle_four.txt'
with open(filename) as f:
	data = f.readlines()

passports = []
valid_passengers = 0
good_char = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

appender = ""
for item in data:
	string = item
	if string != '\n' and appender != '':
		appender += ' ' + string.rstrip('\n')
	elif string != '\n' and appender == '':
		appender += string.rstrip('\n')
	if string == '\n' or string == data[-1]:
		passports.append(appender)
		appender = ""


for passenger in passports:
	passport_info = []
	info = passenger.split(' ')
	for data_point in info:
		passport_info.append(data_point.split(':')[0])

	flag = True
	for trait in good_char:
		if trait not in passport_info:
			flag = False
	if flag == True:
		valid_passengers += 1

print(valid_passengers)
valid_passengers = 0

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

valid_passports = []

for passenger in passports:
	passport_details = []
	passport_info = []

	info_point = passenger.split(' ')
	for detail in info_point:
		passport_details.append(detail)
	for detail in info_point:
		passport_info.append(detail.split(':'))

	flag = True
	for trait in good_char:
		if trait not in passport_info:
			flag = False
	if flag == True:
		valid_passports.append(passport_details)

for passenger in valid_passports:
	for trait in passenger:
		feature = trait.split(':')[0]
		detail = trail.split(':')[1]

		flag = True
		
		if feature == 'byr':
			if int(detail) <= 1920 or int(detail) >= 2020:
				flag = False
		if feature == 'iyr':
			if int(detail) <= 2010 or int(detail) >= 2020:
				flag = False
		if feature == 'eyr':
			if int(detail) <= 2020 or int(detail) >= 2030:
				flag = False
		if feature == 'hgt':
			number = detail[0:-2]
			unit = detail[-2]
			


	