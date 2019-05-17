import PySide2.QtWidgets
import Game


class FormLOTRConfrontation(PySide2.QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(FormLOTRConfrontation, self).__init__(parent)

        # self.map = Map()
        # self.player_fellowship = Player.Player(self.map)
        self.game = Game.Game()
        self.map = self.game.map
        self.player_fellowship = self.game.player_fellowship
        self.player_sauron = self.game.player_sauron

        # Board setup
        self.player_fellowship.choose_starting_positions()
        self.player_sauron.choose_starting_positions()

        print("\nGame starting. ")

        # Declare layout
        self.layout_regions = PySide2.QtWidgets.QHBoxLayout(PySide2.QtWidgets.QHBoxLayout.LeftToRight)
        self.layout_good_characters = PySide2.QtWidgets.QVBoxLayout(PySide2.QtWidgets.QBoxLayout.TopToBottom)
        self.layout_evil_characters = PySide2.QtWidgets.QVBoxLayout(PySide2.QtWidgets.QBoxLayout.TopToBottom)

        # Text section
        self.txt_area = PySide2.QtWidgets.QLabel()

        def init_buttons(me):
            # Frodo button
            me.button_frodo = PySide2.QtWidgets.QPushButton("Frodo")

            # Pippin button
            me.button_pippin = PySide2.QtWidgets.QPushButton("Pippin")

            # Gandalf button
            me.button_gandalf = PySide2.QtWidgets.QPushButton("Gandalf")

            # Sam button
            me.button_sam = PySide2.QtWidgets.QPushButton("Sam")

            # Legolas button
            me.button_legolas = PySide2.QtWidgets.QPushButton("Legolas")

            # Aragorn button
            me.button_aragorn = PySide2.QtWidgets.QPushButton("Aragorn")

            # Gimli button
            me.button_gimli = PySide2.QtWidgets.QPushButton("Gimli")

            # Merry button
            me.button_merry = PySide2.QtWidgets.QPushButton("Merry")

            # Boromir button
            me.button_boromir = PySide2.QtWidgets.QPushButton("Boromir")

            # Orcs button
            me.button_orcs = PySide2.QtWidgets.QPushButton("Orcs")

            # Shelob button
            me.button_shelob = PySide2.QtWidgets.QPushButton("Shelob")

            # Saruman button
            me.button_saruman = PySide2.QtWidgets.QPushButton("Saruman")

            # Flying Nazgul button
            me.button_flying_nazgul = PySide2.QtWidgets.QPushButton("Flying Nazgul")

            # Balrog button
            me.button_balrog = PySide2.QtWidgets.QPushButton("Balrog")

            # Warg button
            me.button_warg = PySide2.QtWidgets.QPushButton("Warg")

            # Black rider button
            me.button_black_rider = PySide2.QtWidgets.QPushButton("Black Rider")

            # Witch King button
            me.button_witch_king = PySide2.QtWidgets.QPushButton("Witch King")

            # Cave troll button
            me.button_cave_troll = PySide2.QtWidgets.QPushButton("Cave Troll")

            # Mordor button
            me.button_mordor = PySide2.QtWidgets.QPushButton("Mordor")

            # Gondor button
            me.button_gondor = PySide2.QtWidgets.QPushButton("Gondor")

            # Rohan button
            me.button_rohan = PySide2.QtWidgets.QPushButton("Rohan")

            # Gap of Rohan button
            me.button_gap_of_rohan = PySide2.QtWidgets.QPushButton("Gap of Rohan")

            # Dagorlad button
            me.button_dagorlad = PySide2.QtWidgets.QPushButton("Dagorlad")

            # Fangorn button
            me.button_fangorn = PySide2.QtWidgets.QPushButton("Fangorn")

            # Moria button
            me.button_moria = PySide2.QtWidgets.QPushButton("Moria")

            # Endewaith button
            me.button_endewaith = PySide2.QtWidgets.QPushButton("Endewaith")

            # Mirkwood button
            me.button_mirkwood = PySide2.QtWidgets.QPushButton("Mirkwood")

            # Misty Mountains buton
            me.button_misty_mountains = PySide2.QtWidgets.QPushButton("Misty Mountains")

            # Eregion button
            me.button_eregion = PySide2.QtWidgets.QPushButton("Eregion")

            # Cardolan button
            me.button_cardolan = PySide2.QtWidgets.QPushButton("Cardolan")

            # High pass button
            me.button_high_pass = PySide2.QtWidgets.QPushButton("High Pass")

            # Rhudaur button
            me.button_rhudaur = PySide2.QtWidgets.QPushButton("Rhudaur")

            # Arthedain button
            me.button_arthedain = PySide2.QtWidgets.QPushButton("Arthedain")

            # The Shire button
            me.button_the_shire = PySide2.QtWidgets.QPushButton("The Shire")

        init_buttons(self)

        self.pixmap = PySide2.QtGui.QPixmap('map_middle_earth.jpg')
        self.label_map = PySide2.QtWidgets.QLabel()

        def init_ui(self):
            # Text section
            self.layout_regions.addWidget(self.txt_area)

            # Orcs button
            self.button_orcs.clicked.connect(self.orcs_clicked)
            self.layout_regions.addWidget(self.button_orcs)
            # self.layout.setAlignment(self.button_orcs, Qt.AlignRight)

            # Shelob button
            self.button_shelob.clicked.connect(self.shelob_clicked)
            self.layout_regions.addWidget(self.button_shelob)
            # self.layout.setAlignment(self.button_shelob, Qt.AlignRight)

            # Saruman button
            self.button_saruman.clicked.connect(self.saruman_clicked)
            self.layout_regions.addWidget(self.button_saruman)
            # self.layout.setAlignment(self.button_saruman, Qt.AlignRight)

            # Flying Nazgul button
            self.button_flying_nazgul.clicked.connect(self.flying_nazgul_clicked)
            self.layout_regions.addWidget(self.button_flying_nazgul)
            # self.layout.setAlignment(self.button_flying_nazgul, Qt.AlignRight)

            # Balrog button
            self.button_balrog.clicked.connect(self.balrog_clicked)
            self.layout_regions.addWidget(self.button_balrog)
            # self.layout.setAlignment(self.button_balrog, Qt.AlignRight)

            # Warg button
            self.button_warg.clicked.connect(self.warg_clicked)
            self.layout_regions.addWidget(self.button_warg)
            # self.layout.setAlignment(self.button_warg, Qt.AlignRight)

            # Black Rider button
            self.button_black_rider.clicked.connect(self.black_rider_clicked)
            self.layout_regions.addWidget(self.button_black_rider)
            # self.layout.setAlignment(self.button_black_rider, Qt.AlignRight)

            # Witch King button
            self.button_witch_king.clicked.connect(self.witch_king_clicked)
            self.layout_regions.addWidget(self.button_witch_king)
            # self.layout.setAlignment(self.button_witch_king, Qt.AlignRight)

            # Cave Troll button
            self.button_cave_troll.clicked.connect(self.cave_troll_clicked)
            self.layout_regions.addWidget(self.button_cave_troll)
            # self.layout.setAlignment(self.button_cave_troll, Qt.AlignRight)

            # Frodo button
            self.button_frodo.clicked.connect(self.frodo_clicked)
            self.layout_regions.addWidget(self.button_frodo)
            # self.layout.setAlignment(self.button_frodo, Qt.AlignLeft)

            # Pippin button
            self.button_pippin.clicked.connect(self.pippin_clicked)
            self.layout_regions.addWidget(self.button_pippin)
            # self.layout.setAlignment(self.button_pippin, Qt.AlignLeft)

            # Gandalf button
            self.button_gandalf.clicked.connect(self.gandalf_clicked)
            self.layout_regions.addWidget(self.button_gandalf)
            # self.layout.setAlignment(self.button_gandalf, Qt.AlignLeft)

            # Sam button
            self.button_sam.clicked.connect(self.sam_clicked)
            self.layout_regions.addWidget(self.button_sam)
            # self.layout.setAlignment(self.button_sam, Qt.AlignLeft)

            # Legolas button
            self.button_legolas.clicked.connect(self.legolas_clicked)
            self.layout_regions.addWidget(self.button_legolas)
            # self.layout.setAlignment(self.button_legolas, Qt.AlignLeft)

            # Aragorn button
            self.button_aragorn.clicked.connect(self.aragorn_clicked)
            self.layout_regions.addWidget(self.button_aragorn)
            # self.layout.setAlignment(self.button_aragorn, Qt.AlignLeft)

            # Gimli button
            self.button_gimli.clicked.connect(self.gimli_clicked)
            self.layout_regions.addWidget(self.button_gimli)
            # self.layout.setAlignment(self.button_gimli, Qt.AlignLeft)

            # Merry button
            self.button_merry.clicked.connect(self.merry_clicked)
            self.layout_regions.addWidget(self.button_merry)
            # self.layout.setAlignment(self.button_merry, Qt.AlignLeft)

            # Boromir button
            self.button_boromir.clicked.connect(self.boromir_clicked)
            self.button_boromir.setDefault(False)
            self.layout_regions.addWidget(self.button_boromir)
            # self.layout.setAlignment(self.button_boromir, Qt.AlignLeft)

            # Mordor region button
            self.button_mordor.setEnabled(False)
            self.button_mordor.setDefault(True)
            self.button_mordor.clicked.connect(self.mordor_clicked)
            self.layout_regions.addWidget(self.button_mordor)
            # self.layout.setAlignment(self.button_mordor, Qt.AlignLeft)

            # Gondor region button
            self.button_gondor.setEnabled(False)
            self.button_gondor.setDefault(True)
            self.button_gondor.clicked.connect(self.gondor_clicked)
            self.layout_regions.addWidget(self.button_gondor)
            # self.layout.setAlignment(self.button_gondor, Qt.AlignCenter)

            # Rohan region button
            self.button_rohan.setEnabled(False)
            self.button_rohan.setDefault(True)
            self.button_rohan.clicked.connect(self.rohan_clicked)
            self.layout_regions.addWidget(self.button_rohan)
            # self.layout.setAlignment(self.button_rohan, Qt.AlignCenter)

            # Gap of Rohan region button
            self.button_gap_of_rohan.setEnabled(False)
            self.button_gap_of_rohan.setDefault(True)
            self.button_gap_of_rohan.clicked.connect(self.gap_of_rohan_clicked)
            self.layout_regions.addWidget(self.button_gap_of_rohan)
            # self.layout.setAlignment(self.button_gap_of_rohan, Qt.AlignCenter)

            # Dagorlad region button
            self.button_dagorlad.setEnabled(False)
            self.button_dagorlad.setDefault(True)
            self.button_dagorlad.clicked.connect(self.dagorlad_clicked)
            self.layout_regions.addWidget(self.button_dagorlad)
            # self.layout.setAlignment(self.button_dagorlad, Qt.AlignCenter)

            # Fangorn region button
            self.button_fangorn.setEnabled(False)
            self.button_fangorn.setDefault(True)
            self.button_fangorn.clicked.connect(self.fangorn_clicked)
            self.layout_regions.addWidget(self.button_fangorn)
            # self.layout.setAlignment(self.button_fangorn, Qt.AlignCenter)

            # Moria region button
            self.button_moria.setEnabled(False)
            self.button_moria.setDefault(True)
            self.button_moria.clicked.connect(self.moria_clicked)
            self.layout_regions.addWidget(self.button_moria)
            # self.layout.setAlignment(self.button_moria, Qt.AlignCenter)

            # Endewaith region button
            self.button_endewaith.setEnabled(False)
            self.button_endewaith.setDefault(True)
            self.button_endewaith.clicked.connect(self.endewaith_clicked)
            self.layout_regions.addWidget(self.button_endewaith)
            # self.layout.setAlignment(self.button_endewaith, Qt.AlignCenter)

            # Mirkwood region button
            self.button_mirkwood.setEnabled(False)
            self.button_mirkwood.setDefault(True)
            self.button_mirkwood.clicked.connect(self.mirkwood_clicked)
            self.layout_regions.addWidget(self.button_mirkwood)
            # self.layout.setAlignment(self.button_mirkwood, Qt.AlignCenter)

            # Misty Mountains region button
            self.button_misty_mountains.setEnabled(False)
            self.button_misty_mountains.setDefault(True)
            self.button_misty_mountains.clicked.connect(self.misty_mountains_clicked)
            self.layout_regions.addWidget(self.button_misty_mountains)
            # self.layout.setAlignment(self.button_misty_mountains, Qt.AlignCenter)

            # Eregion region button
            self.button_eregion.setEnabled(False)
            self.button_eregion.setDefault(True)
            self.button_eregion.clicked.connect(self.eregion_clicked)
            self.layout_regions.addWidget(self.button_eregion)
            # self.layout.setAlignment(self.button_eregion, Qt.AlignCenter)

            # Cardolan region button
            self.button_cardolan.setEnabled(False)
            self.button_cardolan.setDefault(True)
            self.button_cardolan.clicked.connect(self.cardolan_clicked)
            self.layout_regions.addWidget(self.button_cardolan)
            # self.layout.setAlignment(self.button_cardolan, Qt.AlignCenter)

            # High Pass region button
            self.button_high_pass.setEnabled(False)
            self.button_high_pass.setDefault(True)
            self.button_high_pass.clicked.connect(self.high_pass_clicked)
            self.layout_regions.addWidget(self.button_high_pass)
            # self.layout.setAlignment(self.button_high_pass, Qt.AlignCenter)

            # Rhudaur region button
            self.button_rhudaur.setEnabled(False)
            self.button_rhudaur.setDefault(True)
            self.button_rhudaur.clicked.connect(self.rhudaur_clicked)
            self.layout_regions.addWidget(self.button_rhudaur)
            # self.layout.setAlignment(self.button_rhudaur, Qt.AlignCenter)

            # Arthedain region button
            self.button_arthedain.setEnabled(False)
            self.button_arthedain.setDefault(True)
            self.button_arthedain.clicked.connect(self.arthedain_clicked)
            self.layout_regions.addWidget(self.button_arthedain)
            # self.layout.setAlignment(self.button_arthedain, Qt.AlignCenter)

            # The Shire region button
            self.button_the_shire.setEnabled(False)
            self.button_the_shire.setDefault(True)
            self.button_the_shire.clicked.connect(self.the_shire_clicked)
            self.layout_regions.addWidget(self.button_the_shire)
            # elf.layout.setAlignment(self.button_the_shire, Qt.AlignCenter)

            # smaller_pixmap = self.pixmap.scaled(800, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
            # smaller_pixmap = self.pixmap.scaled(PySide2.QtCore.QSize)
            # self.label_map.setPixmap(smaller_pixmap)
            self.layout_regions.addWidget(self.label_map)

        init_ui()

        self.setLayout(self.layout_regions)

        self.current_character = None
        self.current_region = None

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
