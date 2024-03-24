import sys
from auto_complete import AutoComplete


def run(data, k):
    while True:
        prefix = input()
        match_list = data.match(prefix)
        repeats = len(match_list) if len(match_list) < k else k
        for i in range(repeats):
            print(match_list[i], end="")


def main():
    file = sys.argv[1]
    k = int(sys.argv[2])
    data = AutoComplete(file)

    run(data, k)


if __name__ == '__main__':
    main()
