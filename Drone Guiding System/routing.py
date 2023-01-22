import numpy as np
import os
import fnmatch
import docx2txt
import matplotlib.pyplot as plt
n = 12  #size of grid

# To convert all .docx file to .txt file
res = []
for path in os.listdir('.'):
    if os.path.isfile(os.path.join('.', path)):
         if(fnmatch.fnmatch(path,"*.docx")): 
                convertFile = docx2txt.process(path)
                file = path.split(".")
                output = file[0]+".txt"
                with open(output, "w") as text_file:
                     print(convertFile, file=text_file)
                
def solve(moves, coord, row, column):
    ny = column
    nx = row
    l = [(row, column)]
    for k in moves:
        if k == "N":
            while (nx, ny) in l:
                ny += 1
        elif k == "S":
            while (nx, ny) in l:
                ny -= 1
        elif k == "E":
            while (nx, ny) in l:
                nx += 1
        else:
            while (nx, ny) in l:
                nx -= 1
        if nx <= 0 or ny <=0:
            print("\n\tError: The route is outside of the grid.")
            break
        l.append((nx, ny))
    return l

def plotGraph(coordinates,n,filename):
#     plt.rcdefaults()
    name = filename.split('.')[0]
    coordinatesArray = np.array(coordinates)  #converting list of cootdinates into array
    fig = plt.figure(facecolor="#e1ddbf")
    dim=np.arange(1,n+1,1)   #It is arranging arrany points from 1--->12 i.e, 1,2,3,4...12
    fig.set_size_inches(8, 7)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.xlim(0, n)        #limiting range of x-axis
    plt.ylim(0, n)
    plt.xticks(dim)
    plt.yticks(dim)
    plt.annotate(' start',coordinatesArray[0])  #labeling the starting point
    plt.annotate(' stop',coordinatesArray[-1])  #labeling the stoping point
    plt.plot(*coordinatesArray.T,'o--',color='steelblue',linewidth=3)
    plt.title('Drone Guidance System\n',fontname='Gabriola', fontsize=22)
    plt.grid()
    # plt.savefig(name+'.png',facecolor=fig.get_facecolor())  # uncomment this line to save graph as a seperate file with name (filename.png)
    plt.show()

def main():
    while(True):
        routeInstructions = input("Enter the next route instructions file or enter STOP to finish: ")
        if routeInstructions == 'STOP':
            print("\t\tProgram terminated!")
            break
        try:
            instructions = []
            with open(routeInstructions,'r') as f:
                for line in f:
                    if line.rstrip():
                        instructions.append(line.rstrip('\n'))
#             Assigning x and y coordinate values 
            row = int(instructions[0])
            column = int(instructions[1])
            moves = instructions[2:]
            coord = [row,column]
            coordinates = solve(moves,coord,row,column)
            plotGraph(coordinates,n,routeInstructions)
            print("Coordinates:\n\t",coordinates)         #printing coordinates
            print("="*(80+len(coordinates)))
        except IOError:
            print("\n\tFile not found") 

if __name__=="__main__":
    main()