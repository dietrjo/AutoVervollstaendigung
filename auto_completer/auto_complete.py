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

        self.term_list.sort(key=lambda e: e.word)

    def match(self, prefix):
        pass

    def matches(self, prefix):
        n = 0
        left = 0
        right = len(self.term_list)-1
        while left <= right:
            center = left + (right - left) // 2
            print(self.term_list[center])
            if self.term_list[center].word_is_smaller_then(prefix):
                # prefix comes after word in alphabetical order
                left = center + 1
            else:
                # prefix comes before word in alphabetical order
                if self.term_list[center].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                    # word begins with prefix
                    n += 1
                    while right >= center + n and self.term_list[center + n].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        n += 1

                    degr = -1
                    while self.term_list[center + degr].subword_equals_or_is_smaller_then(prefix, len(prefix)) == "equal":
                        degr -= 1
                        n += 1

                    return n

                right = center - 1

        return 0

    def __len__(self):
        return len(self.term_list)

    def __str__(self):
        return ''.join(str(term) for term in self.term_list)


def test():
    filename = sys.argv[1]
    data = AutoComplete(filename)
    print(str(data) + "\n")
    print(data.matches("lam"))


if __name__ == '__main__':
    test()
