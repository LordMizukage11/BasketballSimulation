import random

class Team:
    def __init__(self, players, name=None, location=None):
        self.players = players
        if name == None:
            self.generateName()
        else:
            name = name
        if location == None:
            self.generatelocation()
        else:
            location = location
    
    def generateName():
        # List of possible team names
        team_names = ["Lions", "Tigers", "Bears", "Eagles", "Dragons", "Panthers", "Wolves", "Sharks", "Cobras", "Scorpions"]

        # Randomly select a name from the list
        return random.choice(team_names)
    
    def generateLocation():
        # List of possible team locations
        team_locations = ["New York", "Los Angeles", "Chicago", "Miami", "Dallas", "Boston", "San Francisco", "Denver", "Seattle", "Atlanta"]

        # Randomly select a location from the list
        return random.choice(team_locations)