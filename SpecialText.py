class SpecialText:

    def __init__(self, text, precedence, target_character=None, target_region=None):
        self.text = text
        self.precedence = precedence
        self.target_character = target_character
        self.target_region = target_region

    def __str__(self):
        return self.text
