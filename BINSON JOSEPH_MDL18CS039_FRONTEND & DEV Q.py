import random
import sys

def ran_generator():    #Generates the random number(2 or 4) to be inserted in the random index
    x = random.randint(0,3)
    y = random.randint(0,3)
    t = random.randint(1,2)
    if a[x][y] != 0:    #Checks if the position is already filled
        ran_generator() #If already filled, generates calls the function again 
    else:
        a[x][y] = 2 * t #Assigns the position with the generated random number(2 or 4)


def key_1():
    for i in range(4):
        k = a[i][3]  #k is initialised to the last no. in a row
        for j in range(2,-1,-1):
            if a[i][j] == k:    #Compares the previous no. in the row with k
                a[i][j] += a[i][j + 1]  #if found equal, add the two no.s
                k = 0   
                a[i][j + 1] = 0 #make the next number as 0 
            
            elif a[i][j] == 0:  #Checks if the current no. in the cell is 0
                a[i][j] = a[i][j + 1] #If so, initialise the current cell with next cell 
                a[i][j + 1] = 0 #make the next number as 0

            else:
                k = a[i][j] #Else initialise k with the current cell number

        c = a[i].count(0)   #Function to count no. of zeroes
        w = c
        while c != 0:
            a[i].remove(0)  # remove all zeroes
            c -= 1 
        while w != 0:
            a[i].append(0)  #Append removed zeroes to the right
            w -= 1


def key_2():
    for i in range(4):
        k = a[i][0] #k is initialised to the first no. in a row
        for j in range(1,4):
            if a[i][j] == k:    #Compares the next no. in the row with k
                a[i][j] += a[i][j - 1]  #if found equal, add the two no.s
                k = 0
                a[i][j - 1] = 0 #make the previous number as 0 
            
            elif a[i][j] == 0:  #Checks if the current no. in the cell is 0
                a[i][j] = a[i][j - 1] #If so, initialise the current cell with previous cell
                a[i][j - 1] = 0 #make the previous number as 0

            else:
                k = a[i][j] #Else initialise k with the current cell number

        c = a[i].count(0)   #Function to count no. of zeroes
        w = c
        while c != 0:
            a[i].remove(0)  # remove all zeroes
            c -= 1 
        while w != 0:
            a[i].insert(0,0)    #Append removed zeroes to the left
            w -= 1


def transposmat():  #Finds transpose of the matrix
    b = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            b[i][j] = a[j][i]

    return b    #returns the transpose matrix


def printm():   #Function to print matrix after each move
    r = 0
    q = 0
    g = 0
    w = 2048
    print("\n")
    for i in range(4):
        print(a[i]) #Prints each row
        if g in a[i]:
            q = 1
        if w in a[i]:
            r = 1 
    print("\n")
    if q == 0:
        print("You Lost. Game Over!") #Prints this if no more empty space in the grid
        sys.exit()  #Exits program
    if r == 1:
        print("Congratulations!!! You won the Game.")   #If any cell contains 2048 as a value prints this message
        sys.exit()  #Exits program


a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
ran_generator() #Generates first random number(2 or 4)
ran_generator() #Generates second random number(2 or 4)
printm()

while True:

    s = int(input("Enter key : Left - 1, Right - 2, Up - 3, Down - 4  :  "))    #Prints move options

    if s == 1:  #Makes Left move
        print("\nLeft")
        key_1()
        ran_generator() #Generates next random number(2 or 4)
        printm()

    elif s == 2:    #Makes Right move
        print("\nRight")
        key_2()
        ran_generator() #Generates next random number(2 or 4)
        printm()

    elif s == 3:    #Makes Up move
        print("\nUp")
        a = transposmat()
        key_1()
        a = transposmat()
        ran_generator() #Generates next random number(2 or 4)
        printm()

    elif s == 4:    #Makes Down move
        print("\nDown")
        a = transposmat()
        key_2()
        a = transposmat()
        ran_generator() #Generates next random number(2 or 4)
        printm()

    else:
        print("Inalid Key!")
        print("Game Over!!!")
        break