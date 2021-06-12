
#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
	# min_dist = 1000
	min_dist_info = None
	for row_num, row in enumerate(board):
		for col_num, cell in enumerate(row):
			if cell == 'd':
				row_dist = posr - row_num
				col_dist = posc - col_num
				# dist = abs(row_dist) + abs(col_dist)
				# print((row_num, col_num, dist ))
				# if dist < min_dist:
					# print(f"MIN: {(row_num, col_num)}")
					# min_dist = dist
				min_dist_info = (row_num, col_num, row_dist, col_dist)
	# print(min_dist_info)
	if min_dist_info is None:
		return
	if min_dist_info[2] == 0 and min_dist_info[3] == 0:
		print("CLEAN")
	elif min_dist_info[2] == 0 and min_dist_info[3] < 0:
		print("RIGHT")
	elif min_dist_info[2] == 0 and min_dist_info[3] > 0:
		print("LEFT")
	elif min_dist_info[2] < 0:
		print("DOWN")
	elif min_dist_info[2] > 0:
		print("UP")
    # print("")

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)