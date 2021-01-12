filename = 'puzzle_three.txt'
with open(filename) as f:
	data = f.readlines()

for counter in range(len(data)):
	data[counter] = data[counter].rstrip('\n')

tree_counter = 0
the_hill = data
right_mvt = 3
down_mvt = 1

x_pos = 0
y_pos = 0


while y_pos < len(the_hill):
	if the_hill[y_pos][x_pos] == '#':
		tree_counter += 1 
	x_pos += right_mvt
	y_pos += down_mvt
	if x_pos >= 31:
		x_pos = x_pos - 31

print(tree_counter)



right_mvts = [1, 3, 5, 7, 1]
down_mvts = [1, 1, 1, 1, 2]
tree_counters = []
for counter in range(len(right_mvts)):
	tree_counter = 0
	x_pos = 0
	y_pos = 0
	while y_pos < len(the_hill):
		if the_hill[y_pos][x_pos] == '#':
			tree_counter += 1
		x_pos += right_mvts[counter]
		y_pos += down_mvts[counter]
		if x_pos >= 31:
			x_pos = x_pos - 31
	tree_counters.append(tree_counter)

print(tree_counters)
answer = 1
for x in tree_counters:
	answer = answer * x
print(answer)