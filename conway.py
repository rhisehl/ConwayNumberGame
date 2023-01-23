# Conway's  Game of Life
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells
nextCells = []
for x in range(WIDTH):
    column = [] #create new column
    for y in range(HEIGHT):
        if random.randint(0,1) ==0:
            column.append('#') #add a living cell
        else:
            column.append(' ') #add a dead cell.
    nextCells.append(column) #nextCells is a list of column lists

while True: #main program loop
    print('\n\n\n\n\n') #separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    #print CurrentCells on screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end='') #print the # or space
        print() #print a newline at the end of the row
    #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get neighboring coordinates:
            # `% WIDTH` ensures leftCoord is always between 0 and WIDTH -1
            leftCoord = (x-1) % WIDTH
            rightCoord = (x+1) % WIDTH
            aboveCoord = (y-1) % HEIGHT
            belowCoord = (y+1) % HEIGHT

            #count the number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #top left Neighbor alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #top neighbor is alive
            if currentCells [rightCoord][aboveCoord] == '#':
                numNeighbors +=1 #top right neighbor is alive
            if currentCells [leftCoord][y] == '#':
                numNeighbors +=1 #left neighbor is alive
            if currentCells [rightCoord][y] == '#':
                numNeighbors +=1 #right neighbor is alive
            if currentCells [leftCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom left neighbor is alive
            if currentCells [x][belowCoord] == '#':
                numNeighbors += 1 #bottom neighbor is alive
            if currentCells [rightCoord][belowCoord] == '#':
                numNeighbors += 1 #bottom right neighbor is alive
            
            #set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living  cells with 2 or 3 neighbors stay alive
                nextCells [x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors ==3:
                #dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                #everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) #add a 1-second pause to reduce flickering