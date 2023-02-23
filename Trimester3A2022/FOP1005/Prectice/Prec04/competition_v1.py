#
# competition_v1.py - 
#

numJudges = 7
numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc)"))

for comp in range(numCompetitors):
    totalC = 0
    print("input scores between 0 to 10 for each Judge")
    for j in range(numJudges):
        scoreJ = int(input("Enter the score for Judge"))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor is ", scoreC)