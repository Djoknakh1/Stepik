import re
Hello again !!
one more text
sdasdas
def rotate(param):
    if param == "left":
        return (-1, 0)
    if param == "right":
        return\
            (1, 0)
    if param == "up":
        return (0, 1)
    if param == "down":
        return (0, -1)

def execute(code):
    my_map = list()
    n,m = 20,20
    my_map = [[" "] * m for _ in range(n)]

    current_position_x= 0
    current_position_y= 0
    delta_x = 0
    delta_y = 1
    counter = 0
    for elem in range(len(code)):
        if code[elem] == "F":
            current_position_x += delta_x
            current_position_y += delta_y
            my_map[0+current_position_x][7+current_position_y] = "*"

        if code[elem] == "L":
            counter += 1
            if counter == 1:
                turn = "left"
            if counter == 2:
                turn = "down"
            if counter == 3:
                turn = "right"
            if counter == 4:
                turn = "up"
                counter = 0
            delta_x, delta_y = rotate(turn)
        if code[elem] == "R":
            counter += 1
            if counter == 1:
                turn = "left"
            if counter == 2:
                turn = "up"
            if counter == 3:
                turn = "right"
            if counter == 4:
                turn = "down"
                counter = 0
            delta_x, delta_y = rotate(turn)

    for row in my_map:
        print(' '.join(list(map(str, row))))



execute("LFFFFFFRFFFRFFFRFFFFFFF")
string = "LF15RF3RF3RF7"
match = re.compile(r"([FRL])(\d+)?")
results = re.findall(match,string)
new_string = ""
for result in results:
    if result[1] != "":
        for i in range(int(result[1])):
            new_string+= result[0]
    else:
        new_string += result[0]
execute(new_string)