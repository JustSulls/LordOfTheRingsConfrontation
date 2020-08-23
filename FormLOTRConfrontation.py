import PySide2.QtWidgets
import PySide2.QtCore
import PySide2.QtGui
import Game
import Character
import Region
import random


class FormLOTRConfrontation(PySide2.QtWidgets.QMainWindow):

    def __init__(self):
        PySide2.QtWidgets.QMainWindow.__init__(self)
        # Button group good characters
        self.group_good_character_buttons = PySide2.QtWidgets.QButtonGroup()
        # Button group good characters
        self.group_evil_character_buttons = PySide2.QtWidgets.QButtonGroup()
        # Button group good characters
        self.group_region_buttons = PySide2.QtWidgets.QButtonGroup()

        def setup_game_windows(self):

            def init_main_layouts(self):
                # QGridLayout for central widget QGraphicsView
                self.main_grid_layout = PySide2.QtWidgets.QGridLayout()

                # To hold good character buttons
                self.sub_grid_layout_0 = PySide2.QtWidgets.QGridLayout()

                # To hold map and regions and top buttons
                self.sub_grid_layout_1 = PySide2.QtWidgets.QGridLayout()

                # To hold map
                self.sub_grid_layout_0_0 = PySide2.QtWidgets.QGridLayout()

                # To hold region layouts
                self.sub_grid_layout_1_0 = PySide2.QtWidgets.QGridLayout()

                # To hold regions
                self.sub_box_layout_1_0_0_0 = PySide2.QtWidgets.QHBoxLayout()

                # To hold more regions
                self.sub_box_layout_1_0_1_0 = PySide2.QtWidgets.QHBoxLayout()

                # To hold instructions text
                self.sub_box_layout_1_0_2_0 = PySide2.QtWidgets.QHBoxLayout()

                # To hold evil characters
                self.sub_grid_layout_2 = PySide2.QtWidgets.QGridLayout()

                # Insert into regions/text layout
                self.sub_grid_layout_1_0.addLayout(self.sub_box_layout_1_0_0_0, 0, 0)
                self.sub_grid_layout_1_0.addLayout(self.sub_box_layout_1_0_1_0, 1, 0)
                # self.sub_grid_layout_1_0.addLayout(self.sub_box_layout_1_0_2_0, 2, 0, 4)
                # EDIT --
                self.sub_grid_layout_1_0.addLayout(self.sub_box_layout_1_0_2_0, 2, 0)
                # EDIT end --
                # Insert into center layout
                self.sub_grid_layout_1.addLayout(self.sub_grid_layout_0_0, 0, 0)
                self.sub_grid_layout_1.addLayout(self.sub_grid_layout_1_0, 1, 0)
                # Insert sub layouts into main layout
                self.main_grid_layout.addLayout(self.sub_grid_layout_0, 0, 0)
                self.main_grid_layout.addLayout(self.sub_grid_layout_1, 0, 1)
                self.main_grid_layout.addLayout(self.sub_grid_layout_2, 0, 2)
            # Set layout for main window
            init_main_layouts(self)

            def init_main_buttons(self):
                def init_character_buttons(self):
                    def init_good_character_buttons(self):
                        # Frodo button
                        self.button_frodo = PySide2.QtWidgets.QRadioButton("Frodo")
                        self.button_frodo.setChecked(True)
                        self.group_good_character_buttons.addButton(self.button_frodo, 1)

                        # Pippin button
                        self.button_pippin = PySide2.QtWidgets.QRadioButton("Pippin")
                        self.group_good_character_buttons.addButton(self.button_pippin, 2)

                        # Gandalf button
                        self.button_gandalf = PySide2.QtWidgets.QRadioButton("Gandalf")
                        self.group_good_character_buttons.addButton(self.button_gandalf, 3)

                        # Sam button
                        self.button_sam = PySide2.QtWidgets.QRadioButton("Sam")
                        self.group_good_character_buttons.addButton(self.button_sam, 4)

                        # Legolas button
                        self.button_legolas = PySide2.QtWidgets.QRadioButton("Legolas")
                        self.group_good_character_buttons.addButton(self.button_legolas, 5)

                        # Aragorn button
                        self.button_aragorn = PySide2.QtWidgets.QRadioButton("Aragorn")
                        self.group_good_character_buttons.addButton(self.button_aragorn, 6)

                        # Gimli button
                        self.button_gimli = PySide2.QtWidgets.QRadioButton("Gimli")
                        self.group_good_character_buttons.addButton(self.button_gimli, 7)

                        # Merry button
                        self.button_merry = PySide2.QtWidgets.QRadioButton("Merry")
                        self.group_good_character_buttons.addButton(self.button_merry, 8)

                        # Boromir button
                        self.button_boromir = PySide2.QtWidgets.QRadioButton("Boromir")
                        self.group_good_character_buttons.addButton(self.button_boromir, 9)
                    # Create good character push buttons
                    init_good_character_buttons(self)

                    def init_evil_character_buttons(self):
                        # Orcs button
                        self.button_orcs = PySide2.QtWidgets.QRadioButton("Orcs")
                        self.group_evil_character_buttons.addButton(self.button_orcs, 1)

                        # Shelob button
                        self.button_shelob = PySide2.QtWidgets.QRadioButton("Shelob")
                        self.group_evil_character_buttons.addButton(self.button_shelob, 2)

                        # Saruman button
                        self.button_saruman = PySide2.QtWidgets.QRadioButton("Saruman")
                        self.group_evil_character_buttons.addButton(self.button_saruman, 3)

                        # Flying Nazgul button
                        self.button_flying_nazgul = PySide2.QtWidgets.QRadioButton("Flying Nazgul")
                        self.group_evil_character_buttons.addButton(self.button_flying_nazgul, 4)

                        # Balrog button
                        self.button_balrog = PySide2.QtWidgets.QRadioButton("Balrog")
                        self.group_evil_character_buttons.addButton(self.button_balrog, 5)

                        # Warg button
                        self.button_warg = PySide2.QtWidgets.QRadioButton("Warg")
                        self.group_evil_character_buttons.addButton(self.button_warg, 6)

                        # Black rider button
                        self.button_black_rider = PySide2.QtWidgets.QRadioButton("Black Rider")
                        self.group_evil_character_buttons.addButton(self.button_black_rider, 7)

                        # Witch King button
                        self.button_witch_king = PySide2.QtWidgets.QRadioButton("Witch King")
                        self.group_evil_character_buttons.addButton(self.button_witch_king, 8)

                        # Cave troll button
                        self.button_cave_troll = PySide2.QtWidgets.QRadioButton("Cave Troll")
                        self.group_evil_character_buttons.addButton(self.button_cave_troll, 9)
                    # Create evil character push buttons
                    init_evil_character_buttons(self)
                # Create character push buttons
                init_character_buttons(self)

                def init_region_buttons(self):
                    # Mordor button
                    self.button_mordor = PySide2.QtWidgets.QRadioButton("Mordor")
                    self.group_region_buttons.addButton(self.button_mordor)

                    # Gondor button
                    self.button_gondor = PySide2.QtWidgets.QRadioButton("Gondor")
                    self.group_region_buttons.addButton(self.button_gondor)

                    # Rohan button
                    self.button_rohan = PySide2.QtWidgets.QRadioButton("Rohan")
                    self.group_region_buttons.addButton(self.button_rohan)

                    # Gap of Rohan button
                    self.button_gap_of_rohan = PySide2.QtWidgets.QRadioButton("Gap of Rohan")
                    self.group_region_buttons.addButton(self.button_gap_of_rohan)

                    # Dagorlad button
                    self.button_dagorlad = PySide2.QtWidgets.QRadioButton("Dagorlad")
                    self.group_region_buttons.addButton(self.button_dagorlad)

                    # Fangorn button
                    self.button_fangorn = PySide2.QtWidgets.QRadioButton("Fangorn")
                    self.group_region_buttons.addButton(self.button_fangorn)

                    # Moria button
                    self.button_moria = PySide2.QtWidgets.QRadioButton("Moria")
                    self.group_region_buttons.addButton(self.button_moria)

                    # Endewaith button
                    self.button_endewaith = PySide2.QtWidgets.QRadioButton("Endewaith")
                    self.group_region_buttons.addButton(self.button_endewaith)

                    # Mirkwood button
                    self.button_mirkwood = PySide2.QtWidgets.QRadioButton("Mirkwood")
                    self.group_region_buttons.addButton(self.button_mirkwood)

                    # Misty Mountains buton
                    self.button_misty_mountains = PySide2.QtWidgets.QRadioButton("Misty Mountains")
                    self.button_misty_mountains.setChecked(True)
                    self.group_region_buttons.addButton(self.button_misty_mountains)

                    # Eregion button
                    self.button_eregion = PySide2.QtWidgets.QRadioButton("Eregion")
                    self.group_region_buttons.addButton(self.button_eregion)

                    # Cardolan button
                    self.button_cardolan = PySide2.QtWidgets.QRadioButton("Cardolan")
                    self.group_region_buttons.addButton(self.button_cardolan)

                    # High pass button
                    self.button_high_pass = PySide2.QtWidgets.QRadioButton("High Pass")
                    self.group_region_buttons.addButton(self.button_high_pass)

                    # Rhudaur button
                    self.button_rhudaur = PySide2.QtWidgets.QRadioButton("Rhudaur")
                    self.group_region_buttons.addButton(self.button_rhudaur)

                    # Arthedain button
                    self.button_arthedain = PySide2.QtWidgets.QRadioButton("Arthedain")
                    self.group_region_buttons.addButton(self.button_arthedain)

                    # The Shire button
                    self.button_the_shire = PySide2.QtWidgets.QRadioButton("The Shire")
                    self.group_region_buttons.addButton(self.button_the_shire)
                # Create region push buttons
                init_region_buttons(self)

                def init_text_box(self):
                    # Add text line edit for instructions?
                    self.text_box = PySide2.QtWidgets.QLabel()
                    size_policy = PySide2.QtWidgets.QSizePolicy(PySide2.QtWidgets.QSizePolicy.Maximum,
                                                                PySide2.QtWidgets.QSizePolicy.Maximum)

                    self.text_box.setSizePolicy(size_policy)
                    self.text_box.setAlignment(PySide2.QtCore.Qt.AlignHCenter)
                # Init text box widget
                init_text_box(self)

                def init_player_commands(self):
                    self.button_command_move = PySide2.QtWidgets.QPushButton("Command Move")
                    self.button_command_move.setDefault(True)
                    self.button_command_move.setFocus()
                    self.button_command_move.clicked.connect(self.command_move_clicked)
                init_player_commands(self)
            # Create buttons and connect for main window
            init_main_buttons(self)

            def set_up_main_buttons(self):
                def set_up_evil_buttons(self):
                    # Orcs button
                    self.sub_grid_layout_2.addWidget(self.button_orcs)

                    # Shelob button
                    self.sub_grid_layout_2.addWidget(self.button_shelob)

                    # Saruman button
                    self.sub_grid_layout_2.addWidget(self.button_saruman)

                    # Flying Nazgul button
                    self.sub_grid_layout_2.addWidget(self.button_flying_nazgul)

                    # Balrog button
                    self.sub_grid_layout_2.addWidget(self.button_balrog)

                    # Warg button
                    self.sub_grid_layout_2.addWidget(self.button_warg)

                    # Black Rider button
                    self.sub_grid_layout_2.addWidget(self.button_black_rider)

                    # Witch King button
                    self.sub_grid_layout_2.addWidget(self.button_witch_king)

                    # Cave Troll button
                    self.sub_grid_layout_2.addWidget(self.button_cave_troll)
                # Add evil character buttons to layout
                set_up_evil_buttons(self)

                def set_up_good_buttons(self):
                    # Frodo button
                    self.sub_grid_layout_0.addWidget(self.button_frodo)

                    # Pippin button
                    self.sub_grid_layout_0.addWidget(self.button_pippin)

                    # Gandalf button
                    self.sub_grid_layout_0.addWidget(self.button_gandalf)

                    # Sam button
                    self.sub_grid_layout_0.addWidget(self.button_sam)

                    # Legolas button
                    self.sub_grid_layout_0.addWidget(self.button_legolas)

                    # Aragorn button
                    self.sub_grid_layout_0.addWidget(self.button_aragorn)

                    # Gimli button
                    self.sub_grid_layout_0.addWidget(self.button_gimli)

                    # merry button
                    self.sub_grid_layout_0.addWidget(self.button_merry)

                    # Boromir button
                    self.sub_grid_layout_0.addWidget(self.button_boromir)
                # Add good character buttons to layout
                set_up_good_buttons(self)

                def set_up_region_buttons(self):
                    # Mordor region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_mordor)

                    # Gondor region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_gondor)

                    # Rohan region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_rohan)

                    # Gap of Rohan region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_gap_of_rohan)

                    # Dagorlad region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_dagorlad)

                    # Fangorn region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_fangorn)

                    # Moria region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_moria)

                    # Endewaith region button
                    self.sub_box_layout_1_0_0_0.addWidget(self.button_endewaith)

                    # Mirkwood region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_mirkwood)

                    # Misty Mountains region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_misty_mountains)

                    # Eregion region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_eregion)

                    # Cardolan region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_cardolan)

                    # High Pass region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_high_pass)

                    # Rhudaur region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_rhudaur)

                    # Arthedain region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_arthedain)

                    # The Shire region button
                    self.sub_box_layout_1_0_1_0.addWidget(self.button_the_shire)
                # Add region buttons to layout
                set_up_region_buttons(self)

                def set_up_text_box(self):
                    self.sub_box_layout_1_0_2_0.addWidget(self.text_box)
                # Add text box to layout
                set_up_text_box(self)

                def set_up_command_buttons(self):
                    self.sub_box_layout_1_0_2_0.addWidget(self.button_command_move)
                # Add command buttons to layout
                set_up_command_buttons(self)
            # Add widgets to layout
            set_up_main_buttons(self)

            def init_start_layouts(self):
                # QGridLayout for central widget QGraphicsView
                self.setup_start_grid_layout = PySide2.QtWidgets.QGridLayout()
            # Init setup main window layout
            init_start_layouts(self)

            def init_start_buttons(self):
                self.button_select_good = PySide2.QtWidgets.QPushButton("Good")
                self.button_select_evil = PySide2.QtWidgets.QPushButton("Evil")

                # Text box for start window (choose player)
                self.text_box_start = PySide2.QtWidgets.QLabel()
                size_policy = PySide2.QtWidgets.QSizePolicy(PySide2.QtWidgets.QSizePolicy.Maximum,
                                                            PySide2.QtWidgets.QSizePolicy.Maximum)

                self.text_box_start.setSizePolicy(size_policy)
                self.text_box_start.setAlignment(PySide2.QtCore.Qt.AlignHCenter)
            # Start window buttons
            init_start_buttons(self)

            def set_up_start_buttons(self):
                self.setup_start_grid_layout.addWidget(self.button_select_good)
                self.button_select_good.clicked.connect(self.select_good_clicked)
                self.setup_start_grid_layout.addWidget(self.button_select_evil)
                self.button_select_evil.clicked.connect(self.select_evil_clicked)
                self.setup_start_grid_layout.addWidget(self.text_box_start)
            # Organize layout & connect buttons
            set_up_start_buttons(self)
            pass
        # Set up PySide2 windows
        setup_game_windows(self)

        # Game information
        self.game = Game.Game(self)
        self.map = self.game.map
        self.player_fellowship = self.game.player_fellowship
        self.player_sauron = self.game.player_sauron

        # Start window central widget QGraphicsView
        self.start_window_central_widget_graphics_view = PySide2.QtWidgets.QGraphicsView()

        # Main window central widget will QGraphicsView
        self.central_widget_graphics_view = PySide2.QtWidgets.QGraphicsView()

        def setup_pixmap_middle_earth(self):
            # Setup QPixmap
            pixmap_item = PySide2.QtGui.QPixmap("images/pic_middle_earth.jpg")
            label = PySide2.QtWidgets.QLabel()

            # Put QPixmap in Label
            label.setPixmap(pixmap_item)
            label.setScaledContents(True)
            self.sub_grid_layout_0_0.addWidget(label)
        # Map of middle earth
        setup_pixmap_middle_earth(self)

        self.available_to_spawn_characters = None

        self.graphics_scene_start_window()

    @property
    def character_selected(self) -> Character:
        """
        Gets Character from good/evil_character selected property.
        :return: Character selected depending on side good/evil.
        """
        if Character.Side.GOOD == self.game.player_human_side:
            return self.good_character_selected
        elif Character.Side.EVIL == self.game.player_human_side:
            return self.evil_character_selected
        else:
            return None

    @property
    def evil_character_selected(self) -> Character:
        # Currently selected evil character radio button
        selected_button = self.group_evil_character_buttons.checkedButton()
        # String name of character
        character_name = selected_button.text()
        # Get character
        return self.game.get_character(character_name)

    @property
    def good_character_selected(self) -> Character:
        # Currently selected good character radio button
        selected_button = self.group_good_character_buttons.checkedButton()
        # String name of character
        character_name = selected_button.text()
        # Get character
        return self.game.get_character(character_name)

    @property
    def player_human_side_fellowship(self) -> bool:
        if self.game.player_human.player_side == Character.Side.GOOD:
            return True
        else:
            return False

    @property
    def player_human_side_sauron(self) -> bool:
        if self.game.player_human.player_side == Character.Side.EVIL:
            return True
        else:
            return False

    @property
    def region_selected(self) -> Region:
        # Currently selected region radio button
        selected_region = self.group_region_buttons.checkedButton()
        # String name of character
        region_name = selected_region.text()
        # Get region
        return self.game.get_region(region_name)

    def add_dialogue(self, *args):
        full_txt = ''
        for txt in args:
            full_txt += str(txt)
        self.text_box.setText(self.text_box.text() + "\n" + full_txt)

    def choose_starting_positions(self):
        """

        :return:
        """
        self.new_msg("Choose starting positions. ")
        spawn_place = self.game.get_spawn_region()
        self.add_dialogue(self.game.player_human.name + " chooses four of his characters and places them in "
                          + spawn_place.name + ". ")
        # Disconnect original button command move func call
        self.button_command_move.clicked.disconnect()
        # Make command move button do the spawn for choose_starting_positions()
        self.button_command_move.clicked.connect(self.command_spawn_move_clicked)
        # Update button's name
        self.button_command_move.setText("Spawn Character")
        # Disable Region buttons
        for button in self.group_region_buttons.buttons():
            button.setDisabled(True)

        # Set available to choose characters list to all player's characters to be spawned.
        self.available_to_spawn_characters = self.game.player_human.characters

    def command_move_clicked(self):
        # Get selected region
        region_moved_to = self.region_selected
        # Get selected character
        moving_character = self.character_selected
        # Make move happen
        try:
            self.game.player_turn(self.game.player_human, moving_character, region_moved_to)
        except Exception as e:
            print("Problem during command move clicked func.")
            print(e)
        pass

    def command_spawn_move_clicked(self):
        """
        Moves selected character to selected region. If spawning complete,
        spawns opponents characters, then calls start_game().
        :return:
        """
        # Get region to spawn to
        spawn_region = self.game.get_spawn_region()

        # Get player's character choice
        character_choice = self.character_selected

        # Validate
        if spawn_region is not None and character_choice.region is None:
            # Valid choices probably. # TODO: Confirm this works.
            # Do spawn
            try:
                self.game.spawn_character(character_choice, spawn_region)
                self.new_msg(character_choice.name + " spawned at " + spawn_region.name + ". ")
                # Update character list, call next phase if done choosing
                self.available_to_spawn_characters.remove(character_choice)
            except Exception as ex:
                print("Invalid choice. Need to implement error handling during spawn choices. " + ex.__str__())
        else:
            # Not valid choice, try again
            self.new_msg("Invalid choice... try again.")

        # Disable button for character already chosen.
        if self.player_human_side_sauron:
            for button_character in self.group_evil_character_buttons.buttons():
                if button_character.text() == character_choice.name:
                    button_character.setDisabled(True)
                    self.highlight_next_available_character()
        else:
            for button_character in self.group_good_character_buttons.buttons():
                if button_character.text() == character_choice.name:
                    button_character.setDisabled(True)
                    self.highlight_next_available_character()

        # Check if spawning complete
        if not self.available_to_spawn_characters:
            # Spawning complete
            # No characters left in available to spawn characters list.
            self.button_command_move.clicked.disconnect()
            # Make command move button do the regular move function
            self.button_command_move.clicked.connect(self.command_move_clicked)
            self.button_command_move.setText("Move")
            # Next phase
            self.game.do_enemy_ai_spawn()
            # After all characters now spawned, may start game.
            # -- STARTING REGULAR GAME HERE --
            self.start_game()
        else:
            # Do prompt for next character to spawn to region
            spawn_place = self.game.get_spawn_region()
            self.add_dialogue("Choose character to spawn to "
                              + spawn_place.name + ". ")
        # Refresh screen
        self.hide()
        self.show()

    def disable_non_player_buttons(self):
        if self.game.player_computer_side == Character.Side.GOOD:
            for button in self.group_good_character_buttons.buttons():
                button.setDisabled(True)
        if self.game.player_computer_side == Character.Side.EVIL:
            for button in self.group_evil_character_buttons.buttons():
                button.setDisabled(True)

    def graphics_scene_start_window(self):
        """
        QGraphicsScene to QGraphicsView central widget of self:QMainWindow
        Also, QGraphicsView central widget Layout to start_grid_layout
        :return:
        """
        # Create Graphics scene
        scene_start = PySide2.QtWidgets.QGraphicsScene()

        # Add QGraphicsScene to GraphicsView (QMainwindow's central widget)
        # self.central_widget_graphics_view.setScene(scene_main)
        self.start_window_central_widget_graphics_view.setScene(scene_start)

        # Set MainWindow's central widget
        self.setCentralWidget(self.start_window_central_widget_graphics_view)

        # Set central widget's (GraphicsView's) layout
        self.start_window_central_widget_graphics_view.setLayout(self.setup_start_grid_layout)

        # Size window to 50% available screen space
        self.resize(PySide2.QtWidgets.QDesktopWidget.availableGeometry(
            PySide2.QtWidgets.QDesktopWidget()).size() * 0.5)

        self.msg_start("Welcome to The Lord Of the Rings Confrontation.")
        self.msg_start("Select your side: Good, Evil")

        self.show()

    def graphics_scene_main_window(self):
        """
        QGraphicsScene to QGraphicsView central widget of self:QMainWindow
        Also, QGraphicsView central widget Layout to main_grid_layout
        :return:
        """
        # Create Graphics scene
        scene_main = PySide2.QtWidgets.QGraphicsScene()

        # Add QGraphicsScene to GraphicsView (Mainwindow's central widget)
        self.central_widget_graphics_view.setScene(scene_main)

        # Set MainWindow's central widget
        self.setCentralWidget(self.central_widget_graphics_view)

        # Set central widget's (GraphicsView's) layout
        self.central_widget_graphics_view.setLayout(self.main_grid_layout)

        # Size window to 70% available screen space
        self.resize(PySide2.QtWidgets.QDesktopWidget.availableGeometry(
            PySide2.QtWidgets.QDesktopWidget()).size() * 0.8)

        def move_main_window_center():
            desktop = PySide2.QtWidgets.QApplication.desktop()
            screen_geometry = desktop.screenGeometry(self)
            x = (screen_geometry.width() - self.width()) / 2
            y = (screen_geometry.height() - self.height()) / 2
            self.move(x, y)
        # Move window to center screen
        move_main_window_center()

        self.show()

    def highlight_next_available_character(self):
        if self.player_human_side_fellowship:
            for btn in self.group_good_character_buttons.buttons():
                if btn.isEnabled():
                    btn.toggle()
                    break
        else:
            for btn in self.group_evil_character_buttons.buttons():
                if btn.isEnabled():
                    btn.toggle()
                    break

    def msg_start(self, *args: str):
        txt = self.text_box_start.text()
        txt += "\n"
        for arg in args:
            txt += arg
        self.text_box_start.setText(txt)

    def new_msg(self, *args: str):
        txt = ""
        for arg in args:
            txt += arg
        self.text_box.setText(txt)

    def prompt_user_which_card_to_choose(self, cards) -> int:
        dialog = PySide2.QtWidgets.QDialog()
        layout = PySide2.QtWidgets.QVBoxLayout()
        for card in cards:
            layout.addWidget(PySide2.QtWidgets.QPushButton(card.__str__()))
        dialog.setLayout(layout)
        pass

    def prompt_user_which_enemy_to_battle(self, *args: str) -> str:
        """
        Takes enemy character names as parameters and prompts user to choose which to battle.
        :param args: String character names to choose from to battle.
        :return: Name of character chosen to battle.
        """
        # dialog = PySide2.QtWidgets.QDialog()
        # layout = PySide2.QtWidgets.QHBoxLayout()
        # for name in args:
        #     layout.addWidget(PySide2.QtWidgets.QRadioButton(name))
        # ok = PySide2.QtWidgets.QPushButton("Ok")
        # layout.addWidget(ok)
        # dialog.setLayout(layout)
        # ok.clicked.connect(dialog.accept)
        # returned = dialog.exec_()sss
        # print("Great successs!")
        def test_dialog_ok(self):
            """Test we can click OK."""

            button = self.dialog.button_box.button(PySide2.QtWidgets.QDialogButtonBox.Ok)
            button.click()
            result = self.dialog.result()
            self.assertEqual(result, PySide2.QtWidgets.QDialog.Accepted)
        test_dialog_ok(self)
        pass

    def select_evil_clicked(self):
        """
        One of two possibilities for first button push. Starts game with
        player as evil. Moves to setup_game().
        :return:
        """
        self.game.player_human = self.game.player_sauron
        self.game.player_computer = self.game.player_fellowship
        self.new_msg("Evil player chosen. ")
        self.setup_game()

    def select_good_clicked(self):
        """
        One of two possibilities for first button push. Starts game with
        player as evil. Moves to setup_game().
        :return:
        """
        self.game.player_human = self.game.player_fellowship
        self.game.player_computer = self.game.player_sauron
        self.new_msg("Good player chosen. ")
        self.setup_game()

    def setup_game(self):
        """
        Disables opposing player buttons, calls choose_starting_positions().
        :return:
        """
        self.graphics_scene_main_window()
        # Disable non player buttons (done after player chosen)
        self.disable_non_player_buttons()
        # Have player choose starting positions for his characters
        #self.choose_starting_positions()
        self.scaffolding()

    def start_game(self):
        # Game starts with AI player's turn
        self.new_msg("Game starts with AI player's turn.")
        # TODO: leftoff here
        self.game.do_ai_turn()

    def scaffolding(self):
        # Setup game in order to test do ai turn()
        for i in range(0, 9):
            self.command_spawn_move_clicked()
