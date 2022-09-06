
# o(n) time | o(k) space
def solution(competitions, results):
    currentBestTeam = "" 
    scores = {currentBestTeam: 0}
    
    for idx, competition in enumerate(competitions):
        result = results[idx]
        
        homeTeam, awayTeam = competition
        
        winningTeam = homeTeam if result == 1 else awayTeam
        
        updateScores(winningTeam, 3, scores)
        
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points
    

competitions = [["HTML","C#"], ["C#","Python"],["Python", "HTML"]]
results = [0,0,1]

print(solution(competitions, results))


def tournamentWinner(competitions, results):
    # Write your code here.
    teamPoints = {}
    currentWinner = '',0
    for competition, result in zip(competitions, results):
        winner = competition[not result]
        if winner not in teamPoints: teamPoints[winner] = 0
        teamPoints[winner] += 3

        if teamPoints[winner] > currentWinner[1]:
            currentWinner = winner, teamPoints[winner]
    return currentWinner[0]
