import StrengthCard
import Map
import Character
import Region


class Player:

    def __init__(self, map: Map, name: str, side: Character.Side):
        self.strength_cards = []
        self.init_cards()
        self.map = map
        self.name = name
        self.side = side

        self.characters = []

    def __eq__(self, other):
        if not isinstance(other, Player):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.side == other.side and self.name == other.name

    def __ne__(self, other): return not self == other

    def init_cards(self):
        for x in range(1, 6):
            self.strength_cards.append(StrengthCard.StrengthCard(x))

    def spawn_characters(self, spawn_place):
        for character in self.characters:
            self.map.place_character_on_region(character, spawn_place)

    def choose_card(self):
        print(self.name + " choosing strength card. ")
        i = 0
        for card in self.strength_cards:
            print(str(i) + " : " + "Strength card (" + str(card) + ").")
            i += 1
        try:
            choice = int(input("Choose a strength card. "))
        except Exception as ex:
            print(ex.__str__)

        card = self.strength_cards[choice]
        # Discard chosen card
        self.strength_cards.remove(card)
        print("Chosen strength card (" + str(card.strength) + ") for player (" + self.name + "). ")
        return card.strength

    def move_character(self, character: Character, region: Map.Region) -> bool:
        """
        Moves character to region. Does not currently handle battle.
        :param character: (Character) to be moved.
        :param region: (Region) to be moved to.
        :return:
        """
        # Get character's potential move cooCharacter.Side.GOODrdinates
        potential_region_coordinates = character.see_potential_moves()
        potential_regions = []

        # If character potential moves returned
        if potential_region_coordinates:
            for region_coordinate in potential_region_coordinates:
                # Add region objects to list
                potential_regions.append(self.map.positions[tuple(region_coordinate)])

            # Check if parameter region is a valid move.
            # True if any coordinate (x,y) returned in see_potential_moves() is parameter region coordinates
            result1 = any(elem in region.location for elem in potential_region_coordinates.pop())
            if potential_region_coordinates.__len__() > 0:
                result2 = any(elem in region.location for elem in potential_region_coordinates.pop())

            # If parameter region valid check.
            if result1 or result2:

                # Valid region passed to this function.
                # Move character to chosen region.
                character.move(region)
                return True
            else:
                # Invalid move, not in potential regions.
                raise ValueError("Invalid move, not in potential regions.")
        else:
            raise Exception('No region coordinates returned in player.move_character().')

    def choose_character_move(self)-> Character:
        """
        Provides text info for user input when choosing which character to move.
        :return: (Character) to be moved.
        """
        print("Choose character to move: ")
        i = 0
        for character in self.characters:
            if character.region is not None:
                print(str(i) + " : " + character.name + " at (" + character.region.name + ").")
            i += 1
        try:
            # --SCAFFOLD--
            # choice = 2
            choice = int(input("Choose character to move."))
            try:
                print("(" + self.characters[choice].name + ") chosen. ")
                chosen_character = self.characters[choice]
                return chosen_character
            except Exception as ex:
                print("Error during chosen character. " + ex.__str__())
        except ValueError as ex:
            print("Error number value error. " + ex.__str__())

    def receive_characters_init(self, characters: [Character]):
        for character in characters:
            self.characters.append(character)

    @staticmethod
    def spawn(character: Character, region: Map.Region):
        character.move(region)

    def choose_starting_positions(self):
        def good()-> bool:
            if self.side == 1:
                return True
            else:
                return False
        print("Choosing starting positions. ")
        if good():
            spawn_place = "The Shire"
        else:
            spawn_place = "Mordor"
        print(self.name + " chooses four of his characters and places them in " + spawn_place + ". ")

        available_to_choose_characters = list(self.characters)
        print("Choose character to spawn in " + spawn_place + ". ")
        spawn_place_characters = []

        def print_avail_chars(avail_chars):
            i = 0
            for guy in avail_chars:
                print(str(i) + " : " + guy.name)
                i += 1

        try:
            for i in range(4):
                print_avail_chars(available_to_choose_characters)
                # - SCAFFOLD
                # choice = int(input("Choose character to spawn in The Shire. "))
                choice = 0
                try:
                    the_character = available_to_choose_characters[choice]
                    print("(" + the_character.name + ") chosen. ")
                    spawn_place_characters.append(the_character)
                    available_to_choose_characters.remove(the_character)
                except Exception as ex:
                    print("Error during chosen character. " + ex.__str__())
        except ValueError as ex:
            print("Error number value error. " + ex.__str__())

        # Put chosen characters in spawn place
        for character in spawn_place_characters:
            self.spawn(character, self.map.regions[spawn_place])

        # Then  places his remaining five characters in the five regions in front of the
        # Shire (Arthedain, Cardolan, Enedwaith, Eregion, and
        # Rhudaur), so that each of those five regions contains one
        # Fellowship character.
        print("\nPlace remaining five characters in the five regions in front of the Shire. \n"
              "(Arthedain, Cardolan, Endewaith, Eregion, and Rhudaur), so that each of those\n"
              "five regions contains one fellowship character. ")

        def front_region_choices(region: str):
            # region
            print("Choose character to spawn in: " + self.map.regions[region].name)
            print_avail_chars(available_to_choose_characters)
            # - SCAFFOLD
            # choice = int(input("Choose character to spawn..."))
            choice = 0
            try:
                the_character = available_to_choose_characters[choice]
                print("(" + the_character.name + ") chosen. ")
                self.spawn(the_character, self.map.regions[region])
                available_to_choose_characters.remove(the_character)
            except Exception as ex:
                print("Error during chosen character. " + ex.__str__())

        if good():
            spawn_places = ["Arthedain", "Cardolan", "Endewaith", "Eregion", "Rhudaur"]
            # Arthedain
            front_region_choices(spawn_places[0])
            # Cardolan
            front_region_choices(spawn_places[1])
            # Endewaith
            front_region_choices(spawn_places[2])
            # Eregion
            front_region_choices(spawn_places[3])
            # Rhudaur
            front_region_choices(spawn_places[4])
        else:
            spawn_places = ["Gondor", "Dagorlad", "Fangorn", "Mirkwood", "Rohan"]
            # Gondor
            front_region_choices(spawn_places[0])
            # Dagorlad
            front_region_choices(spawn_places[1])
            # Fangorn
            front_region_choices(spawn_places[2])
            # Mirkwood
            front_region_choices(spawn_places[3])
            # Rohan
            front_region_choices(spawn_places[4])

