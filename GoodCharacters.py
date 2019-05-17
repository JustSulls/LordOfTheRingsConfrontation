from SpecialText import *
import Region
import Character


class Frodo(Character.Character):
    def __init__(self, the_map):
        super().__init__(1,
                         "Frodo",
                         1,
                         SpecialText("When attacked, may retreat sideways.",
                                     1),
                         Character.Side.GOOD,
                         the_map)

    @property
    def adjacent_regions(self) -> [Region]:
        """
        Returns list of adjacent regions ([Region, Region]) available.
        :return: list of regions [Region, Region] if multiple available. List of [Region) if only one available.
        (None) if none available.
        """
        potential_regions = []
        if self.region.region_left_of is not None:
            potential_regions.append(self.region.region_left_of)
        if self.region.region_right_of is not None:
            potential_regions.append(self.region.region_right_of)
        if not potential_regions:
            # List empty, no available regions
            return None
        else:
            # List contains Region(s).
            return potential_regions

    def do_special_ability(self, *args)-> bool:
        """
        Returns true if retreated, false otherwise.
        :param args:
        :return:
        """
        # Check if sideways available.
        # Choose whether to retreat sideways.
        print("Choose whether to retreat sideways as Frodo.")
        try:
            # --SCAFFOLD--
            # choice = "n"
            choice = str(input("y/n"))
            if choice == "y":
                # Retreat chosen.
                print("(Retreat) chosen. ")
                self.retreat_sideways()
                return True
            elif choice == "n":
                # Not retreat chosen.
                print("(No retreat) chosen. ")
                return False
            else:
                # Invalid choice
                raise ValueError("Bad input at Frodo do_special_ability(). ")
        except Exception as ex:
            print(ex)
        # Move Frodo to region, end battle
        pass

    def retreat_sideways(self):
        # Provide region(s) as options to player
        if not self.adjacent_regions:
            # No regions available
            print("No regions available to retreat to. ")
            return
        else:
            # At least one region available
            if self.adjacent_regions.__len__() > 1:
                # Two regions returned
                # TODO: have player pick which region to retreat to.
                print("Choose which region to retreat to.")
                try:
                    print_str = ""
                    i = 0
                    for reg in self.adjacent_regions:
                        print_str += str(i) + " : " + reg.name + " "
                        i += 1
                    choice = int(input(print_str))
                    region_choice = self.adjacent_regions[choice]
                    self.move(region_choice)
                except Exception as ex:
                    print("Error during choose retreat region as Frodo. " + ex)

                pass
            else:
                # One region returned.
                # TODO: Fix this etc.
                self.move(self.adjacent_regions[0])
        pass


class Pippin(Character.Character):
    def __init__(self, the_map):
        super().__init__(2,
                         "Pippin",
                         1,
                         SpecialText("When attacking, may retreat backwards.",
                                     1),
                         Character.Side.GOOD,
                         the_map)

    @property
    def regions_behind(self) -> [Region]:
        """
        Returns list of regions behind ([Region, Region]) available.
        :return: list of regions [Region, Region] if multiple available. List of [Region) if only one available.
        (None) if none available.
        """
        potential_regions = []
        if self.region.region_above_and_left is not None:
            potential_regions.append(self.region.region_above_and_left)
        if self.region.region_above_and_right is not None:
            potential_regions.append(self.region.region_above_and_right)
        if not potential_regions:
            # List empty, no available regions
            return None
        else:
            # List contains Region(s).
            return potential_regions

    def do_special_ability(self, *args):
        # Check if sideways available.
        # Choose whether to retreat sideways.
        print("Choose whether to retreat backwards as Pippin.")
        try:
            # --SCAFFOLD--
            # choice = "n"
            choice = str(input("y/n"))
            if choice == "y":
                # Retreat chosen.
                print("(Retreat) chosen. ")
                self.retreat_backwards()
            elif choice == "n":
                # Not retreat chosen.
                print("(No retreat) chosen. ")
                return
            else:
                # Invalid choice
                raise ValueError("Bad input at Frodo do_special_ability(). ")
        except Exception as ex:
            print("Error during choose retreat as Frodo. " + ex)
        # Move Frodo to region, end battle
        pass

    def retreat_backwards(self):
        # Provide region(s) as options to player
        if not self.regions_behind:
            # No regions available
            print("No regions available to retreat to. ")
            return
        else:
            # At least one region available
            regions_behind = self.regions_behind
            if regions_behind.__len__() > 1:
                # Two regions returned
                # TODO: have player pick which region to retreat to.
                print("Choose which region to retreat to.")
                try:
                    print_str = ""
                    for reg in regions_behind:
                        print_str += reg.__str__() + " \n"
                    choice = str(input(print_str))
                    choice.lower()
                    region1 = regions_behind.pop()
                    region2 = regions_behind.pop()
                    if region1.lower() == choice.lower():
                        region = self.map.regions[region1]
                        self.move(region)
                    elif region2.lower() == choice.lower():
                        region = self.map.regions[region2]
                        self.move(region)
                    else:
                        raise ValueError("Error during Frodo do special ability region choice.")

                except Exception as ex:
                    print("Error during choose retreat region as Frodo. " + ex)

                pass
            else:
                # One region returned.
                # TODO: Fix this etc.
                try:
                    region = regions_behind.pop()
                    self.move(region)
                    # self.move(self.map.regions[regions_behind.pop()])
                except Exception as ex:
                    print(ex)
        pass


class Gandalf(Character.Character):
    def __init__(self, the_map):
        super().__init__(3,
                         "Gandalf",
                         5,
                         SpecialText("The Dark Player must play his card first.",
                                     0),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args)-> object:
        """
        Does Gandalf's special.
        :param args: Player Sauron
        :return: Player Sauron's chosen (Card).
        """
        for arg in args:
            # Have player choose strength card
            print(self.name + " special activated. " + str(self.special_text))
            card_chosen = arg.choose_card()
            return card_chosen


class Sam(Character.Character):
    def __init__(self, the_map):
        super().__init__(4,
                         "Sam",
                         2,
                         SpecialText("When with Frodo, is Strength 5 and may replace Frodo in battle.",
                                     1),
                         Character.Side.GOOD,
                         the_map)

    @property
    def with_frodo(self)-> bool:
        if self.region == self.map.region_with_character("Frodo"):
            return True

    def do_special_ability(self, *args)-> bool:
        if self.with_frodo:
            self.strength = 5
            if self.choose_to_replace_frodo():
                # TODO: replace Frodo in battle.
                return True
            else:
                return False
        else:
            self.strength = 2
            return False

    @staticmethod
    def choose_to_replace_frodo() -> bool:
        choice = input("Decide whether to replace Frodo? y/n...")
        choice = choice.lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            raise ValueError("invalid choice in Sam special.")


class Legolas(Character.Character):
    def __init__(self, the_map):
        super().__init__(5,
                         "Legolas",
                         3,
                         SpecialText("Instantly defeats the Flying Nazgul.",
                                     2),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args):
        pass


class Aragorn(Character.Character):
    def __init__(self, the_map):
        super().__init__(6,
                         "Aragorn",
                         4,
                         SpecialText("May attack any adjacent region.",
                                     0),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args):
        pass

    def see_potential_moves(self):
        """
        See character's potential standard and special moves based on current region.
        :return: list(int, int) of potential region coordinates available. (None) if no available.
        """
        potential_regions = []

        # Check if left
        left_region = self.region.region_left_of
        if left_region:
            # Check if can attack adjacent region
            if left_region.contains_evil_characters:
                potential_regions.append([left_region.x, left_region.y])
        # Check if right
        right_region = self.region.region_right_of
        if right_region:
            # Check if can attack adjacent region
            if right_region.contains_evil_characters:
                potential_regions.append([right_region.x, right_region.y])

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


class Gimli(Character.Character):
    def __init__(self, the_map):
        super().__init__(7,
                         "Gimli",
                         3,
                         SpecialText("Instantly defeats the Orcs.",
                                     2),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args):
        pass


class Merry(Character.Character):
    def __init__(self, the_map):
        super().__init__(8,
                         "Merry",
                         2,
                         SpecialText("Instantly defeats the Witch King.",
                                     2),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args):
        pass


class Boromir(Character.Character):
    def __init__(self, the_map):
        super().__init__(9,
                         "Boromir",
                         0,
                         SpecialText("Both Boromir and Enemy character are instantly defeated.",
                                     2),
                         Character.Side.GOOD,
                         the_map)

    def do_special_ability(self, *args):
        # Instantly kill and be killed
        for arg in args:
            self.noble_sacrifice(arg)

    def noble_sacrifice(self, enemy):
        # Get region with enemy character
        region = self.map.region_with_character(enemy)
        # Destroy enemy character from region.
        # After which, game should check map for defeated characters then remove
        # any defeated character found from player inventory of characters.

        # Remove enemy from region.
        region.characters.remove(enemy)
        # Remove enemy's region.
        enemy.region = None
        # Remove Boromir from region
        region.characters.remove(self)
        self.region = None
        print("Boromir instantly kills " + enemy.name + ", and dies in the process. ")
