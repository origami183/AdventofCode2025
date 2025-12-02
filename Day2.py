file = 'day2_input.txt'
# file = 'temp.txt'

def part1():
    sum = 0
    with open(file) as f:
        ranges = f.read().split(",")
        for chunk in ranges:
            ends = chunk.split("-")
            front = int(ends[0])
            back = int(ends[1])
            for i in range(front, back+1):
                value = str(i)
                length = len(value)
                if length % 2 == 1:
                    continue
                divide = length // 2
                halfA = value[0:divide]
                halfB = value[divide:]
                if halfA == halfB:
                    sum += i
    print(sum)

def part2():
    sum = 0
    with open(file) as f:
        ranges = f.read().split(",")
        for chunk in ranges:
            ends = chunk.split("-")
            front = int(ends[0])
            back = int(ends[1])
            for i in range(front, back+1):
                value = str(i)
                digits = list(value)
                n = len(digits)
                found = False
                for window in range(1, n//2+1):
                    if found:
                        break
                    temp = ""
                    pattern = value[:window]
                    repeat = n//window
                    for _ in range(repeat):
                        temp += pattern
                    if temp == value:
                        sum += i
                        found = True
                        continue      
    print(sum)

# part1()
part2()