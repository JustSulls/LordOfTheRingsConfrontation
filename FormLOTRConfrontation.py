import PySide2.QtWidgets
import PySide2.QtCore
import PySide2.QtGui
import Game
import Character
import Region


class FormLOTRConfrontation(PySide2.QtWidgets.QMainWindow):

    def __init__(self):
        PySide2.QtWidgets.QMainWindow.__init__(self)
        self.human_player = None
        self.computer_player = None

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
                        # TODO: Implement custom radiobutton/abstraction class and include
                        #  each appropriate character from Game
                        # Frodo button
                        self.button_frodo = PySide2.QtWidgets.QRadioButton("Frodo")
                        self.button_frodo.setChecked(True)
                        self.group_good_character_buttons.addButton(self.button_frodo)

                        # Pippin button
                        self.button_pippin = PySide2.QtWidgets.QRadioButton("Pippin")
                        self.group_good_character_buttons.addButton(self.button_pippin)

                        # Gandalf button
                        self.button_gandalf = PySide2.QtWidgets.QRadioButton("Gandalf")
                        self.group_good_character_buttons.addButton(self.button_gandalf)

                        # Sam button
                        self.button_sam = PySide2.QtWidgets.QRadioButton("Sam")
                        self.group_good_character_buttons.addButton(self.button_sam)

                        # Legolas button
                        self.button_legolas = PySide2.QtWidgets.QRadioButton("Legolas")
                        self.group_good_character_buttons.addButton(self.button_legolas)

                        # Aragorn button
                        self.button_aragorn = PySide2.QtWidgets.QRadioButton("Aragorn")
                        self.group_good_character_buttons.addButton(self.button_aragorn)

                        # Gimli button
                        self.button_gimli = PySide2.QtWidgets.QRadioButton("Gimli")
                        self.group_good_character_buttons.addButton(self.button_gimli)

                        # Merry button
                        self.button_merry = PySide2.QtWidgets.QRadioButton("merry")
                        self.group_good_character_buttons.addButton(self.button_merry)

                        # Boromir button
                        self.button_boromir = PySide2.QtWidgets.QRadioButton("Boromir")
                        self.group_good_character_buttons.addButton(self.button_boromir)
                    # Create good character push buttons
                    init_good_character_buttons(self)

                    def init_evil_character_buttons(self):
                        # Orcs button
                        self.button_orcs = PySide2.QtWidgets.QRadioButton("Orcs")
                        self.group_evil_character_buttons.addButton(self.button_orcs)

                        # Shelob button
                        self.button_shelob = PySide2.QtWidgets.QRadioButton("Shelob")
                        self.group_evil_character_buttons.addButton(self.button_shelob)

                        # Saruman button
                        self.button_saruman = PySide2.QtWidgets.QRadioButton("Saruman")
                        self.group_evil_character_buttons.addButton(self.button_saruman)

                        # Flying Nazgul button
                        self.button_flying_nazgul = PySide2.QtWidgets.QRadioButton("Flying Nazgul")
                        self.group_evil_character_buttons.addButton(self.button_flying_nazgul)

                        # Balrog button
                        self.button_balrog = PySide2.QtWidgets.QRadioButton("Balrog")
                        self.group_evil_character_buttons.addButton(self.button_balrog)

                        # Warg button
                        self.button_warg = PySide2.QtWidgets.QRadioButton("Warg")
                        self.group_evil_character_buttons.addButton(self.button_warg)

                        # Black rider button
                        self.button_black_rider = PySide2.QtWidgets.QRadioButton("Black Rider")
                        self.group_evil_character_buttons.addButton(self.button_black_rider)

                        # Witch King button
                        self.button_witch_king = PySide2.QtWidgets.QRadioButton("Witch King")
                        self.group_evil_character_buttons.addButton(self.button_witch_king)

                        # Cave troll button
                        self.button_cave_troll = PySide2.QtWidgets.QRadioButton("Cave Troll")
                        self.group_evil_character_buttons.addButton(self.button_cave_troll)
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
                    # TODO: make sure this is the right way to connect button to func
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

            # TODO : Connect new command button to yet to be implemented command button func.

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

        self.current_character = None
        self.current_region = None

        self.graphics_scene_start_window()

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

        self.handle_game()

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

    def start_game(self):
        self.graphics_scene_main_window()
        # Disable non player buttons (after player chosen)
        if self.human_player == self.player_fellowship:
            # Disable player sauron's character buttons
            for button in self.group_evil_character_buttons.buttons():
                button.setDisabled(True)
        else:
            for button in self.group_good_character_buttons.buttons():
                button.setDisabled(True)

        # Get player first move.
        # TODO: Left off here. Game has started and player chosen. Other player's buttons disabled.

    def handle_game(self):
        """
        Have player choose side.
        :return:
        """
        def choose_player():
            self.msg_start("Welcome to The Lord Of the Rings Confrontation.")
            self.msg_start("Select your side: Good, Evil")

        choose_player()

    def msg(self, *args: str):
        txt = self.text_box.text()
        txt += "\n"
        for arg in args:
            txt += arg
        self.text_box.setText(txt)

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

    def select_evil_clicked(self):
        self.human_player = self.player_sauron
        self.computer_player = self.player_fellowship
        self.new_msg("Evil player chosen. ")
        self.start_game()

    def select_good_clicked(self):
        self.human_player = self.player_fellowship
        self.computer_player = self.player_sauron
        self.new_msg("Good player chosen. ")
        self.start_game()

    def add_dialogue(self, *args):
        full_txt = ''
        for txt in args:
            full_txt += str(txt)
        self.txt_area.setText(self.txt_area.text() + "\n" + full_txt)

    def command_move_clicked(self):
        # Get selected region
        region_moved_to = self.region_selected
        # Get selected character
        moving_character = self.character_selected
        # Make move happen
        try:
            # TODO : Leftoff here, make sure this call works
            self.game.player_turn(self.human_player, moving_character, region_moved_to)
        except Exception as e:
            print("Problem during command move clicked func.")
            print(e)
        pass

    @property
    def player_side(self) -> Character.Side:
        if self.human_player == self.player_fellowship:
            return Character.Side.GOOD
        elif self.human_player == self.player_sauron:
            return Character.Side.EVIL
        else:
            return None

    @property
    def character_selected(self) -> Character:
        if Character.Side.GOOD == self.player_side:
            return self.good_character_selected
        elif Character.Side.EVIL == self.player_side:
            return self.evil_character_selected
        else:
            return None

    @property
    def good_character_selected(self) -> Character:
        # Currently selected good character radio button
        selected_button = self.group_good_character_buttons.checkedButton()
        # String name of character
        character_name = selected_button.text()
        # Get character
        return self.game.get_character(character_name)

    @property
    def evil_character_selected(self) -> Character:
        # Currently selected evil character radio button
        selected_button = self.group_evil_character_buttons.checkedButton()
        # String name of character
        character_name = selected_button.text()
        # Get character
        return self.game.get_character(character_name)

    @property
    def region_selected(self) -> Region:
        # Currently selected region radio button
        selected_region = self.group_region_buttons.checkedButton()
        # String name of character
        region_name = selected_region.text()
        # Get region
        return self.game.get_region(region_name)
