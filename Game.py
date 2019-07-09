import Player
import Character
import EvilCharacters
import GoodCharacters
import Region
import Map


class Game:

    def __init__(self, form = None):
        # New form to main window
        self.form = form

        self.characters = []
        self.good_characters = []
        self.evil_characters = []

        self.game_over = False
        self.game_winner = None
        
        self.map = Map.Map()
        self.player_sauron = Player.Player(self.map, "Sauron", Character.Side.EVIL)
        self.player_fellowship = Player.Player(self.map, "Fellowship", Character.Side.GOOD)

        self.strength_card_fellowship = None
        self.strength_card_sauron = None

        # Sauron characters
        self.orcs = EvilCharacters.Orcs(self.map)
        self.shelob = EvilCharacters.Shelob(self.map)
        self.saruman = EvilCharacters.Saruman(self.map)
        self.flying_nazgul = EvilCharacters.FlyingNazgul(self.map)
        self.balrog = EvilCharacters.Balrog(self.map)
        self.warg = EvilCharacters.Warg(self.map)
        self.black_rider = EvilCharacters.BlackRider(self.map)
        self.witch_king = EvilCharacters.WitchKing(self.map)
        self.cave_troll = EvilCharacters.CaveTroll(self.map)

        # Fellowship characters
        self.frodo = GoodCharacters.Frodo(self.map)
        self.pippin = GoodCharacters.Pippin(self.map)
        self.gandalf = GoodCharacters.Gandalf(self.map)
        self.sam = GoodCharacters.Sam(self.map)
        self.legolas = GoodCharacters.Legolas(self.map)
        self.aragorn = GoodCharacters.Aragorn(self.map)
        self.gimli = GoodCharacters.Gimli(self.map)
        self.merry = GoodCharacters.Merry(self.map)
        self.boromir = GoodCharacters.Boromir(self.map)        
        
        self._init_characters()
        
    def _init_characters(self):
        self.characters.append(self.frodo)
        self.characters.append(self.pippin)
        self.characters.append(self.gandalf)
        self.characters.append(self.sam)
        self.characters.append(self.legolas)
        self.characters.append(self.aragorn)
        self.characters.append(self.gimli)
        self.characters.append(self.merry)
        self.characters.append(self.boromir)

        self.good_characters.append(self.frodo)
        self.good_characters.append(self.pippin)
        self.good_characters.append(self.gandalf)
        self.good_characters.append(self.sam)
        self.good_characters.append(self.legolas)
        self.good_characters.append(self.aragorn)
        self.good_characters.append(self.gimli)
        self.good_characters.append(self.merry)
        self.good_characters.append(self.boromir)

        self.characters.append(self.orcs)
        self.characters.append(self.shelob)
        self.characters.append(self.saruman)
        self.characters.append(self.flying_nazgul)
        self.characters.append(self.balrog)
        self.characters.append(self.warg)
        self.characters.append(self.black_rider)
        self.characters.append(self.witch_king)
        self.characters.append(self.cave_troll)

        self.evil_characters.append(self.orcs)
        self.evil_characters.append(self.shelob)
        self.evil_characters.append(self.saruman)
        self.evil_characters.append(self.flying_nazgul)
        self.evil_characters.append(self.balrog)
        self.evil_characters.append(self.warg)
        self.evil_characters.append(self.black_rider)
        self.evil_characters.append(self.witch_king)
        self.evil_characters.append(self.cave_troll)

        self.player_fellowship.receive_characters_init(self.good_characters)
        self.player_sauron.receive_characters_init(self.evil_characters)

    @property
    def region_with_battle_event(self) -> Region:
        """
        If region with good and bad player, return region.
        :return: Region with conflict.
        """
        # for region in self.map.regions:
        for k, v in self.map.regions.items():
            if v.contains_evil_characters and v.contains_good_characters:
                return v

    @property
    def exists_region_with_battle_event(self) -> bool:
        """
        Returns True if exists a region with sauron and fellowship character in same region.
        :return: True if battle event exists, False otherwise.
        """
        found = False
        for k, v in self.map.regions.items():
            if v.contains_evil_characters and v.contains_good_characters:
                found = True
                break
        return found

    def get_character(self, name: str) -> Character:
        """
        Get character.
        :param name: Name (str) of character to get.
        :return: (Character) if found, None if not.
        """
        for character in self.characters:
            if name == character.name:
                return character

        return None

    def get_region(self, name: str) -> Region:
        """
        Get region.
        :param name: Name (str) of region to get
        :return: Character if found, None if not.
        """
        for region in self.map.regions:
            if name == region:
                return self.map.regions[name]

        return None

    def battle(self, character_fellowship: Character, character_sauron: Character):
        """
        Handle battle between characters. Handle's character specials. Gets player strength cards.
        :param character_fellowship:
        :param character_sauron:
        :return:
        """
        self.form.msg("Battle initiating between " + character_fellowship.name + "(Strength " +
                      str(character_fellowship.strength) + ") " + " and " + character_sauron.name +
                      "(Strength " + str(character_sauron.strength) + "). ")

        # Clear old strength card values.
        self.strength_card_sauron = None
        self.strength_card_fellowship = None

        if character_sauron.name != "Warg":
            # Handle character's specials.
            potential_character = self.handle_specials(character_fellowship, character_sauron)

            if potential_character:
                # Character fellowship replaced in battle during handle_specials().
                character_fellowship = potential_character

            if character_fellowship.region != character_sauron.region:
                # The two characters which entered battle no longer occupy same region.
                # Possible retreat scenario.
                if character_sauron.region.conflict_exists:
                    # There is still a fellowship character in sauron character region after retreat occurred.
                    # Sauron character must now engage other fellowship character in its region.
                    # Get new fellowship character to be battled.
                    new_character_fellowship = character_sauron.region.get_fellowship_character()
                    # Do battle with this character.
                    self.battle(new_character_fellowship, character_sauron)
                    return
            else:
                # No retreat detected. First, handle instant kills.
                if self.handle_instant_kills(character_fellowship, character_sauron):
                    # Instant kill used, end battle here.
                    return
                # Do battle traditional style.
                else:
                    # ---Player battle starts here after special ability---
                    # Have players choose strength cards.
                    self.decide_cards()
                    # Decide victor.
                    self.decide_victor(character_fellowship, character_sauron)
        else:
            # character name == "Warg"
            # ---Player battle starts here after special ability---
            # Have players choose strength cards.
            self.decide_cards()
            # Decide victor.
            self.decide_victor(character_fellowship, character_sauron)

    def handle_instant_kills(self, character_fellowship:Character, character_sauron:Character)-> bool:
        """
        Handles any instant kill scenarios.
        :param character_fellowship:
        :param character_sauron:
        :return: True if instant kill applied, False otherwise.
        """
        if character_fellowship.name == "Legolas" and character_sauron.name == "Flying Nazgul":
            self.form.msg(character_fellowship.name + " special activated. ")
            self.form.msg(character_fellowship.special_text)
            self.delete_character(character_sauron)
            return True
        elif character_fellowship.name == "Gimli" and character_sauron.name == "Orcs":
            self.form.msg(character_fellowship.name + " special activated. ")
            self.delete_character(character_sauron)
            return True
        elif character_fellowship.name == "Merry" and character_sauron.name == "Witch King":
            self.form.msg(character_fellowship.name + " special activated. ")
            self.delete_character(character_sauron)
            return True
        elif character_sauron.name == "Balrog" and character_sauron.region is self.map.regions["Moria"]:
            self.form.msg(character_sauron.name + " special activated. ")
            self.delete_character(character_fellowship)
            return True
        else:
            return False

    def decide_cards(self):
        # Choose cards
        # If no cards playable (saruman special)
        if self.strength_card_sauron != 0 or self.strength_card_fellowship != 0:
            # If not already set
            if not self.strength_card_fellowship:
                self.strength_card_fellowship = self.player_fellowship.choose_card()
            if not self.strength_card_sauron:
                self.strength_card_sauron = self.player_sauron.choose_card()

    def decide_victor(self, character_fellowship: Character, character_sauron: Character):
        # Decide victor
        strength_fellowship = self.strength_card_fellowship + character_fellowship.strength
        strength_sauron = self.strength_card_sauron + character_sauron.strength

        # Cave Troll special
        if character_sauron.name == "Cave Troll":
            strength_sauron -= self.strength_card_sauron

        self.form.msg(character_fellowship.name + " strength (" + str(strength_fellowship) + "). ")
        self.form.msg(character_sauron.name + " strength (" + str(strength_sauron) + "). ")

        if strength_fellowship > strength_sauron:
            # Fellowship wins.
            self.form.msg("Fellowship wins battle. " + character_fellowship.name + " defeated " +
                  character_sauron.name + ". ")
            self.delete_character(character_sauron)
            pass
        elif strength_fellowship < strength_sauron:
            # Sauron wins.
            self.form.msg("Sauron wins battle. " + character_sauron.name + " defeated " + character_fellowship.name + ". ")
            if character_fellowship.name == "Frodo":
                self.game_over = True
                self.game_winner = self.player_sauron
            if character_sauron.name == "Shelob":
                # Shelob special, return her to Gondor.
                self.form.msg("Special activated. " + character_sauron.special_text)
                self.shelob.move(self.map.regions["Gondor"])
            self.delete_character(character_fellowship)
            pass
        else:
            # Tie
            self.form.msg("Tie resulted. ")
            self.form.msg("Both characters defeated. ")
            # Delete both characters from their player's lists
            self.delete_character(character_fellowship)
            self.delete_character(character_sauron)

    def choose_character_region(self, chosen_character: Character) -> Region:
        """
        Provides text info for user input when choosing which region to move character to.
        :param chosen_character: (Character) which is moving.
        :return: (Region) chosen.
        """
        # Get character's potential move coordinates
        list_of_potential_moves = chosen_character.see_potential_moves()

        # If there are potential moves
        if list_of_potential_moves:
            self.form.msg("Potential regions to move " + chosen_character.name + ": ")
            i = 0

            # Show region names for received coordinates
            for coordination in list_of_potential_moves:
                the_region = self.map.positions[tuple(coordination)]
                self.form.msg(str(i) + " : " + the_region.__str__())
                i += 1
            try:
                # --SCAFFOLD--
                # choice = 0
                choice = int(input("Choose region to move to."))
                # -
                try:
                    for i in range(len(list_of_potential_moves)):
                        if choice == i:
                            return self.map.positions[tuple(list_of_potential_moves[i])]
                    # if choice == 0:
                    #     return self.map.positions[tuple(list_of_potential_moves[0])]
                    # elif choice == 1:
                    #     return self.map.positions[tuple(list_of_potential_moves[1])]
                except Exception as ex:
                    self.form.msg("Error during chosen character. " + str(ex))
            except Exception as ex:
                self.form.msg("Error during chosen character. " + str(ex))

    def handle_specials(self, character_fellowship: Character, character_sauron: Character) -> Character:
        # Do special ability.
        if character_fellowship.name == "Gandalf":
            chosen_card = character_fellowship.do_special_ability(self.player_sauron)
            if chosen_card:
                self.strength_card_sauron = chosen_card
        elif character_fellowship.name == "Frodo":
            retreated = character_fellowship.do_special_ability(character_sauron)
            if not retreated:
                replace = self.sam.do_special_ability(character_sauron)
                if replace:
                    # Replace Frodo with Sam
                    character_fellowship = self.sam
                    return character_fellowship
            else:
                # Frodo retreated, restart everything?
                return
        else:
            character_fellowship.do_special_ability(character_sauron)

        if character_sauron.name == "Saruman":
            no_cards_played = character_sauron.do_special_ability(character_fellowship)
            if no_cards_played:
                # Prevent cards from being played
                # 0 to cards?
                self.strength_card_fellowship = 0
                self.strength_card_sauron = 0
        else:
            # If battle not already resolved, do sauron special ability
            if self.map.exists_conflict:
                character_sauron.do_special_ability(character_fellowship)

    def player_turn(self, player, character, region) -> bool:
        """
        To be called by FormLOTR when player pushes button to make move.
        :param player: Player making the move.
        :param character: Character being moved. Chosen by Player.
        :param region: Region being moved to. Chosen by Player.
        :return: Success or fail (bool).
        """
        #TODO : implement
        if player.side == Character.Side.EVIL:
            return self.bad_player_turn(character, region)
        else:
            return self.good_player_turn(character, region)

    # TODO : Make this callable by self.player turn()
    def good_player_turn(self, character: Character, region: Region):
        """
        Good player chooses which character to move and which region to move to.
        Then moves character to region.
        :return: Region moved to.
        """
        # Move character to region.
        self.player_fellowship.move_character(character, region)

        # Check for first win condition.
        if character.region.name == "Mordor":
            self.game_over = True
            self.game_winner = self.player_fellowship
            return
        if self.region_with_battle_event:
            # Get the info necessary to call battle(), then call it.
            self.form.msg("Battle imminent. " + character.name + " attacking. ")
            region_with_battle = self.region_with_battle_event
            # If region contains more than one enemy, choose which to fight.
            if len(region_with_battle.characters) > 2:
                self.form.msg("Choose which enemy to fight. ")
                print_str = ""
                for enemy in region_with_battle.characters:
                    if enemy.side == Character.Side.EVIL:
                        print_str += enemy.name + " "
                self.form.msg(print_str)
                # --SCAFFOLD--
                # choice = "Saruman"
                choice = str(input())
                # -
                for enemy in region_with_battle.characters:
                    if choice.lower() == enemy.name.lower():
                        self.form.msg("(" + choice + ") chosen. ")
                        self.battle(character, enemy)
                        break
                # else:
                #     # Chosen enemy not found.
                #     raise ValueError("Error during Game good_player_turn(). Chosen enemy not found. ")
            elif len(region_with_battle.characters) > 1:
                self.form.msg("One enemy in region. ")
                # Region contains just one enemy
                # Get enemy from region to do battle with.
                enemy = region_with_battle.get_sauron_character()
                if enemy:
                    # Enter battle with enemy sauron character
                    self.battle(character, enemy)
            else:
                raise ValueError("Error getting sauron character returned from region in "
                                 "Game.get_enemy_to_battle().")
            pass
        self.form.msg("\n")

    # TODO: Make this callable by self.player turn()
    def bad_player_turn(self, character: Character, region: Region) -> bool:
        """
        Moves character to region.
        :return: Success or fail (bool)
        """
        # Move character to region.
        move_success = self.player_sauron.move_character(character, region)

        # If moved into enemy territory
        if self.region_with_battle_event:
            self.form.msg("Battle imminent. " + character.name + " attacking. ")
            region_with_battle = self.region_with_battle_event
            # If region contains more than one enemy, choose which to fight.
            if len(region_with_battle.characters) > 2:
                self.form.msg("Choose which enemy to fight. ")
                print_str = ""
                for enemy in region_with_battle.characters:
                    if enemy.side == Character.Side.GOOD:
                        print_str += enemy.name + " "
                # --SCAFFOLD--
                choice = region_with_battle.characters[0].name
                # choice = str(input(print_str))
                # -
                for enemy in region_with_battle.characters:
                    if choice.lower() == enemy.name.lower():
                        # Note - order of parameters here matters.
                        self.form.msg("(" + choice + ") chosen. ")
                        self.battle(enemy, character)
                        break
                # else:
                #     # Chosen enemy not found.
                #     raise ValueError("Error during Game good_player_turn(). Chosen enemy not found. ")
            elif len(region_with_battle.characters) > 1:
                self.form.msg("One enemy in region. ")
                # Region contains just one enemy
                # Get enemy from region to do battle with.
                enemy = region_with_battle.get_fellowship_character()
                if enemy:
                    # Enter battle with enemy sauron character
                    self.battle(enemy, character)
            else:
                raise ValueError("Error getting sauron character returned from region in "
                                 "Game.get_enemy_to_battle().")
            pass
        return move_success

    def play_game(self):
        # Board setup
        self.player_fellowship.choose_starting_positions()
        self.player_sauron.choose_starting_positions()

        self.form.msg("\nGame starting. ")
        while not self.game_over:
            self.good_player_turn()
            self.bad_player_turn()
            # Sauron win condition if 3 characters in the shire
            if self.map.regions["The Shire"].contains_three_evil_characters:
                self.game_over = True
                self.game_winner = self.player_sauron

    def delete_character(self, character: Character):
        # Delete character in player's inventory
        if character.side == Character.Side.GOOD:
            self.player_fellowship.characters.remove(character)
        else:
            self.player_sauron.characters.remove(character)
        # Delete character in region in map.
        character_region = self.map.region_with_character(character)
        if character_region:
            character_region.characters.remove(character)
        # Delete region in character
        character.region = None
        self.form.msg(character.name + " has been slain. ")

    def spawn_character(self, character: Character, region: Region):
        character.move(region)