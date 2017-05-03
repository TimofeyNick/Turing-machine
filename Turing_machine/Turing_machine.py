fail_name_input = 'input_delete.txt'
fail_name_commands = 'delete second elem.txt'

lenta = [' ' for i in range(100)]
input = open(fail_name_input, 'r')
stroka = input.read()
input.close()

i = 1
for elem in stroka:
    lenta[i] = elem
    i +=1

explore = {}
with open(fail_name_commands, 'r') as f:
    for line in f:
        line = list(line.rstrip())
        cur_number = line[2]
        move = line[8]
        if line[7]=='T':
            if len(line)==11:
                move = line[10]
            else:
                move = 'S' #stop
        current_place = line[0]
        write = line[5]
        state = line[7] #number or 'T'
        if cur_number not in explore:
            explore[cur_number] = {current_place : [write, state, move]}
        else:
            explore[cur_number][current_place] = [write, state, move]

place = '1'
state = '1' # the same cur_number
number = lenta[int(place)]
while True:
    A = explore[state][number]
    n_write, n_state, n_move = A[0], A[1], A[2]
    number = lenta[int(place)]
    if number == ' ':
        number = 'B'
    lenta[int(place)] = n_write
    state = n_state
    if state == 'T':
        break
    if n_move == 'R':
        place = str(int(place) + 1)
    if n_move == 'L':
        place = str(int(place) - 1)
    number = lenta[int(place)]
    if number == ' ':
        number = 'B'

K = []
for elem in lenta:
    if elem != ' ':
        if elem == 'B':
            K.append(' ')
        else:
            K.append(elem)

print(''.join(map(str, K)))