from abc import *
import Region


class Side(enumerate):
    GOOD = 1
    EVIL = 2


class Character(ABC):
    def __init__(self, id, name, strength, special_text, side, map):
        self.id = id
        self.name = name
        self.strength = strength
        self.special_text = special_text
        self.region = None
        self.side = side
        self.map = map
        super().__init__()

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Character):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.id == other.id and self.name == other.name

    def __ne__(self, other): return not self == other

    def see_potential_moves(self) -> [[int, int]]:
        """
        See character's potential standard moves based on current region.
        :return: list(int, int) of potential region coordinates available. (None) if no available.
        """
        if not self.region:
            # Character not in a region.
            return None
        potential_regions = []
        if self.side == 1:
            # Good character.
            # Don't go out of bounds left
            if self.region.x > 0:
                l1 = [self.region.x - 1, self.region.y]
                potential_regions.append(l1)
            # Don't go out of bounds right
            if self.region.y > 0:
                l2 = [self.region.x, self.region.y - 1]
                potential_regions.append(l2)
            if potential_regions:
                return potential_regions
            else:
                return None
        else:
            # Bad character.
            # Don't go out of bounds left
            if self.region.y < 3:
                l1 = [self.region.x, self.region.y+1]
                potential_regions.append(l1)
            # Don't go out of bounds right
            if self.region.x < 3:
                l2 = [self.region.x+1, self.region.y]
                potential_regions.append(l2)
            if potential_regions:
                return potential_regions
            else:
                return None

    def move(self, region: Region):
        """
        Moves character to given (Region).
        :param region: (Region) to be moved to
        :return:
        """
        try:
            # Remove character's current region if it exists.
            if self.region is not None:
                self.region.characters.remove(self)

            # Set characters region to passed region
            self.region = region

            # Add character to chosen region's list of characters
            self.region.characters.append(self)
        except Exception as ex:
            print(ex)

    @abstractmethod
    def do_special_ability(self, *args):
        pass
