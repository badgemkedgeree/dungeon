class Location:

    def __init__(self, identifier, description, next_location_identifier=None, enemy_identifier=None):
        self.enemy_identifier = enemy_identifier
        self.identifier = identifier
        self.description = description
        self.next_location_identifier = next_location_identifier
