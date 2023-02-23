#
# competition_v2.py - 
#

def inputValue(lower, upper, prompt):
    value = int(input(prompt))
    while value < lower or value > upper:
        print("ERROR!")
        value = int(input(prompt))
    return value

numJudges = 7
numCompetitors = inputValue(3, 16, "Enter number of competitors (between 3 and 16 inc)")

for comp in range(numCompetitors):
    totalC = 0
    print("input scores between 0 to 10 for each Judge")
    for j in range(numJudges):
        scoreJ = inputValue(0, 10, "Enter number of score for Judge (between 0 and 10 inc)")
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor is ", scoreC)