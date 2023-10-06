from msvcrt import getwch # to get a single character from the terminal
import os # a module to perform operations in console
import random

list1 = [["    ", "   2", "    ", "    "], ["    ", "    ", "    ", "    "], ["    ", "    ", "    ", "    "], ["    ", "    ", "    ", "    "]]
command = ""
valid_command = True


def draw():
    os.system("cls")
    
    print("\t\t\t\t\t\t\t\t This is 2048")
    print ("\t\t\t\t\t\t\t\t   Welcome")
    print("\n\n\n\n\n\n\n\n")

    # main printing statements
    print ("\t\t\t\t\t\t\t -----------------------------")
    for i in list1:
        print("\t\t\t\t\t\t\t | ", end = "")
        for j in i:
            print(j, end = " | ")
        print()
        print ("\t\t\t\t\t\t\t -----------------------------")
    
    print("\n\n\n")


def input_value():
    print("Commands: \nA --> LEFT \nD --> RIGHT \nW --> UP \nS --> DOWN")
    x = getwch()
    global command
    command = x.upper()
    
    if (command != "A" and command != "W" and command != "S" and command != "D"):
        print("Invalid command. Please try again.", command)
        input_value()


# to arrange the elements according to the commands
"""
    if game is in format:
        2  -  -  -
        -  2  -  2
        4  -  -  -
        -  -  -  -

    if command is D,
    then logic1() returns:
        -  -  -  2
        -  -  2  2
        -  -  -  4
        -  -  -  -   
    
"""
def logic1():
    global valid_command
    valid_command = False
    
    if command == "W":
        for j in range (0,4):
            to_be_filled = 0
            for i in range (0,4):
                if (list1[i][j] != "    "):
                    if (to_be_filled != i):
                        list1[to_be_filled][j] = list1[i][j]
                        list1[i][j] = "    "
                        valid_command = True
                    to_be_filled += 1
    
    elif command == "S":
        for j in range (0, 4):
            to_be_filled = 3
            for i in range (3, -1, -1):
                if (list1[i][j] != "    "):
                    if (to_be_filled != i):
                        list1[to_be_filled][j] = list1[i][j]
                        list1[i][j] = "    "
                        valid_command = True
                    to_be_filled -= 1
                    
    elif command == "A":
        for i in range (0,4):
            to_be_filled = 0
            for j in range (0,4):
                if (list1[i][j] != "    "):
                    if (to_be_filled != j):
                        list1[i][to_be_filled] = list1[i][j]
                        list1[i][j] = "    "
                        valid_command = True
                    to_be_filled += 1
    
    elif command == "D":
        for i in range (0, 4):
            to_be_filled = 3
            for j in range (3, -1, -1):
                if (list1[i][j] != "    "):
                    if (to_be_filled != j):
                        list1[i][to_be_filled] = list1[i][j]
                        list1[i][j] = "    "
                        valid_command = True
                    to_be_filled -= 1

    
def add_operation(i,j):
    global valid_command
    valid_command = True

    if ((int(list1[i][j].lstrip()) * 2) // 10 == 0):
        list1[i][j] = "   " + str(int(list1[i][j].lstrip()) * 2)
    elif ((int(list1[i][j].lstrip()) * 2) // 100 == 0):
        list1[i][j] = "  " + str(int(list1[i][j].lstrip()) * 2)
    elif ((int(list1[i][j].lstrip()) * 2) // 1000 == 0):
        list1[i][j] = " " + str(int(list1[i][j].lstrip()) * 2)
    else:
        list1[i][j] = str(int(list1[i][j].lstrip()) * 2)


# to perform the addition operation
"""
    if logic1() returns:
        -  -  2  4
        -  2  2  2
        2  4  4  2
        -  -  4  8

    if command is D,
    then logic2() returns:
        -  -  2  4
        -  2  -  4
        2  -  8  2
        -  -  4  8   
    
"""
def logic2():
    if command == "A":
        for i in range (0,4):
            for j in range (0,3):
                if (list1[i][j] == list1[i][j + 1] != "    "):
                    list1[i][j + 1] = "    "
                    add_operation(i,j)
    
    elif command == "D":
        for i in range (0,4):
            for j in range (3, 0, -1):
                if (list1[i][j] == list1[i][j - 1] != "    "):
                    list1[i][j - 1] = "    "
                    add_operation(i,j)
    
    elif command == "W":
        for j in range (0,4):
            for i in range (0,3):
                if (list1[i][j] == list1[i + 1][j] != "    "):
                    list1[i + 1][j] = "    "
                    add_operation(i,j)
    
    elif command == "S":
        for j in range (0,4):
            for i in range (3,0,-1):
                if (list1[i][j] == list1[i - 1][j] != "    "):
                    list1[i - 1][j] = "    "
                    add_operation(i,j)


# to add a randomly placed element
def logic3():
    count = 0
    number = random.randint(1,16)
    
    while True:
        for i in range (0,4):
            for j in range(0,4):
                if list1[i][j] == "    ":
                    count += 1
                if count == number:
                    list1[i][j] = "   2"
                    break
            if count == number:
                break
        if count == number:
            break


"""
The game is over when we have the matrix fully filled and when we perform any of the A,S,D,W operation, we cannot empty any space for the randomly placed element.

for example in a condition lke this:

    2  4  2  8
    4  8  4  16
    2  4  8  2
    8  2  4  8

we do not have any two consecutive elements same in any row or column, so when we do any operation A,S,D,W , we cannot empty any space 
and the game is stuck in this condition. In this condition , game ends.
"""
def game_over():
    can_logic2 = False
    fully_filled = True
    gameOver = False
    
    for i in range(0,4):
        for j in range(0,4):
            if (list1[i][j] == "    "):
                fully_filled = False
                break
        if (not fully_filled):
            break
    
    if fully_filled:
        for i in range(0,4):
            for j in range (0,3):
                if (list1[i][j] == list1[i][j + 1] or list1[j][i] == list1[j + 1][i]):
                    can_logic2 = True
                    break
            if (can_logic2):
                break
    
    if (not can_logic2 and fully_filled):
        gameOver = True
    
    return gameOver


def win():
    for i in range(0,4):
        for j in range(0,4):
            if(list1[i][j] == "2048"):
                return True
    return False


while True:
    draw()
    
    if (game_over()):
        print ("\t\t\t\t\t***************************Game Over******************************")
        break

    if (win()):
        print ("\t\t\t\t\t************************!!!You won it!!!**************************\n")
        print ("\t\t\t\t\t***************************Game Over******************************")
        break
    
    input_value()
    logic1()
    logic2()
    
    if(not valid_command):
        continue
    
    logic1()
    logic3()



#**************************************************************************************************************************************************
#**************************************************************************************************************************************************
"""
The valid_command in this checks if there is any change in the matrix due to logic1() or logic2() when we input a command.
If there is no change in the matrix, we do not consider that command as valid. And take the command again.
"""


"""
Example of the operations performed in logic1()

1   if command == "W":
2       for j in range (0,4):
3           to_be_filled = 0
4           for i in range (0,4):
5               if (list1[i][j] != "    "):
6                   if (to_be_filled != i):
7                       list1[to_be_filled][j] = list1[i][j]
8                       list1[i][j] = "    "
9                       valid_command = True
10                  to_be_filled += 1

    
in this if we have the matrix as:
    2  -  4  -
    -  4  4  2
    2  -  -  4
    8  8  -  4

what we want is:
    2  4  4  2
    2  8  4  4
    8  -  -  4
    -  -  -  -

In this, what we do is we take the elements by column, and then we arrange them  --> statament 2
then we check which position is to be filled by us in the column, we set that for each column the starting value as 0 --> statement 3
then we initiate a loop in the column to check perform the operations --> statement 4
then we check if the element obtained this way is not a blank space, so that we can ckeck if we have to displace the element upwards or keep the element in same place --> statement 5
if there is no space above the element,we do nothing. If there is, we displace the element in the to_be_filled position, and make that position as vacant--> statemen 6,7,8
if we can perform this operation, it means that logic1() changes the matrix, hence command is valid --> statement 9
at last, if there is not a blank apace in the position we increment to_be_filled by 1 --> statement 10
"""


"""
In logic2()
    if logic1() returns:
        -  -  2  4
        -  2  2  2
        2  4  4  2
        -  -  4  8

    if command is D,
    then logic2() returns:
        -  -  2  4
        -  2  -  4
        2  -  8  2
        -  -  4  8
        

    elif command == "D":
        for i in range (0,4):
            for j in range (3, 0, -1):
                if (list1[i][j] == list1[i][j - 1] != "    "):
                    list1[i][j - 1] = "    "
    
 ---->              if ((int(list1[i][j].lstrip()) * 2) // 10 == 0):
                        list1[i][j] = "   " + str(int(list1[i][j].lstrip()) * 2)
    
                    elif ((int(list1[i][j].lstrip()) * 2) // 100 == 0):
                        list1[i][j] = "  " + str(int(list1[i][j].lstrip()) * 2)
    
                    elif ((int(list1[i][j].lstrip()) * 2) // 1000 == 0):
                        list1[i][j] = " " + str(int(list1[i][j].lstrip()) * 2)
    
                    else:
                        list1[i][j] = str(int(list1[i][j].lstrip()) * 2)
    
                    valid_command = True


we check if the consecutive elements in a row are same and not equal to "    ".
then we replace the element in i,j+1 position by a blank apace and the element in i,j position by double of the previous value in the commands starting from ---->

if we can perform this operatoin we set the command as valid
"""



"""
In this we had to define global values in functions because in python, we cannot change the global values globally, if we do not do this. But we can use that global value.
"""