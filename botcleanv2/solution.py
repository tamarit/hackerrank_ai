#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
	min_dist = 1000
	min_dist_info = None
	found = False
	if board[posr][posc] == 'd':
		min_dist_info = (posr, posc, 0, 0)
	else:	
		for row_num, row in enumerate(board):
			if found:
				break
			for col_num, cell in enumerate(row):
				if cell == 'd':
					row_dist = posr - row_num
					col_dist = posc - col_num
					dist = abs(row_dist) + abs(col_dist)
					# print((row_num, col_num, dist ))
					if dist < min_dist or row_num == 0 or row_num == 4 or col_num == 0 or col_num == 4:
						# print(f"MIN: {(row_num, col_num)}")
						min_dist_info = (row_num, col_num, row_dist, col_dist)
						if dist < min_dist:
							min_dist = dist
						else:
							found = True
							break		
	# print(min_dist_info)
	# min_dist_info = (0, 0, posr - 4, posc - 4)
	forced = False
	if min_dist_info is None:
		forced = True
		for (row_num, col_num) in [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]:
			row_dist = posr - row_num
			col_dist = posc - col_num
			dist = abs(row_dist) + abs(col_dist)
			# print((row_num, col_num, dist ))
			if dist < min_dist:
				# print(f"MIN: {(row_num, col_num)}")
				min_dist = dist
				min_dist_info = (row_num, col_num, row_dist, col_dist)
	if min_dist_info[2] == 0 and min_dist_info[3] == 0:
		if not forced:
			print("CLEAN")
		else:
			if min_dist_info[0] >= 1 and  min_dist_info[0] < 3 and  min_dist_info[1] == 1:
				print("DOWN")
			elif  min_dist_info[0] == 1:
				print("LEFT")
			elif  min_dist_info[0] == 3 and  min_dist_info[1] < 3:
				print("RIGHT")
			elif  min_dist_info[0] > 1 and  min_dist_info[1] == 3:
				print("UP")
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
