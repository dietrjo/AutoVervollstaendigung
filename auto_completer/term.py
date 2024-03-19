class Term:
    def __init__(self, weight, word):
        if weight < 0:
            raise ValueError(f'Error! Weight of {word} is not positive.')
        self.weight = weight
        self.word = word

    def word_is_smaller_then(self, other_word):
        return self.word < other_word

    def weight_is_smaller_then(self, other_weight):
        return self.weight < other_weight

    def subword_is_smaller_then(self, other_word, num_first_letters):
        return self.word[0:num_first_letters] < other_word[0:num_first_letters]

    def __str__(self):
        return f'{self.weight:>14} {self.word}'


def test():
    term1 = Term(5627187200, "the")
    term2 = Term(879975500, "his")
    term3 = Term(109051000, "these")

    print(term1)
    print(term2)
    print(term3)

    print(f'\n{term1.word_is_smaller_then(term2.word)} (has to be: False)')
    print(f'{term1.weight_is_smaller_then(term2.weight)} (has to be: False)\n')

    print(f'{term1.subword_is_smaller_then(term3.word, 4)} (has to be: True)')
    print(f'{term1.subword_is_smaller_then(term3.word, 3)} (has to be: False)')


if __name__ == '__main__':
    test()
