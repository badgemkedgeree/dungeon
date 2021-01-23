import json

from creature import Creature
from location import Location


class World:

    def __init__(self):
        self.locations = {}
        self.creatures = {}
        with open("data/world.json") as file:
            world_dict = json.load(file)
            for loc in world_dict['locations']:
                self.locations[loc['identifier']] = Location(**loc)
            for critter in world_dict['creatures']:
                self.creatures[critter['identifier']] = Creature(**critter)

    def get_location(self, identifier):
        return self.locations.get(identifier, None)

    def get_next_location(self, identifier):
        return self.locations.get(self.locations[identifier].next_location_identifier, None)

    def get_creature(self, identifier):
        return self.creatures.get(identifier, None)
