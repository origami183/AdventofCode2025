file = 'day1_input.txt'

zeros = 0
dial_value = 50
dial_min = 0
dial_max = 99

with open(file) as f:
    for line in f:
        text = line.strip
        direction = line[0]
        move = int(line[1:])
        for _ in range(move):
            if direction == 'R':
                dial_value += 1
                if dial_value > dial_max:
                    dial_value = 0
                if dial_value == 0:
                    zeros += 1
            else:
                dial_value -= 1
                if dial_value == 0:
                    zeros += 1
                if dial_value < dial_min:
                    dial_value = 99

print(zeros)