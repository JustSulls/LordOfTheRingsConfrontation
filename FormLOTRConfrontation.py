import PySide2.QtWidgets
import PySide2.QtCore
import PySide2.QtGui
import Game


class FormLOTRConfrontation(PySide2.QtWidgets.QMainWindow):

    def __init__(self):
        PySide2.QtWidgets.QMainWindow.__init__(self)

        # QGridLayout for central widget QGraphicsView
        main_grid_layout = PySide2.QtWidgets.QGridLayout()
        
        # To hold good character buttons
        sub_grid_layout_0 = PySide2.QtWidgets.QGridLayout()
        
        # To hold map and regions
        sub_grid_layout_1 = PySide2.QtWidgets.QGridLayout()
        
        # To hold map
        sub_grid_layout_0_0 = PySide2.QtWidgets.QGridLayout()

        # To hold region layouts
        sub_grid_layout_1_0 = PySide2.QtWidgets.QGridLayout()
        
        # To hold regions
        sub_box_layout_1_0_0_0 = PySide2.QtWidgets.QHBoxLayout()
        
        # To hold more regions
        sub_box_layout_1_0_1_0 = PySide2.QtWidgets.QHBoxLayout()
        
        # To hold evil characters
        sub_grid_layout_2 = PySide2.QtWidgets.QGridLayout()

        # Insert into sub sub sub layout
        sub_grid_layout_1_0.addLayout(sub_box_layout_1_0_0_0, 0, 0)
        sub_grid_layout_1_0.addLayout(sub_box_layout_1_0_1_0, 1, 0)
        # Insert into sub sub layout
        sub_grid_layout_1.addLayout(sub_grid_layout_0_0, 0, 0)
        sub_grid_layout_1.addLayout(sub_grid_layout_1_0, 1, 0)
        # Insert sub layouts into main layout
        main_grid_layout.addLayout(sub_grid_layout_0, 0, 0)
        main_grid_layout.addLayout(sub_grid_layout_1, 0, 1)
        main_grid_layout.addLayout(sub_grid_layout_2, 0, 2)

        def init_buttons(self):
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

                    # merry button
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

            # Organize layout & connect buttons
            def set_up_buttons(self):
                # Organize layout & connect evil character buttons
                def set_up_evil_buttons(self):
                    # Orcs button
                    self.button_orcs.clicked.connect(self.orcs_clicked)
                    sub_grid_layout_2.addWidget(self.button_orcs)

                    # Shelob button
                    self.button_shelob.clicked.connect(self.shelob_clicked)
                    sub_grid_layout_2.addWidget(self.button_shelob)

                    # Saruman button
                    self.button_saruman.clicked.connect(self.saruman_clicked)
                    sub_grid_layout_2.addWidget(self.button_saruman)

                    # Flying Nazgul button
                    self.button_flying_nazgul.clicked.connect(self.flying_nazgul_clicked)
                    sub_grid_layout_2.addWidget(self.button_flying_nazgul)

                    # Balrog button
                    self.button_balrog.clicked.connect(self.balrog_clicked)
                    sub_grid_layout_2.addWidget(self.button_balrog)

                    # Warg button
                    self.button_warg.clicked.connect(self.warg_clicked)
                    sub_grid_layout_2.addWidget(self.button_warg)

                    # Black Rider button
                    self.button_black_rider.clicked.connect(self.black_rider_clicked)
                    sub_grid_layout_2.addWidget(self.button_black_rider)

                    # Witch King button
                    self.button_witch_king.clicked.connect(self.witch_king_clicked)
                    sub_grid_layout_2.addWidget(self.button_witch_king)

                    # Cave Troll button
                    self.button_cave_troll.clicked.connect(self.cave_troll_clicked)
                    sub_grid_layout_2.addWidget(self.button_cave_troll)
                set_up_evil_buttons(self)

                # Organize layout & connect good character buttons
                def set_up_good_buttons(self):
                    # Frodo button
                    self.button_frodo.clicked.connect(self.frodo_clicked)
                    sub_grid_layout_0.addWidget(self.button_frodo)

                    # Pippin button
                    self.button_pippin.clicked.connect(self.pippin_clicked)
                    sub_grid_layout_0.addWidget(self.button_pippin)

                    # Gandalf button
                    self.button_gandalf.clicked.connect(self.gandalf_clicked)
                    sub_grid_layout_0.addWidget(self.button_gandalf)

                    # Sam button
                    self.button_sam.clicked.connect(self.sam_clicked)
                    sub_grid_layout_0.addWidget(self.button_sam)

                    # Legolas button
                    self.button_legolas.clicked.connect(self.legolas_clicked)
                    sub_grid_layout_0.addWidget(self.button_legolas)

                    # Aragorn button
                    self.button_aragorn.clicked.connect(self.aragorn_clicked)
                    sub_grid_layout_0.addWidget(self.button_aragorn)

                    # Gimli button
                    self.button_gimli.clicked.connect(self.gimli_clicked)
                    sub_grid_layout_0.addWidget(self.button_gimli)

                    # merry button
                    self.button_merry.clicked.connect(self.merry_clicked)
                    sub_grid_layout_0.addWidget(self.button_merry)

                    # Boromir button
                    self.button_boromir.clicked.connect(self.boromir_clicked)
                    self.button_boromir.setDefault(False)
                    sub_grid_layout_0.addWidget(self.button_boromir)
                set_up_good_buttons(self)

                # Organize layout & connect region buttons
                def set_up_region_buttons(self):
                    # Mordor region button
                    self.button_mordor.setEnabled(False)
                    self.button_mordor.setDefault(True)
                    self.button_mordor.clicked.connect(self.mordor_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_mordor)

                    # Gondor region button
                    self.button_gondor.setEnabled(False)
                    self.button_gondor.setDefault(True)
                    self.button_gondor.clicked.connect(self.gondor_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_gondor)

                    # Rohan region button
                    self.button_rohan.setEnabled(False)
                    self.button_rohan.setDefault(True)
                    self.button_rohan.clicked.connect(self.rohan_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_rohan)

                    # Gap of Rohan region button
                    self.button_gap_of_rohan.setEnabled(False)
                    self.button_gap_of_rohan.setDefault(True)
                    self.button_gap_of_rohan.clicked.connect(self.gap_of_rohan_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_gap_of_rohan)

                    # Dagorlad region button
                    self.button_dagorlad.setEnabled(False)
                    self.button_dagorlad.setDefault(True)
                    self.button_dagorlad.clicked.connect(self.dagorlad_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_dagorlad)

                    # Fangorn region button
                    self.button_fangorn.setEnabled(False)
                    self.button_fangorn.setDefault(True)
                    self.button_fangorn.clicked.connect(self.fangorn_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_fangorn)

                    # Moria region button
                    self.button_moria.setEnabled(False)
                    self.button_moria.setDefault(True)
                    self.button_moria.clicked.connect(self.moria_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_moria)

                    # Endewaith region button
                    self.button_endewaith.setEnabled(False)
                    self.button_endewaith.setDefault(True)
                    self.button_endewaith.clicked.connect(self.endewaith_clicked)
                    sub_box_layout_1_0_0_0.addWidget(self.button_endewaith)

                    # Mirkwood region button
                    self.button_mirkwood.setEnabled(False)
                    self.button_mirkwood.setDefault(True)
                    self.button_mirkwood.clicked.connect(self.mirkwood_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_mirkwood)

                    # Misty Mountains region button
                    self.button_misty_mountains.setEnabled(False)
                    self.button_misty_mountains.setDefault(True)
                    self.button_misty_mountains.clicked.connect(self.misty_mountains_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_misty_mountains)

                    # Eregion region button
                    self.button_eregion.setEnabled(False)
                    self.button_eregion.setDefault(True)
                    self.button_eregion.clicked.connect(self.eregion_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_eregion)

                    # Cardolan region button
                    self.button_cardolan.setEnabled(False)
                    self.button_cardolan.setDefault(True)
                    self.button_cardolan.clicked.connect(self.cardolan_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_cardolan)

                    # High Pass region button
                    self.button_high_pass.setEnabled(False)
                    self.button_high_pass.setDefault(True)
                    self.button_high_pass.clicked.connect(self.high_pass_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_high_pass)

                    # Rhudaur region button
                    self.button_rhudaur.setEnabled(False)
                    self.button_rhudaur.setDefault(True)
                    self.button_rhudaur.clicked.connect(self.rhudaur_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_rhudaur)

                    # Arthedain region button
                    self.button_arthedain.setEnabled(False)
                    self.button_arthedain.setDefault(True)
                    self.button_arthedain.clicked.connect(self.arthedain_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_arthedain)

                    # The Shire region button
                    self.button_the_shire.setEnabled(False)
                    self.button_the_shire.setDefault(True)
                    self.button_the_shire.clicked.connect(self.the_shire_clicked)
                    sub_box_layout_1_0_1_0.addWidget(self.button_the_shire)
                set_up_region_buttons(self)
            set_up_buttons(self)

            self.game = Game.Game()
            self.map = self.game.map
            self.player_fellowship = self.game.player_fellowship
            self.player_sauron = self.game.player_sauron
        # Board button setup
        init_buttons(self)

        self.player_fellowship.choose_starting_positions()
        self.player_sauron.choose_starting_positions()

        print("\nGame starting. ")

        # To be central widget will be QGraphicsView
        self.central_widget_graphics_view = PySide2.QtWidgets.QGraphicsView()

        # Setup QPixmap
        pixmap_item = PySide2.QtGui.QPixmap("images/pic_middle_earth.jpg")
        label = PySide2.QtWidgets.QLabel()

        # Put QPixmap in Label
        label.setPixmap(pixmap_item)
        label.setScaledContents(True)
        sub_grid_layout_0_0.addWidget(label)

        # Create Graphics scene
        scene = PySide2.QtWidgets.QGraphicsScene()

        # Add QGraphicsScene to GraphicsView (Mainwindow's central widget)
        self.central_widget_graphics_view.setScene(scene)
        self.central_widget_graphics_view.show()

        # Set MainWindow's central widget
        self.setCentralWidget(self.central_widget_graphics_view)
        
        # Set central widget's (GraphicsView's) layout
        self.central_widget_graphics_view.setLayout(main_grid_layout)

        self.current_character = None
        self.current_region = None

        # Size window to 70% available screen space
        self.resize(PySide2.QtWidgets.QDesktopWidget.availableGeometry(
            PySide2.QtWidgets.QDesktopWidget()).size() * 0.8)

        self.central_widget_graphics_view.show()

    # Mordor clicked
    def mordor_clicked(self):
        pass

    def gondor_clicked(self):
        pass

    def rohan_clicked(self):
        pass

    def gap_of_rohan_clicked(self):
        pass

    def dagorlad_clicked(self):
        pass

    def fangorn_clicked(self):
        pass

    def moria_clicked(self):
        pass

    def endewaith_clicked(self):
        pass

    def mirkwood_clicked(self):
        pass

    def misty_mountains_clicked(self):
        pass

    def eregion_clicked(self):
        pass

    def cardolan_clicked(self):
        pass

    def high_pass_clicked(self):
        pass

    def rhudaur_clicked(self):
        pass

    def arthedain_clicked(self):
        pass

    def the_shire_clicked(self):
        pass

    def orcs_clicked(self):
        pass

    def shelob_clicked(self):
        pass

    def saruman_clicked(self):
        pass

    def flying_nazgul_clicked(self):
        pass

    def balrog_clicked(self):
        pass

    def warg_clicked(self):
        pass

    def black_rider_clicked(self):
        pass

    def witch_king_clicked(self):
        pass

    def cave_troll_clicked(self):
        pass

    def frodo_clicked(self):
        pass

    def pippin_clicked(self):
        pass

    def gandalf_clicked(self):
        pass

    def sam_clicked(self):
        pass

    def legolas_clicked(self):
        pass

    def aragorn_clicked(self):
        pass

    def gimli_clicked(self):
        pass

    def merry_clicked(self):
        pass

    def boromir_clicked(self):
        pass

    def boromir_clicked(self):
        self.current_character = self.game.boromir
        self.button_boromir.setEnabled(False)
        self.button_cardolan.setEnabled(True)

    def msg(self, txt):
        self.txt_area.setText(txt)

    def add_dialogue(self, *args):
        full_txt = ''
        for txt in args:
            full_txt += str(txt)
        self.txt_area.setText(self.txt_area.text() + "\n" + full_txt)
