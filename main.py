from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Background can also be Light
        self.theme_cls.primary_palette = "Orange"  # Restart the game button color
        return Builder.load_file('main.kv')  # Path to the kv file

    # Define Who's turn it is
    turn = "X"
    # Keep Track of win or lose
    winner = False

    # No Winner aka tie
    def no_winner(self):
        if self.winner == False and \
                self.root.ids.btn1.disabled == True and \
                self.root.ids.btn2.disabled == True and \
                self.root.ids.btn3.disabled == True and \
                self.root.ids.btn4.disabled == True and \
                self.root.ids.btn5.disabled == True and \
                self.root.ids.btn6.disabled == True and \
                self.root.ids.btn7.disabled == True and \
                self.root.ids.btn8.disabled == True and \
                self.root.ids.btn9.disabled == True:
            self.root.ids.score.text = "We got a tie"

    # Color the winning combo in red
    def end_game(self, a, b, c):
        self.winner = True
        a.color = "red"
        b.color = "red"
        c.color = "red"

        # Disable the buttons
        self.disable_all_buttons()

        # Set Label for winner
        self.root.ids.score.text = f"{a.text} Wins!"

    def disable_all_buttons(self):
        # Disable The Buttons
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True

    def win(self):
        # Across
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1,
                          self.root.ids.btn2, self.root.ids.btn3)

        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4,
                          self.root.ids.btn5, self.root.ids.btn6)

        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7,
                          self.root.ids.btn8, self.root.ids.btn9)
        # Down
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1,
                          self.root.ids.btn4, self.root.ids.btn7)

        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2,
                          self.root.ids.btn5, self.root.ids.btn8)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3,
                          self.root.ids.btn6, self.root.ids.btn9)

        # Diagonal
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn1,
                          self.root.ids.btn5, self.root.ids.btn9)

        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn3,
                          self.root.ids.btn5, self.root.ids.btn7)

        self.no_winner()

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = "X"
            btn.disabled = True  # Disable The Button After Its Pressed
            # Changes The Label To Next Player's Turn
            self.root.ids.score.text = "O's Turn!"
            self.turn = "O"
        else:
            btn.text = "O"
            btn.disabled = True
            self.root.ids.score.text = "X's Turn!"
            self.turn = "X"

        # Check To See if won
        self.win()

    def restart(self):
        # Reset Who's Turn It Is
        self.turn = "X"

        # Enable The Buttons
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        # Clear The Buttons
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""

        # Reset The Score Label
        self.root.ids.score.text = "X GOES FIRST!"

        # Reset The Winner Variable
        self.winner = False


MainApp().run()


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&&&&&@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# &&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&
# &&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&&@@&
# &&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&@&&&&&&&&
# &&&&@@@@@@@@@@@@@@@@@@@@@&&&&&&%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&@&&&&&&&&
# &@&@@@@@@@@&@&&&@@@@&&&%%######%##%%#####%%%%&&&@@@@@@@@@@@@@@@@@@@@&@&&&&&&&&&&
# &&@@@@@@@&&&%&&&@@@&%&%#(*********************/(#&&@@@@@%&@@@@@@@@@@@@@@&&@@@@&@
# @&@@@@@@@@&%&&&@%%&%%#(/**,,,,,,,,,,,,,,,**********/((###%#%&@@@@@@@@@@@@@@@@@&%
# &@@@@@@@@&%&%%%%&%%%#(/*,,,,,,,,,,,,,,,,,,,,***********///(((#&@@@@@@@@@@@@@@@(/
# @@@@@@@@&&&&&&%%%###(//*,,,,,,,,,,,,,,,,,,,,****,*******////((#@@@@@@@@@@@@@@@&(
# @@@@&@@@&&%&%&###((((/****,,,,,,,,,,,,,,,,,,,,,,*******/***//((%@@@@@@@@@@@@@@@#
# &&&&&@@@@&%%%%###((((/****,,,,,,,,,,,,,,,,,,,,,,*************//#@@@@@@@@@@@@@@@%
# &&&&#%@@&&%%#(##(((((/*******,,,,,,,,,,,,,,,,*,,**************/(%@@@@@@@@@@@@@@@
# //**/(@&&%%#(##((#(/*********,*,,,,,,,,,,,,,,,,,,*,****,,,***//#&@@@@@@@@@@@@@@@
# *****/%&%%%%####((/************,,,,,/*****,,,*,,***********/(#@@@@@@@@@@@@@@@@@@
# *******%#(%%#####(/**********,,,,*/((#&&&&&@&@@&%/((/**//(#&@@&&&@@@@@@@@@@@@@@@
# ***/##*,,**(%%##((*************(%###(((((#%%%%%%%%%#((((%@@@@&@@@@@@@@@@@@@@@@@@
# ****/%///*,*/%#((/**********////////((#%%&&@&%%%%###((#@@@@@&&&&&@@@@@@@@@@@@@@@
# ****//*//((/*/((//*********/*/((#&&&@@@@#(#&&@&%%#*,,,,(@&&&&%%##%@@@@@@@@@@@@@@
# **////**/(///*(//**************/**/(//((/((##((*,,,,,,.,*((((((((#@@@@@@@@@@@@@@
# ///((((,,****,*(//******,*,,,,*,,,**/(((((///*,,,,,,,,,,,*(/////(#@@@@@@@@@@@@@@
# (###%%%#/*,*/**/((///*****,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,*////(#@@@@@@@@@@@@@@
# &&&&&@@@&//(*/(((##((//****,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,**//(#@@@@@@@@@@@@@@
# @@@@@@@@@@@(***/(####((//****,,,,,,,,,,,,,,,,,,****,,,,,,,,,,*/((#@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@&&%##(((///****,,,,,,,,,,,,,,*****,,,,,,,,***(#((%@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@%%#%(((((///*********,**,,****,*/((#%%%%%%&@&%##@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@#####(((((/////*/************,,,,,,*/((%%%%&%%&&@@@@@@@@@@@@@@@
# &@@@@@@@@@@@@@@@@###((##(((//////////******//***************(&&%@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@###(((##((////////***//#%%#(//***//###%%&&&%%@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@%###((((##((//////////(((//**//((//////(/(#%&@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@%(##((((((#(((////((////*********///(####%&@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@&(((((((((((##(((////////*****///(((#((##@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@((((((((((((((##((////////********///(&@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@&(((((((((((((((#%#(#((////*/**//((#@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@(((((((((((((((####%%#######%&@#@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@&(((((((((((###########%@@@@@#@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%(((((((((####(((###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(//((((((((/((((#@@@@@@@/@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(/(((((////((@@@@@@@@@#@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%((////////(@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#((((/((%@@@@@@@@@@(@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#(((&@@@@@@@@@@@(@@@@@@@@@@@@@@@@@@

#             @@@@@@@      @@@@  @@@@
#           @@        @@   @@@@  @@@@
#          @@   #@@@   @@        @@@@
#          @@ #@#       @  @@@@  @@@@       @@@@   @@@  @@@@@@@@@@
#          @@ &@*       @  @@@@  @@@@        @@@# @@@     .@@@@@@@
#           @@  #@@@  %@   @@@@  @@@@@@@      @@@@@@   (@@@   *@@@
#             @@     @@    @@@@  @@@@@@@       @@@@*    @@@@@@ @@@#
#              ,@@@@@                      @@@@@@*
