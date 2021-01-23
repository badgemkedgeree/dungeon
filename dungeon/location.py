import creature

class Location:
    
    def __init__ (self,identifier, description,enemy_identifier=None,next_location_identifier=None):
        self.identifier = identifier
        self.description = description
        self.enemy_identifier = enemy_identifier
        self.next_location_identifier = next_location_identifier
        
    def there_is_a_next_location(self):
        return self.next_location_identifier is not None