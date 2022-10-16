n = int(input())
states = []
for i in range(n):
    states.append(input().split())
it = int(input())
start = it
tape = [0]
index = 0
state = 1
command = ''

while it > 0:
    if tape[index] == 0:
        command = states[state-1][0]
    else:
        command = states[state-1][1]
    tape[index] = int(command[0])
    if command[1] == 'R':
        if index+1 >= len(tape):
            tape.append(0)
        index += 1
    else:
        if index-1 < 0:
            tape.insert(0, 0)
        else:
            index -= 1
    it -= 1
    state = int(command[2])
    if state == 0:
        break

result = ''
for i in range(0, 7):
    if index-3+i >= 0 and index-3+i < len(tape):
        result += str(tape[index-3+i])
    else:
        result += '0'
print(result)
print(start-it)