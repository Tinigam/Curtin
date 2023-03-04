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

hanoi(10, "A", "B", "C")
