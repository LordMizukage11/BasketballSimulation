from apiHandler import ApiHandler
from player import Player
from play import Play
import random

class BasketballGame:
    def __init__(self, teamA, teamB, scoreLimit, ball="winner"):
        self.teamA = teamA
        self.teamB = teamB
        self.teamCheck = False
        self.scoreLimit = scoreLimit
        self.currentPosession = None
        self.currentDefense = None
        self.score = {teamA: 0, teamB: 0}
        self.ball = ball

    def getHighScore(self):
        topScoreTeam = max(self.score, key=lambda team: self.score[team])
        return topScoreTeam
    
    def getLowScore(self):
        lowScoreTeam = min(self.score, key=lambda team: self.score[team])
        return lowScoreTeam
    
    def getScoreDifferential(self):
        winning = self.getHighScore()
        losing = self.getLowScore()
        winningScore = self.score[winning]
        losingScore = self.score[losing]
        difference = winningScore - losingScore
        return difference
    
    def shootForBall(self):
        print("Starting the shootout!")
        # First check who shoots first
        if random.choice([True, False]):
            shootingTeam = self.teamA
            defendingTeam = self.teamB
        else:
            shootingTeam = self.teamB
            defendingTeam = self.teamA
            
        ## Simulate shoot off
        shotMade = False
        while shotMade is False:
            shot = Play(shootingTeam, defendingTeam, False, 0)
            shotMade = shot.openShot("three")
            if shotMade is False:
                temp = shootingTeam
                shootingTeam = defendingTeam
                defendingTeam = temp
        print(f'{shootingTeam} won the shootout!')
        self.currentPosession = shootingTeam
        self.currentDefense = defendingTeam
            
    
    def play(self):
        self.shootForBall()
        
        while True:
            self.showScore()
            self.simulatePlay()
            if (self.checkScore() == True):
                break
        
        winner = self.getHighScore()
        loser = self.getLowScore()
        print(f'{winner} wins the game against {loser}! The score was {self.score[winner]} - {self.score[loser]}')
        print(" --- ")
        print("Stats:")
        winner.getStats()
        loser.getStats()
    
    def simulatePlay(self):
        #print(f'{self.currentPosession} has posession and {self.currentDefense} is on defense!')
        play = Play(self.currentPosession, self.currentDefense, self.getHighScore(), self.getScoreDifferential())
        selectedPlay = play.choosePlay()
        #print(f'{self.currentPosession} chooses {selectedPlay}')
        if selectedPlay == "Layup":
            result = play.layup()
        elif selectedPlay == "Midrange":
            result = play.midRange()
        elif selectedPlay == "Three":
            result = play.Three()
        self.endPlay(result, selectedPlay)
    
    def endPlay(self, result, selectedPlay):
        if result == True:
            if selectedPlay == "Layup" or selectedPlay == "Midrange":
                self.updateScore(2)
                if self.ball == "loser":
                    self.togglePosession()
            else:
                self.updateScore(3)
                if self.ball == "loser":
                    self.togglePosession()
        elif result == "Steal":
            temp = self.currentPosession
            self.currentPosession = self.currentDefense
            self.currentDefense = temp
        else:
            rebound = Play(self.currentPosession, self.currentDefense, self.getHighScore(), self.getScoreDifferential())
            reboundWinner = rebound.rebound()
            self.currentPosession = reboundWinner
            if reboundWinner == self.teamA:
                self.currentDefense = self.teamB
            else:
                self.currentDefense = self.teamA
            
    
    def updateScore(self, result):
        self.score[self.currentPosession] += result
    
    def checkScore(self):
        for team, score in self.score.items():
            if score >= self.scoreLimit:
                return True
        return False
    
    def togglePosession(self):
        if self.currentPosession == self.teamA:
            self.currentPosession = self.teamB
            self.currentDefense = self.teamA
        else:
            self.currentPosession = self.teamA
            self.currentDefense = self.teamB
    
    def showScore(self):
        print(f'Score is: {self.teamA}({self.teamA.fatigue}) - {self.score[self.teamA]} VS {self.teamB}({self.teamB.fatigue}) - {self.score[self.teamB]}')
        
        
    
api = ApiHandler()
player1 = api.getPlayer('Ethan Decker')
player2 = api.getPlayer('Stephon Rosario')
testGame = BasketballGame(player1, player2, 11)
testGame.play()