import random

class Play:
    def __init__(self, offense, defense, winningPlayer, scoreDifference, playOption=None):
        self.offense = offense
        self.defense = defense
        self.playOption = playOption
        self.scoreDifference = scoreDifference
        self.winningPlayer = winningPlayer
        self.stealCost = 2
        self.layupCost = 4
        self.jumperCost = 2
        self.defenseCost = 2
        self.reboundCost = 1
    
    def randomModifier(self):
        return random.uniform(-0.15, 0.15)

    def exhaustionModifier(self, type):
        if type == "offense":
            if self.offense.fatigue == "Well Rested":
                return random.uniform(0, 0.10)
            elif self.offense.fatigue == "Rested":
                return random.uniform(-0.05, 0.0)
            elif self.offense.fatigue == "Tired":
                return random.uniform(-0.10, 0.0)
            elif self.offense.fatigue == "Exhausted":
                return random.uniform(-0.15, 0.0)
            else:
                return random.uniform(-0.05, 0.05)
        else:
            if self.defense.fatigue == "Well Rested":
                return random.uniform(0, 0.10)
            elif self.defense.fatigue == "Rested":
                return random.uniform(-0.05, 0.0)
            elif self.defense.fatigue == "Tired":
                return random.uniform(-0.10, 0.0)
            elif self.defense.fatigue == "Exhausted":
                return random.uniform(-0.15, 0.0)
            else:
                return random.uniform(-0.05, 0.05)
        
        
    
    def choosePlay(self):
        playOptions = {
            "Layup": self.offense.layup,
            "Midrange": self.offense.midrange,
            "Three": self.offense.three
        }
        
        highestAttribute = max(playOptions, key=playOptions.get)
        playOptions[highestAttribute] += 15
        if self.offense != self.winningPlayer:
            if self.scoreDifference <= 6:
                playOptions[highestAttribute] += 10
            else:
                playOptions['Three'] += 20
        
        totalWeight = sum(playOptions.values())
        
        randomNumber = random.uniform(0, totalWeight)
        
        cumulativeWeight = 0
        selectedPlay = None
        
        for play, weight in playOptions.items():
            cumulativeWeight += weight
            if randomNumber <= cumulativeWeight:
                selectedPlay = play
                break
        
        return selectedPlay
    
    def dribbleCheck(self, playType):
        maxStealCheck = 0.10
        
        stealModifier= min(self.defense.steal / 99, maxStealCheck)
        baseSuccessProbability = 0.9 + (self.offense.dribble - 1) * 0.10/ 98  # Scales from 65% to 85%
        stealChance = baseSuccessProbability - stealModifier + self.randomModifier() + self.exhaustionModifier("offense")
        #print(f'{self.offense} has a {stealChance * 100}% chance of not having the ball be stolen')

        
        if random.random() > stealChance:
            print(f'{self.defense} steals the ball from {self.offense}')
            self.defense.stats.totalSteals += 1
            self.offense.stats.totalTurnovers += 1
            self.offense.loseEnergy(self.stealCost)
            self.defense.loseEnergy(self.stealCost)
            return 100
        else:
            print(f'{self.offense} escapes the steal attempt from {self.defense}!')
            defenseSkill = 0
            if playType == "Inside":
                defenseSkill = self.defense.insideD / 99
            else:
                defenseSkill = self.defense.outsideD / 99
            defenseChance = baseSuccessProbability - (defenseSkill * 0.4) + self.exhaustionModifier("defense")
            if random.random() < defenseChance:
                print(f'{self.defense} clamps down on {self.offense}')
                self.offense.loseEnergy(self.defenseCost)
                return -0.1
            else:
                print(f"{self.offense} dribbles by {self.defense}'s defense!")
                self.defense.loseEnergy(self.defenseCost)
                return 0.1
        
        
    def layup(self):
        if self.playOption == None:
            self.playOption = 'Layup'
        dribbleResult = self.dribbleCheck("Inside")
        if dribbleResult == 100:
            return 'Steal'
        else:
            print(f'{self.offense} goes for the layup!')
            baseSuccessProbability = 0.05 + (self.offense.layup - 1) * 0.55 / 98 # scale from 5% to 60%
            insideDModifier = self.defense.insideD / 99
            successProbability = baseSuccessProbability - (insideDModifier * 0.2) + (dribbleResult) + self.randomModifier() + self.exhaustionModifier("offense")
            # make sure the success probability is within range
            successProbability = max(0.01, min(successProbability, 0.99))
            #print(f"Success chance of {self.offense}'s against {self.defense}'s defense is {successProbability * 100}%")
        
            #simulate
            if random.random() < successProbability:
                print("Layup succeeds!")
                self.offense.loseEnergy(self.layupCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalMakes += 1
                self.offense.stats.totalLayupAttempts += 1
                self.offense.stats.totalLayupMakes += 1
                return True
            else:
                print("Layup fails!")
                self.offense.loseEnergy(self.layupCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalLayupAttempts += 1
                return False
        
    
    def midRange(self):
        if self.playOption == None:
            self.playOption = 'Midrange'
        dribbleResult = self.dribbleCheck("Outside")
        if dribbleResult == 100:
            return 'Steal'
        else:
            print(f'{self.offense} goes for the midrange shot!')
            baseSuccessProbability = 0.05 + (self.offense.midrange - 1) * 0.45 / 98 # scale from 5% to 50%
            outsideDModifier = self.defense.outsideD / 99
            successProbability = baseSuccessProbability - (outsideDModifier * 0.2) + (dribbleResult) + self.randomModifier() + self.exhaustionModifier("offense")
            # make sure the success probability is within range
            successProbability = max(0.01, min(successProbability, 0.99))
            #print(f"Success chance of {self.offense}'s against {self.defense}'s defense is {successProbability * 100}%")
        
            #simulate
            if random.random() < successProbability:
                print("Midrange succeeds!")
                self.offense.loseEnergy(self.jumperCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalMakes += 1
                self.offense.stats.totalMidrangeAttempts += 1
                self.offense.stats.totalMidrangeMakes += 1
                return True
            else:
                print("Midrange fails!")
                self.offense.loseEnergy(self.jumperCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalMidrangeAttempts += 1
                return False
    
    def Three(self):
        if self.playOption == None:
            self.playOption = 'Three'
        dribbleResult = self.dribbleCheck("Outside")
        if dribbleResult == 100:
            return 'Steal'
        else:
            print(f'{self.offense} goes for the three point shot!')
            baseSuccessProbability = 0.05 + (self.offense.three - 1) * 0.35 / 98 # scale from 5% to 40%
            outsideDModifier = self.defense.outsideD / 99
            successProbability = baseSuccessProbability - (outsideDModifier * 0.2) + (dribbleResult) + self.randomModifier() + self.exhaustionModifier("offense")
            # make sure the success probability is within range
            successProbability = max(0.01, min(successProbability, 0.99))
            #print(f"Success chance of {self.offense}'s against {self.defense}'s defense is {successProbability * 100}%")
        
            #simulate
            if random.random() < successProbability:
                print("Three succeeds!")
                self.offense.loseEnergy(self.jumperCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalMakes += 1
                self.offense.stats.totalThreeAttempts += 1
                self.offense.stats.totalThreeMakes += 1
                return True
            else:
                print("Three fails!")
                self.offense.loseEnergy(self.jumperCost)
                self.offense.stats.totalShots += 1
                self.offense.stats.totalThreeAttempts += 1
                return False
            
    def passing(self):
        if self.playOption == None:
            self.playOption = 'Pass'
    
    def rebound(self):
        defenseReboundChance = self.defense.rebound / 99
        #print(f'Defense chance at start: {defenseReboundChance}')
        offenseReboundChance = self.offense.rebound / 99
        # if not a layup defense will be closer to rim theoretically so better chance
        if self.playOption != 'Layup':
            defenseReboundChance += 0.2
            defenseReboundChance += 0.03 + (self.defense.insideD - 1) * 0.10 / 98 
        else:
            defenseReboundChance += 0.01 + (self.defense.outsideD - 1) * 0.05 / 98 
        #print(f'Defense chance after play option: {defenseReboundChance}')
        
        # taller means more likely
        if self.defense.height > self.offense.height:
            defenseReboundChance += 0.2
        elif self.offense.height > self.defense.height:
            offenseReboundChance += 0.2
        #print(f'Defense chance after height: {defenseReboundChance}')
        
        # better jump means better chance
        if self.defense.jump > self.offense.jump:
            defenseReboundChance += 0.2
        elif self.offense.jump > self.defense.jump:
            offenseReboundChance += 0.2
        #print(f'Defense chance after jump: {defenseReboundChance}')
        # better IQ means better chance
        if self.defense.iq > self.offense.iq:
            defenseReboundChance += 0.1
        elif self.offense.iq > self.defense.iq:
            offenseReboundChance += 0.1
        #print(f'Defense chance after iq: {defenseReboundChance}')
        
        # more weight measn more likely to box out 
        if self.defense.weight > self.offense.weight:
            defenseReboundChance += 0.1
        elif self.offense.weight > self.defense.weight:
            offenseReboundChance += 0.1
        
        # strength diff
        if self.defense.strength > self.offense.strength:
            defenseReboundChance += 0.1
        elif self.offense.strength > self.defense.strength:
            offenseReboundChance += 0.1
        
        # speed diff
        if self.defense.speed > self.offense.speed:
            defenseReboundChance += 0.05
        elif self.offense.speed > self.defense.speed:
            offenseReboundChance += 0.05
        
        # agility diff
        if self.defense.agility > self.offense.agility:
            defenseReboundChance += 0.1
        elif self.offense.agility > self.defense.agility:
            offenseReboundChance += 0.1
        
            
        #print(f'Defense chance after weight: {defenseReboundChance}')
        # random modifier
        defenseReboundChance += (2*self.randomModifier())+ self.exhaustionModifier("defense")
        offenseReboundChance += (2*self.randomModifier())+ self.exhaustionModifier("offense")
        totalReboundWeight = offenseReboundChance + defenseReboundChance
        #print(f'Defense chance after random: {defenseReboundChance}')
        #print(f'the chance for defensive rebound of {self.defense} is {defenseReboundChance*100}% with a number of {defenseReboundChance}')
        #print(f'the chance for defensive rebound of {self.offense} is {offenseReboundChance*100}% with a number of {offenseReboundChance}')
        #print(f'together it is {defenseReboundChance + offenseReboundChance}')
        
            
        randomChance = random.uniform(0, totalReboundWeight)
        #print(f'random chance number is {randomChance}')
        if randomChance <= defenseReboundChance:
            self.offense.loseEnergy(self.reboundCost)
            self.defense.loseEnergy(self.reboundCost)
            print(f'{self.defense} gets the rebound!')
            self.defense.stats.totalDefensiveRebounds += 1
            return self.defense
        elif randomChance > (defenseReboundChance):
            self.offense.loseEnergy(self.reboundCost)
            self.defense.loseEnergy(self.reboundCost)
            print(f'{self.offense} gets the offensive rebound! Another shot!')
            self.offense.stats.totalOffensiveRebounds += 1
            return self.offense
        else:
            print("REBOUND ERROR")
    
    def openShot(self, type):
        if type == "three":
            baseSuccessProbability = 0.05 + (self.offense.three - 1) * 0.35 / 98 # scale from 5% to 40%
            successProbability = max(0.01, min(baseSuccessProbability, 0.99))
            #print(f'{self.offense} shot chance is {successProbability*100}%')
            randomChanceNumber = random.random()
            #print(f'random number is {randomChanceNumber}')
            if randomChanceNumber < successProbability:
                print(f'{self.offense} hits the shot!')
                return True
            else:
                print(f'{self.offense} misses the shot!')
                return False
            
        else:
            pass