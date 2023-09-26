class Stats:
    def __init__(self, totalShots=0, totalMakes=0, totalThreeAttempts=0, totalThreeMakes=0, totalLayupAttempts=0, totalLayupMakes=0, totalMidrangeAttempts=0, totalMidrangeMakes=0, totalSteals=0, totalOffensiveRebounds=0, totalDefensiveRebounds=0, totalAssists=0, totalBlocks=0, totalTurnovers=0):
        self.totalShots = totalShots
        self.totalMakes = totalMakes
        self.totalThreeAttempts = totalThreeAttempts
        self.totalThreeMakes = totalThreeMakes
        self.totalLayupAttempts = totalLayupAttempts
        self.totalLayupMakes = totalLayupMakes
        self.totalMidrangeAttempts = totalMidrangeAttempts
        self.totalMidrangeMakes = totalMidrangeMakes
        self.totalSteals = totalSteals
        self.totalOffensiveRebounds = totalOffensiveRebounds
        self.totalDefensiveRebounds = totalDefensiveRebounds
        self.totalAssists = totalAssists
        self.totalBlocks = totalBlocks
        self.totalTurnovers = totalTurnovers
    
    @property
    def shotPercentage(self):
        shots = (self.totalMakes/self.totalShots) / 100
        shotPerc = round((shots), 1)
        return shotPerc
    
    def statline(self):
        return f'Shot: {round(((self.totalMakes/self.totalShots)*100))}% ({self.totalMakes}/{self.totalShots}) | Total Rebounds: {self.totalOffensiveRebounds + self.totalDefensiveRebounds} | Offensive Rebounds: {self.totalOffensiveRebounds} | Defensive Rebounds: {self.totalDefensiveRebounds} | Steals: {self.totalSteals} | Turnovers: {self.totalTurnovers}'
        