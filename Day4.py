file = 'day4_input.txt'
# file = 'temp.txt'

def makeGrid():
    grid = []
    with open(file) as f:
        for line in f:
            short = line.strip()
            row = []
            for i in range(len(short)):
                row.append(line[i:i+1])
            grid.append(row)
    return grid


def part1():
    grid = makeGrid()
    rowLen = len(grid[0])
    colLen = len(grid)
    sum = 0
    adjacent = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for r in range(colLen):
        for c in range(rowLen):
            if grid[r][c] != '@':
                continue

            check = 0
            for ar,ac in adjacent:
                tr,tc = r+ar, c+ac

                if 0 <= tr < colLen and 0 <= tc < rowLen:
                    if grid[tr][tc] == '@':
                        check += 1

            if check < 4:
                sum +=1
    print(sum)

def part2():
    grid = makeGrid()
    rowLen = len(grid[0])
    colLen = len(grid)
    totalRemoved = 0
    adjacent = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    lastRemoved = -1
    roundRemove = 0
    round = 0
    while roundRemove != lastRemoved:
        for r in range(colLen):
            for c in range(rowLen):
                if grid[r][c] != '@':
                    continue

                check = 0
                for ar,ac in adjacent:
                    tr,tc = r+ar, c+ac

                    if 0 <= tr < colLen and 0 <= tc < rowLen:
                        if grid[tr][tc] == '@':
                            check += 1

                if check < 4:
                    totalRemoved +=1
                    roundRemove += 1
                    grid[r][c] = "."
        lastRemoved = roundRemove
        roundRemove = 0
        round +=1
    print(totalRemoved)

part1()
part2()