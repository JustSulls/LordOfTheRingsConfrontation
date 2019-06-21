import Region
import Character


class Map:

    def __init__(self):
        self.place_names = ['Mordor', 'Gondor', 'Rohan', 'Gap of Rohan', 'Dagorlad', 'Fangorn',
                       'Moria', 'Endewaith', 'Mirkwood', 'Misty Mountains', 'Eregion', 'Cardolan',
                       'High Pass', 'Rhudaur', 'Arthedain', 'The Shire']
        self.regions = {}
        self.positions = {}

        # Setup regions dictionary
        self.init_places()

    def __str__(self):
        full_map_str = ""
        for k, region in self.regions.items():
            full_map_str += region.__str__()
            full_map_str += "\n"
        return full_map_str

    @property
    def exists_conflict(self)-> bool:
        # Check if region contains good and bad guy(s).
        conflict = False
        for k, v in self.regions.items():
            if not conflict:
                if v.contains_characters:
                    side = v.characters[0].side
                    for character in v.characters:
                        if character.side != side:
                            conflict = True
                            break
        return conflict

    def init_places(self):
        """
        Creates Regions and places them in the dictionary 'regions'.
        :return:
        """
        i = 0
        for x in range(4):
            for y in range(4):
                # New dictionary of names to regions.
                self.regions[self.place_names[i]] = Region.Region(self.place_names[i], x, y, self)
                # Dictionary of x y position to regions.
                self.positions[x, y] = self.regions[self.place_names[i]]
                i += 1

    def place_character_on_region(self, character, region):
        # Add character to region
        self.regions[region].region_receive_character(character)

    def region_with_character(self, character: Character.Character)-> Region.Region:
        """

        :param character: Character whose region we're looking for
        :return: Region character found in. None otherwise.
        """
        for k, v in self.regions.items():
            if v.characters:
                for c in v.characters:
                    if c is character:
                        return v
        return None
