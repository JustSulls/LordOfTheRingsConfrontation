import Character


class Region:
    def __init__(self, name, x, y, the_map):
        self.name = name
        self.x = x
        self.y = y
        self.map = the_map
        self.characters = []

    def __str__(self):
        the_str = self.name
        if self.characters:
            if len(self.characters) > 1:
                the_str += ": "
                for character in self.characters:
                    the_str += character.name + ", "
                    # Gets rid of ugly comma at end.
                the_str = the_str[0:len(the_str)-2]
            else:
                the_str += ": " + self.characters[0].name
        return the_str

    def __eq__(self, other):
        if not isinstance(other, Region):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name

    def __ne__(self, other): return not self == other

    @property
    def location(self) -> [int, int]:
        return [self.x, self.y]

    @property
    def contains_characters(self) -> bool:
        if len(self.characters) > 0:
            return True
        else:
            return False

    @property
    def region_left_of(self) -> object:
        """
        Returns Region left of self. None if no region (out of bounds).
        :return: Regionleft of (str), (None) if out of bounds.
        """
        if self.x == 0 or self.y == 3:
            # Out of bounds left
            return None
        else:
            return self.map.positions[self.x - 1, self.y + 1]

    @property
    def region_right_of(self) -> object:
        """
        Returns Region right of self. None if no region (out of bounds).
        :return: Region right of (str), (None) if out of bounds
        """
        if self.x == 3 or self.y == 0:
            # Out of bounds right
            return None
        else:
            # Return region name right of self
            return self.map.positions[self.x + 1, self.y - 1]

    @property
    def region_below_and_left(self) -> object:
        """
        Returns Region below and left of self. None if no region (out of bounds).
        :return: Regionbelow and left of (str), (None) if out of bounds.
        """
        if self.x == 0:
            # Out of bounds below left
            return None
        else:
            # Return region name below and left
            return self.map.positions[self.x - 1, self.y]

    @property
    def region_below_and_right(self) -> object:
        """
        Returns Region below and right of self. None if no region (out of bounds).
        :return: Regionbelow and left of (str), (None) if out of bounds.
        """
        if self.y == 0:
            # Out of bounds below right
            return None
        else:
            # Return region name below and right
            return self.map.positions[self.x, self.y - 1]

    @property
    def region_above_and_left(self) -> object:
        """
        Returns Region above and left of self. None if no region (out of bounds).
        :return: Regionabove and left of (str), (None) if out of bounds.
        """
        if self.y == 3:
            # Out of bounds above left
            return None
        else:
            # Return region name above and left
            return self.map.positions[self.x, self.y + 1]

    @property
    def region_above_and_right(self) -> object:
        """
        Returns Region above and right of self. none if no region (out of bounds).
        :return: Regionabove and left of (str), (None) if out of bounds.
        """
        if self.x == 3:
            # Out of bounds above right
            return None
        else:
            # Return region name above and right
            return self.map.positions[self.x + 1, self.y]

    @property
    def character_count(self):
        return len(self.characters)

    @property
    def contains_evil_characters(self)-> bool:
        evil_found = False
        for character in self.characters:
            if character.side == Character.Side.EVIL:
                evil_found = True
                break
        return evil_found

    @property
    def contains_good_characters(self) -> bool:
        good_found = False
        for character in self.characters:
            if character.side == Character.Side.GOOD:
                good_found = True
                break
        return good_found

    @property
    def conflict_exists(self) -> bool:
        if self.contains_evil_characters and self.contains_good_characters:
            return True
        else:
            return False

    @property
    def contains_three_evil_characters(self) -> bool:
        evil_char_count = 0
        if self.contains_evil_characters:
            for character in self.characters:
                if character.side == 2:
                    evil_char_count += 1
            if evil_char_count >= 3:
                return True
            else:
                return False
        else:
            return False

    def region_receive_character(self, character: Character):
        """
        Adds character to Region. Sets character Region to self.
        Called by Map.
        :param character: Character to be placed on region.
        """
        self.characters.append(character)
        character.region = self

    def get_sauron_character(self) -> Character:
        """
        Gets a sauron character from this region.
        :return: Sauron character.
        """
        for character in self.characters:
            if character.side == Character.Side.EVIL:
                return character

    def get_fellowship_character(self) -> Character:
        """
        Gets a fellowship character from this region.
        :return: Fellowship character
        """
        for character in self.characters:
            if character.side == Character.Side.GOOD:
                return character
