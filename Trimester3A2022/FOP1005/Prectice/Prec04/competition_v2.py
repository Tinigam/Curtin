#
# competition_v2.py - 
#

numJudges = 7
numCompetitors = int(input("Enter number of competitors (between 3 and 16 inc)"))

while numCompetitors < 3 or numCompetitors > 16:
    numCompetitors = int(input("Error - Re-enter number of competitors (between 3 and 16 inc)"))

for comp in range(numCompetitors):
    totalC = 0
    print("input scores between 0 to 10 for each Judge")
    for j in range(numJudges):
        scoreJ = int(input("Enter the score for Judge"))
        while scoreJ < 0 or scoreJ > 10:
            scoreJ = int(input("Error - Re-enter number of score for Judge (between 0 and 10 inc)"))
        totalC = totalC + scoreJ
    scoreC = totalC / numJudges
    print("Score for competitor is ", scoreC)