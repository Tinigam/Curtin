import random
import matplotlib.pyplot as plt
from shrimp import Shrimp
import sys

XMAX = 1000
YMAX = 500
    
def main():
    shrimpList = []
    numOfShrimp = 15
    show_plot = "Y"
    if len(sys.argv) > 1:
        numOfShrimp = int(sys.argv[1])
    if len(sys.argv) > 2:
        show_plot = sys.argv[2]

    for i in range(numOfShrimp):
        randX = random.randint(0, XMAX)
        randY = random.randint(0, YMAX)
        shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))
     
    for i in range(numOfShrimp):
        xvalues = []
        yvalues = []
        for shrimp in shrimpList:
            shrimp.stepChange()
            xvalues.append(shrimp.pos[0])
            yvalues.append(shrimp.pos[1])

        # Shrimp multiply at a rate of 8%
        for i in range(int(numOfShrimp * 0.08)):
            randX = random.randint(0, XMAX)
            randY = random.randint(0, YMAX)
            shrimpList.append(Shrimp([randX, randY], [XMAX, YMAX]))

        if show_plot == 'Y':
            plt.scatter(xvalues, yvalues)   # Note plt origin is bottom left 
            plt.xlim(0,XMAX)
            plt.ylim(0,YMAX)
            plt.pause(1)
            plt.clf()

    print(f"{numOfShrimp},{len(shrimpList)}")
    
if __name__ == "__main__":
    main()