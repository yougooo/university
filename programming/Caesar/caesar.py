import string

class Caesar(object):
    LETTER_LOWER = string.ascii_lowercase
    LETTER_UPPER = string.ascii_uppercase
    def __init__(self):
        self.dict_letter = {}

    def build_coder(self, shift=0):
        self.shift = shift
        """
            Returns a dict that can apply a Caesar cipher to a letter.
            The cipher is defined by the shift value. Ignores non-letter characters
            like punctuation, numbers, and spaces.

            shift: 0 <= int < 26
            returns: dict
        """
        def build_pos(pos):
            """
            help function for map definition,
            pos : position letter
            return shift position
            """
            if pos + self.shift >= 26:
                return abs(26 - (pos + self.shift))
            return pos + self.shift

        if all([-26 <= self.shift, self.shift <= 26]):
            self.temp = map(lambda x: (Caesar.LETTER_LOWER[x], Caesar.LETTER_LOWER[build_pos(x)]), range(len(Caesar.LETTER_LOWER)))
            for elem in self.temp:
              self.dict_letter[elem[0]] = elem[1]
              self.dict_letter[elem[0].upper()] = elem[1].upper()
        else:
            return ValueError
        return self.dict_letter

    def apply_coder(self, text, coder):
        def check(letter, dic):
            if letter in Caesar.LETTER_LOWER + Caesar.LETTER_UPPER:
                return dic[letter]
            else:
                return letter

        return ''.join(map(lambda x: check(x, coder), text))

    def apply_shift(self, text, shift):
        return self.apply_coder(text, self.build_coder(shift))
