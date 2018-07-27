# https://www.hackerrank.com/challenges/saveprincess2

def nextMove(lr, ud):
    if ud > 0:
        return 'DOWN'
    if ud < 0:
        return 'UP'
    if lr > 0:
        return 'RIGHT'
    if lr < 0:
        return 'LEFT'

def search_princess(n, grid):
   for i in range(0, n): 
        pos = grid[i].find('p')
        if pos != -1:
            return (i, pos)

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input().strip())


m = (r,c)
p = search_princess(n, grid)

# print(m)
# print(p)


ud = p[0] - m[0]
lr = p[1] - m[1]

# print(lr)
# print(ud)

print(nextMove(lr, ud))