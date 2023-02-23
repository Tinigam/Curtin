with open('/home/tinigam/FOP1005/Mid-Trimester_Test/Pending.csv', 'r') as file:
    count = 0
    for line in file:
        values = line.strip().split(',')
        if all(value == 'Done' for value in values[1:]):
            count += 1
    print(f"{count} students have completed all three tests.")
