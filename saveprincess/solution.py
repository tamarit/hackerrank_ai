# https://www.hackerrank.com/challenges/saveprincess

def displayPathtoPrincess(lr, ud):
#print all the moves here
    if lr < 0:
        for i in range(0, abs(lr)):
            print('RIGHT') 
    if lr > 0:
        for i in range(0, lr):
            print('LEFT')
    if ud < 0:
        for i in range(0, abs(ud)):
            print('DOWN')
    if ud > 0:
        for i in range(0, ud):
            print('UP')

def search_princess(n, grid): 
    if grid[0].startswith('p'):
        return (0, 0)
    if grid[0].endswith('p'):
        return (0, n - 1)
    if grid[n - 1].startswith('p'):
        return (n - 1, 0)
    if grid[n - 1].endswith('p'):
        return (n - 1, n - 1)

def search_mario(n, grid):
   for i in range(0, n): 
        pos = grid[i].find('m')
        if pos != -1:
            return (i, pos)
    

n = int(input())
grid = [] 
for i in range(0, n): 
    grid.append(input().strip())

p = search_princess(n, grid)
m = search_mario(n, grid)


lr = p[0] - m[0]
ud = p[1] - m[1]


displayPathtoPrincess(lr, ud)