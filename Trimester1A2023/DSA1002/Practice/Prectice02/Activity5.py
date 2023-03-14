def moveDisk(n, src, dest):
    print(f"Move disk {n} from {src} to {dest}")

def hanoi(n, src, temp, dest):
    if n == 1:
        moveDisk(n, src, dest)
    # elif n == 2:
    #     moveDisk(n, src, temp)
    #     moveDisk(n, src, dest)
    #     moveDisk(n, temp, dest)
    else:
        hanoi(n - 1, src, dest, temp)
        moveDisk(n, src, dest)
        hanoi(n - 1, temp, src, dest)

def main():
    inValn = input("Please enter the number of disks:\n")
    inValsrc = input("Please enter the name of source peg:\n")
    inValtemp = input("Please enter the name of tempory peg:\n")
    inValdest = input("Please enter the name of destination peg\n")
    hanoi(inValn, inValsrc, inValtemp, inValdest)

main()
# hanoi(4, "A", "B", "C")