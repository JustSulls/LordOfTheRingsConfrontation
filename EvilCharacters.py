import Character
import SpecialText


class Orcs(Character.Character):
    def __init__(self, the_map):
        super().__init__(10,
                         "Orcs",
                         2,
                         SpecialText.SpecialText("When attacking, instantly defeat the first character.", 2),
                         Character.Side.EVIL,
                         the_map)
        self.defeated_first_character = False

    def do_special_ability(self, *args):
        """
        Instantly kills (removes from map and player's character list) enemy
        if not already once used.
        :param args: Enemy (Character) to use ability on.
        :return:
        """
        if self.defeated_first_character:
            return
        else:
            for arg in args:
                self.instant_kill_first_enemy(arg)

    def instant_kill_first_enemy(self, enemy):
        # Insta kill enemy
        print("Orcs' special activated.")
        print(self.special_text)
        # Get region with enemy character
        region = self.map.region_with_character(enemy)
        # Remove enemy character from region.
        region.characters.remove(enemy)
        # Remove region from enemy character.
        enemy.region = None
        # After which, game should check map for defeated characters then remove
        # any defeated character found from player inventory of characters.
        print("Orcs instantly kill " + enemy.name + ". ")
        self.defeated_first_character = True


class Shelob(Character.Character):
    def __init__(self, the_map):
        super().__init__(11,
                         "Shelob",
                         5,
                         SpecialText.SpecialText("After Shelob defeats an Enemy character, she is immediately "
                                                 "returned to Gondor.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def retreat_to_gondor(self):
        pass


class Saruman(Character.Character):
    def __init__(self, the_map):
        super().__init__(12,
                         "Saruman",
                         4,
                         SpecialText.SpecialText("May decide that no cards are played.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args)-> bool:
        """
        Decide if no cards are played.
        :param args: Enemy character)
        :return: True if no cards are to be played, False otherwise.
        """
        print(self.name + " special activated. " + str(self.special_text))
        return self.decide_if_cards_are_played()

    @staticmethod
    def decide_if_cards_are_played()-> bool:
        choice = input("Decide no cards are played? y/n...")
        choice = choice.lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            raise ValueError("invalid choice in saruman special.")


class FlyingNazgul(Character.Character):
    def __init__(self, the_map):
        super().__init__(13,
                         "Flying Nazgul",
                         3,
                         SpecialText.SpecialText("May attack a single Good character anywhere on the board.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def attack_single_anywhere(self):
        pass

    def see_potential_moves(self):
        """
        See character's potential standard and special moves based on current region.
        :return: list(int, int) of potential region coordinates available. (None) if no available.
        """
        potential_regions = []
        regions_with_enemy = []
        potential_regions_with_enemy = []
        returned_regions = []

        if self.region.y < 3:
            l1 = [self.region.x, self.region.y + 1]
            potential_regions.append(l1)
        # Don't go out of bounds right
        if self.region.x < 3:
            l2 = [self.region.x + 1, self.region.y]
            potential_regions.append(l2)

        x = self.region.x
        y = self.region.y
        max_y = 4   # Plus one for range function
        max_x = 4   # Plus one for range function
        for i in range(x, max_x):
            for j in range(y, max_y):
                potential_regions_with_enemy.append([i, j])

        if potential_regions_with_enemy:
            for coordination in potential_regions_with_enemy:
                the_region = self.map.positions[tuple(coordination)]
                if the_region.contains_good_characters:
                    regions_with_enemy.append([the_region.x, the_region.y])

        if potential_regions:
            for region in potential_regions:
                returned_regions.append(region)
        if regions_with_enemy:
            for region in regions_with_enemy:
                returned_regions.append(region)

        # initialize a null list
        unique_regions = []

        # traverse for all elements
        for x in returned_regions:
            # check if exists in unique_list or not
            if x not in unique_regions:
                unique_regions.append(x)
        if unique_regions:
            return unique_regions
        else:
            return None


class Balrog(Character.Character):
    def __init__(self, the_map):
        super().__init__(14,
                         "Balrog",
                         5,
                         SpecialText.SpecialText("When in Moria, instantly defeats any Character using the Tunnel.",
                                     2),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def instantly_defeat_in_moria_tunnel(self):
        pass


class Warg(Character.Character):
    def __init__(self, the_map):
        super().__init__(15,
                         "Warg",
                         2,
                         SpecialText.SpecialText("Enemy character's text is ignored.",
                                     3),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def ignore_enemy_text(self):
            pass


class BlackRider(Character.Character):
    def __init__(self, the_map):
        super().__init__(16,
                         "Black Rider",
                         3,
                         SpecialText.SpecialText("May move forward any number of regions to attack.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def see_potential_moves(self):
        """
        See character's potential standard and special moves based on current region.
        :return: list(int, int) of potential region coordinates available. (None) if no available.
        """
        potential_regions = []
        regions_with_enemy = []
        potential_regions_with_enemy = []
        returned_regions = []

        if self.region.y < 3:
            l1 = [self.region.x, self.region.y + 1]
            potential_regions.append(l1)
        # Don't go out of bounds right
        if self.region.x < 3:
            l2 = [self.region.x + 1, self.region.y]
            potential_regions.append(l2)

        x = self.region.x
        y = self.region.y
        max_y = 4   # Plus one for range function
        max_x = 4   # Plus one for range function
        for i in range(x, max_x):
            for j in range(y, max_y):
                potential_regions_with_enemy.append([i, j])

        if potential_regions_with_enemy:
            for coordination in potential_regions_with_enemy:
                the_region = self.map.positions[tuple(coordination)]
                if the_region.contains_good_characters:
                    regions_with_enemy.append([the_region.x, the_region.y])

        if potential_regions:
            for region in potential_regions:
                returned_regions.append(region)
        if regions_with_enemy:
            for region in regions_with_enemy:
                returned_regions.append(region)

        # initialize a null list
        unique_regions = []

        # traverse for all elements
        for x in returned_regions:
            # check if exists in unique_list or not
            if x not in unique_regions:
                unique_regions.append(x)
        if unique_regions:
            return unique_regions
        else:
            return None


class WitchKing(Character.Character):
    def __init__(self, the_map):
        super().__init__(17,
                         "Witch King",
                         5,
                         SpecialText.SpecialText("May attack sideways.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def see_potential_moves(self):
        potential_regions = []

        # Check if left
        left_region = self.region.region_left_of
        if left_region:
            # Check if can attack adjacent region
            if left_region.contains_good_characters:
                potential_regions.append([left_region.x, left_region.y])
        # Check if right
        right_region = self.region.region_right_of
        if right_region:
            # Check if can attack adjacent region
            if right_region.contains_good_characters:
                potential_regions.append([right_region.x, right_region.y])

        # Bad character.
        # Don't go out of bounds left
        if self.region.y < 3:
            l1 = [self.region.x, self.region.y + 1]
            potential_regions.append(l1)
        # Don't go out of bounds right
        if self.region.x < 3:
            l2 = [self.region.x + 1, self.region.y]
            potential_regions.append(l2)
        if potential_regions:
            return potential_regions
        else:
            return None

    def do_special_ability(self, *args):
        pass

    def attack_sideways(self):
        pass


class CaveTroll(Character.Character):
    def __init__(self, the_map):
        super().__init__(18,
                         "Cave Troll",
                         9,
                         SpecialText.SpecialText("The Dark Player's card has no value or effect.",
                                     0),
                         Character.Side.EVIL,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def cancel_dark_player_card(self):
        pass
