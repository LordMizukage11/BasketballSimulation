from stats import Stats
class Player(Stats):
    def __init__(self, firstName, lastName, fullName, age, height, weight, strength, endurance, agility, speed, iq, jump, dribble, passing,layup,midrange,three,steal, rebound, insideD, outsideD, hot, temperature, traits):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = fullName
        self.age = age
        self.height = height
        self.weight = weight
        self.strength = strength
        self.endurance = endurance
        self.agility = agility
        self.speed = speed
        self.iq = iq
        self.jump = jump
        self.dribble = dribble
        self.passing = passing
        self.layup = layup
        self.midrange = midrange
        self.three = three
        self.steal = steal
        self.rebound = rebound
        self.insideD = insideD
        self.outsideD = outsideD
        self.hot = hot
        self.temperature = temperature
        self.traits = traits
        self.energy = 100
        self.stats = Stats()
    
    @property
    def overall(self):
        #point totals
        skillTotal = self.dribble + self.passing + self.layup + self.midrange + self.three + self.steal + self.rebound + self.insideD + self.outsideD
        athleticsTotal = self.strength + self.endurance + self.agility + self.speed + self.iq + self.jump
        # Average
        overallAverage = (skillTotal + athleticsTotal) / 15

        # Ensure the overall score is within the range of 1 to 99
        overall =round(min(max(overallAverage, 1), 99))
        return overall
    @property
    def fatigue(self):
        if self.energy >= 75:
            level = "Well Rested"
        elif self.energy >= 45 and self.energy < 75:
            level = "Rested"
        elif self.energy >=15 and self.energy <25:
            level = "Tired"
        else:
            level = "Exhausted"
        return level
    
    def __str__(self):
        return f'{self.fullName}'
    
    def get(self):
        return f'{self.fullName} - {self.overall} OVR'
    
    def getStats(self):
        stats = self.stats.statline()
        print(f'{self.fullName} -- {stats}')
    
    def loseEnergy(self, cost):
        if self.endurance >= 95:
            self.energy -= (cost * .5)
        elif self.endurance >= 85 and self.endurance < 95:
            self.energy -= (cost * .75)
        elif self.endurance >= 70 and self.endurance < 85:
            self.energy -= (cost * 1)
        elif self.endurance >= 51 and self.endurance < 70:
            self.energy -= (cost * 1.2)
        else:
            self.energy -= (cost * 1.5)
                
        