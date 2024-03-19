import sys

from term import Term


class AutoComplete:
    def __init__(self, filename):
        self.term_list = []
        data = open(filename, 'r', encoding='utf-8')
        next(data)

        for line in data:
            term = Term(int(line[:14]), line[15:])
            self.term_list += [term]

    def match(self, prefix):
        pass

    def matches(self, prefix):
        left = 0
        right = len(self.term_list)-1
        while True:
            center = left + (right - left) // 2
            if self.term_list[center].word_is_smaller_then(prefix):
                # prefix comes after word in alphabetical order
                pass
            else:
                pass

    def __len__(self):
        pass

    def __str__(self):
        return ''.join(str(term) for term in self.term_list)


def test():
    filename = sys.argv[1]
    data = AutoComplete(filename)
    print(data)


if __name__ == '__main__':
    test()
