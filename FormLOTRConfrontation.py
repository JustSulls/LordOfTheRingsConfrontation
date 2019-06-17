import PySide2.QtWidgets
import PySide2.QtCore
import PySide2.QtGui
import Game


class FormLOTRConfrontation(PySide2.QtWidgets.QMainWindow):

    def __init__(self):
        PySide2.QtWidgets.QMainWindow.__init__(self)
        self.real_player = None
        self.computer_player = None

        # Set layout for main window
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
            self.sub_grid_layout_1_0.addLayout(self.sub_box_layout_1_0_2_0, 2, 0, 4)
            # Insert into center layout
            self.sub_grid_layout_1.addLayout(self.sub_grid_layout_0_0, 0, 0)
            self.sub_grid_layout_1.addLayout(self.sub_grid_layout_1_0, 1, 0)
            # Insert sub layouts into main layout
            self.main_grid_layout.addLayout(self.sub_grid_layout_0, 0, 0)
            self.main_grid_layout.addLayout(self.sub_grid_layout_1, 0, 1)
            self.main_grid_layout.addLayout(self.sub_grid_layout_2, 0, 2)
        init_main_layouts(self)

        # Init setup main window layout
        def init_start_layouts(self):
            # QGridLayout for central widget QGraphicsView
            self.setup_start_grid_layout = PySide2.QtWidgets.QGridLayout()
        init_start_layouts(self)

        # Board button setup for main window
        def init_main_buttons(self):
            # Create character push buttons
            def init_character_buttons(self):
                # Create good character push buttons
                def init_good_character_buttons(self):
                    # Frodo button
                    self.button_frodo = PySide2.QtWidgets.QPushButton("Frodo")

                    # Pippin button
                    self.button_pippin = PySide2.QtWidgets.QPushButton("Pippin")

                    # Gandalf button
                    self.button_gandalf = PySide2.QtWidgets.QPushButton("Gandalf")

                    # Sam button
                    self.button_sam = PySide2.QtWidgets.QPushButton("Sam")

                    # Legolas button
                    self.button_legolas = PySide2.QtWidgets.QPushButton("Legolas")

                    # Aragorn button
                    self.button_aragorn = PySide2.QtWidgets.QPushButton("Aragorn")

                    # Gimli button
                    self.button_gimli = PySide2.QtWidgets.QPushButton("Gimli")

                    # Merry button
                    self.button_merry = PySide2.QtWidgets.QPushButton("merry")

                    # Boromir button
                    self.button_boromir = PySide2.QtWidgets.QPushButton("Boromir")
                init_good_character_buttons(self)
                
                # Create evil character push buttons
                def init_evil_character_buttons(self):
                    # Orcs button
                    self.button_orcs = PySide2.QtWidgets.QPushButton("Orcs")

                    # Shelob button
                    self.button_shelob = PySide2.QtWidgets.QPushButton("Shelob")

                    # Saruman button
                    self.button_saruman = PySide2.QtWidgets.QPushButton("Saruman")

                    # Flying Nazgul button
                    self.button_flying_nazgul = PySide2.QtWidgets.QPushButton("Flying Nazgul")

                    # Balrog button
                    self.button_balrog = PySide2.QtWidgets.QPushButton("Balrog")

                    # Warg button
                    self.button_warg = PySide2.QtWidgets.QPushButton("Warg")

                    # Black rider button
                    self.button_black_rider = PySide2.QtWidgets.QPushButton("Black Rider")

                    # Witch King button
                    self.button_witch_king = PySide2.QtWidgets.QPushButton("Witch King")

                    # Cave troll button
                    self.button_cave_troll = PySide2.QtWidgets.QPushButton("Cave Troll")
                init_evil_character_buttons(self)
            init_character_buttons(self)

            # Create region push buttons
            def init_region_buttons(self):
                # Mordor button
                self.button_mordor = PySide2.QtWidgets.QPushButton("Mordor")

                # Gondor button
                self.button_gondor = PySide2.QtWidgets.QPushButton("Gondor")

                # Rohan button
                self.button_rohan = PySide2.QtWidgets.QPushButton("Rohan")

                # Gap of Rohan button
                self.button_gap_of_rohan = PySide2.QtWidgets.QPushButton("Gap of Rohan")

                # Dagorlad button
                self.button_dagorlad = PySide2.QtWidgets.QPushButton("Dagorlad")

                # Fangorn button
                self.button_fangorn = PySide2.QtWidgets.QPushButton("Fangorn")

                # Moria button
                self.button_moria = PySide2.QtWidgets.QPushButton("Moria")

                # Endewaith button
                self.button_endewaith = PySide2.QtWidgets.QPushButton("Endewaith")

                # Mirkwood button
                self.button_mirkwood = PySide2.QtWidgets.QPushButton("Mirkwood")

                # Misty Mountains buton
                self.button_misty_mountains = PySide2.QtWidgets.QPushButton("Misty Mountains")

                # Eregion button
                self.button_eregion = PySide2.QtWidgets.QPushButton("Eregion")

                # Cardolan button
                self.button_cardolan = PySide2.QtWidgets.QPushButton("Cardolan")

                # High pass button
                self.button_high_pass = PySide2.QtWidgets.QPushButton("High Pass")

                # Rhudaur button
                self.button_rhudaur = PySide2.QtWidgets.QPushButton("Rhudaur")

                # Arthedain button
                self.button_arthedain = PySide2.QtWidgets.QPushButton("Arthedain")

                # The Shire button
                self.button_the_shire = PySide2.QtWidgets.QPushButton("The Shire")
            init_region_buttons(self)

            # Init text box widget
            def init_text_box(self):
                # Add text line edit for instructions?
                self.text_box = PySide2.QtWidgets.QLabel()
                size_policy = PySide2.QtWidgets.QSizePolicy(PySide2.QtWidgets.QSizePolicy.Maximum,
                                                            PySide2.QtWidgets.QSizePolicy.Maximum)

                self.text_box.setSizePolicy(size_policy)
                self.text_box.setAlignment(PySide2.QtCore.Qt.AlignHCenter)
            init_text_box(self)
        init_main_buttons(self)

        # Organize layout & connect buttons
        def set_up_main_buttons(self):
            # Organize layout & connect evil character buttons
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
            set_up_evil_buttons(self)

            # Organize layout good character buttons
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
            set_up_good_buttons(self)

            # Organize layout region buttons
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
            set_up_region_buttons(self)

            # Organize layout text box
            def set_up_text_box(self):
                self.sub_box_layout_1_0_2_0.addWidget(self.text_box)
            set_up_text_box(self)
        set_up_main_buttons(self)

        # Start window buttons
        def init_start_buttons(self):
            self.button_select_good = PySide2.QtWidgets.QPushButton("Good")
            self.button_select_evil = PySide2.QtWidgets.QPushButton("Evil")
        init_start_buttons(self)

        # Organize layout & connect buttons
        def set_up_start_buttons(self):
            self.setup_start_grid_layout.addWidget(self.button_select_good)
            self.button_select_good.clicked.connect(self.select_good_clicked)
            self.setup_start_grid_layout.addWidget(self.button_select_evil)
            self.button_select_evil.clicked.connect(self.select_evil_clicked)
        set_up_start_buttons(self)

        # Game information
        self.game = Game.Game(self)
        self.map = self.game.map
        self.player_fellowship = self.game.player_fellowship
        self.player_sauron = self.game.player_sauron

        # To be central widget will be QGraphicsView
        self.central_widget_graphics_view = PySide2.QtWidgets.QGraphicsView()

        # Map of middle earth
        def setup_pixmap_middle_earth(self):
            # Setup QPixmap
            pixmap_item = PySide2.QtGui.QPixmap("images/pic_middle_earth.jpg")
            label = PySide2.QtWidgets.QLabel()

            # Put QPixmap in Label
            label.setPixmap(pixmap_item)
            label.setScaledContents(True)
            self.sub_grid_layout_0_0.addWidget(label)
        setup_pixmap_middle_earth(self)

        self.current_character = None
        self.current_region = None

        self.graphics_scene_start_window()

    # QGraphicsScene to QGraphicsView central widget of self:QMainWindow
    # Also, QGraphicsView central widget Layout to start_grid_layout
    def graphics_scene_start_window(self):
        # Create Graphics scene
        scene_main = PySide2.QtWidgets.QGraphicsScene()

        # Add QGraphicsScene to GraphicsView (Mainwindow's central widget)
        self.central_widget_graphics_view.setScene(scene_main)

        # Set MainWindow's central widget
        self.setCentralWidget(self.central_widget_graphics_view)

        # Set central widget's (GraphicsView's) layout
        self.central_widget_graphics_view.setLayout(self.setup_start_grid_layout)

        # Size window to 50% available screen space
        self.resize(PySide2.QtWidgets.QDesktopWidget.availableGeometry(
            PySide2.QtWidgets.QDesktopWidget()).size() * 0.5)

        self.show()

    # QGraphicsScene to QGraphicsView central widget of self:QMainWindow
    # Also, QGraphicsView central widget Layout to main_grid_layout
    def graphics_scene_main_window(self):
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

        self.show()

    def handle_game(self):
        self.disable_all_buttons()

        # Have player choose side
        def choose_player():
            self.msg("Welcome to the game!")
            self.msg("Select your side: [Good, Evil]")
            # TODO: Cleanup
        choose_player()

    def disable_all_buttons(self):
        for button in self.central_widget_graphics_view.children():
            if isinstance(button, PySide2.QtWidgets.QPushButton):
                button.setEnabled(False)

    def enable_all_buttons(self):
        for button in self.central_widget_graphics_view.children():
            if isinstance(button, PySide2.QtWidgets.QPushButton):
                button.setEnabled(True)

    def msg(self, *args: str):
        txt = self.text_box.text()
        txt += "\n"
        for arg in args:
            txt += arg
        self.text_box.setText(txt)

    def new_msg(self, *args: str):
        txt = ""
        for arg in args:
            txt += arg
        self.text_box.setText(txt)

    def start_game(self):
        self.enable_all_buttons()
        #TODO: LEFTOFF HERE
        self.button_select_evil.setDisabled(True)
        self.button_select_good.setDisabled(True)
        self.button_select_evil.hide()
        self.button_select_good.hide()
        self.hide()
        self.graphics_scene_main_window()
        pass

    def select_evil_clicked(self):
        self.real_player = self.player_sauron
        self.computer_player = self.player_fellowship
        self.new_msg("Evil player chosen. ")
        self.start_game()

    def select_good_clicked(self):
        self.real_player = self.player_fellowship
        self.computer_player = self.player_sauron
        self.new_msg("Good player chosen. ")
        self.start_game()

    def add_dialogue(self, *args):
        full_txt = ''
        for txt in args:
            full_txt += str(txt)
        self.txt_area.setText(self.txt_area.text() + "\n" + full_txt)
