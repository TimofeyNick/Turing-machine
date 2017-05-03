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

__author__ = 'student'

fail_name_input = 'input_data'
N = 10
number_iterations = 1

Field = [[0]*(N + 2) for i in range(N + 2)]
with open(fail_name_input, 'r') as f:
    for line in f:
        x,y = map(int, line.rstrip().split())
        Field[x][y] = 1

def check_neighboor(x, y): # 1 - если жизнь зарождается, 2 - жизнь продолжается, 0 - умирает
    answer = 0
    i = 0
    if Field[x-1][y-1] == 1: i += 1
    if Field[x][y-1] == 1: i += 1
    if Field[x+1][y-1] == 1: i += 1
    if Field[x-1][y] == 1: i += 1
    if Field[x+1][y] == 1: i += 1
    if Field[x-1][y+1] == 1: i += 1
    if Field[x][y+1] == 1: i += 1
    if Field[x+1][y+1] == 1: i += 1
    if i == 3: # жизнь зарождается 1
        answer = 1
    if i == 2:
        answer = 2
    return answer

def iterations(number_iterations):
    print_Fild(Field)
    print()
    for i in range(number_iterations):
        Field1 = Field[:]
        for x in range(1,N + 1):
            for y in range(1, N + 1):
                answer = check_neighboor(x, y)
                if answer == 1:
                    Field[x][y] = 1
                if answer == 0:
                    Field[x][y] = 0
        print_Fild(Field)
        print()
        if ending(Field, Field1):
            return


def print_Fild(Field):
    for elem in Field:
        print(' '.join(map(str, elem)))

def ending(Field, Field1):
    return (deathing_and_stable(Field, Field1))

def deathing_and_stable(Field, Field1):
    ans1 = True
    ans2 = True
    for x in range(1,N + 1):
        for y in range(1, N + 1):
            if Field[x][y]== 1:
                ans1 = False
            if Field[x][y] != Field1[x][y]:
                ans2 = False
    if ans1 or ans2:
        return True
    else:
        return False

iterations(100)

__author__ = 'student'

fail_name_input = 'input_data_Wolfram'

input = open(fail_name_input, 'r')
number = input.read()
number = int(number)
input.close()
num_bin = bin(number)

states = [0 for i in range(8)]
number = list(str(num_bin))
number = number[2:]

i = 8 - len(number)
for elem in number:
    states[i] = int(elem)
    i += 1

N = 35

def generate_field():
    field = [0]*N
    x = N//2
    field[x] = 1
    return field

def cell_calculate(left, current, right, G):
    return G[left][current][right]

def calculate_field(field):
    """field -- список из N ноликов или единичек"""
    G = {1:{1:{1:states[0], 0:states[1]}, 0:{1:states[2], 0:states[3]}}, 0:{1:{1:states[4], 0:states[5]}, 0:{1:states[6], 0:states[7]}}}
    new_field = [0]*N
    for i in range(1, N-1):
        new_field[i] = cell_calculate(field[i-1], field[i], field[i+1], G)
    new_field[0] = cell_calculate(field[-1], field[0], field[1], G)
    new_field[N-1] = cell_calculate(field[N-2], field[N-1], field[0], G)
    field[:] = new_field

def print_field(field):
    for cell in field:
        if cell == 1 :
            print('★', end = '')
        else:
            print(' ', end = '')
    print()

field = generate_field()
print_field(field)
for t in range(15):
    calculate_field(field)
    print_field(field)

