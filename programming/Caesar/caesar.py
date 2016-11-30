import string
import re

class Caesar(object):
    LETTER_LOWER = string.ascii_lowercase
    LETTER_UPPER = string.ascii_uppercase
    def __init__(self, words_path, shift_path):
        self.dict_letter = {}
        self.word_file = open(words_path).read()
        self.shift_file = open(shift_path).read()

    def _build_pos(self, pos):
        """
        help function for map definition,
        pos : position letter
        return shift position
        """
        if pos + self.shift >= 26:
            return abs(26 - (pos + self.shift))
        return pos + self.shift

    def build_coder(self, shift=0):
        """
        shift: 0 <= int < 26
        returns: dict
        """
        self.shift = shift
        if all([-26 <= self.shift, self.shift <= 26]):
            self.temp = map(lambda x: (Caesar.LETTER_LOWER[x], Caesar.LETTER_LOWER[self._build_pos(x)]), range(len(Caesar.LETTER_LOWER)))
            for elem in self.temp:
                self.dict_letter[elem[0]] = elem[1]
                self.dict_letter[elem[0].upper()] = elem[1].upper()
        else:
            return ValueError
        return self.dict_letter

    def _check(self, letter, dic):
        """
        :param letter: some char symbol
        :param dic: translate data dict
        :return: correct symbol or if in not in dict, just symbol
        """
        if letter in Caesar.LETTER_LOWER + Caesar.LETTER_UPPER:
            return dic[letter]
        else:
            return letter

    def _apply_coder(self, text, coder):
        
        return ''.join(map(lambda x: self._check(x, coder), text))

    def apply_shift(self, text, shift):
        return self._apply_coder(text, self.build_coder(shift))

    def _word(self, word):
        #print word
        pattern = re.compile(word)
        if pattern.search(self.word_file):
            return 1
        return 0

    def expresion(self, exp):
        temp = map(lambda x: self._word(x), exp.split())
        #for i in exp.split():
        #    print i
        #    print self._word(i)
        return sum(temp)

    def best_shift(self):
        shift_all = map(lambda x: self.expresion(self.apply_shift(self.shift_file, x)), range(27))
        #for best in range(27):
        print self.shift_file
        print shift_all
        print len(self.shift_file)
        return shift_all.index(max(shift_all))

shift = Caesar('words.txt', 'story.txt')

print shift.best_shift()
