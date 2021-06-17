
#!/usr/bin/python
import random

# Head ends here

def next_move(bot, board):
	borders = []
	for row_n, row in enumerate(board):
		for col_n, cell in enumerate(row):
			# if cell == "e":
			# 	if row_n == 0:
			# 		return "UP"
			# 	if row_n == 1 and col_n == 0:
			# 		return "LEFT"
			# 	if row_n == 1 and col_n == 2:
			# 		return "RIGHT"
			# 	if row_n == 2:
			# 		return "DOWN"
			if cell == "#":
				borders.append((row_n, col_n, "#"))
			if cell == "e":
				borders.append((row_n, col_n, 'e'))
	# print(borders)
	choices = ["LEFT", "RIGHT", "UP", "DOWN",]
	if (0, 1, "#") in borders:
		choices.remove("UP")
	if (1, 0, "#") in borders:
		choices.remove("LEFT")
	if (1, 2, "#") in borders:
		choices.remove("RIGHT")
	if (2, 2, "#") in borders:
		choices.remove("DOWN")
	e_pos = [(r,c) for (r, c, t)  in borders if t == "e" and (r,c) in [(0, 1), (1, 0), (1, 2), (2, 2)]]
	if e_pos != []:
		if e_pos[0] == (0,1):
			return "UP"
		if e_pos[0] == (1,0):
			return "LEFT"
		if e_pos[0] == (1,2):
			return "RIGHT"
		if e_pos[0] == (2,2):
			return "DOWN"
	if ["LEFT", "DOWN"] == choices:
		return "LEFT"
	if ["RIGHT", "DOWN"] == choices:
		return "RIGHT"
	if ["RIGHT", "LEFT", "DOWN"] == choices:
		return "RIGHT"
	if "UP" in choices:
		return "UP"
	if "RIGHT" in choices:
		return "RIGHT"
	if "LEFT" in choices:
		return "LEFT"

	return random.choice(choices)
	return choices[0]
	

	# return "DOWN"
	# print(bot)



# Tail starts here

if __name__ == "__main__":
    bot = int(input().strip())
    board = [[j for j in input().strip()] for i in range(3)]
    print(next_move(bot, board))