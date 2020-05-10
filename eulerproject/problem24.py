from math import factorial

_WORD = 'abcdefghijklm'


def is_in_range(position: int, ord_letter: int, boundary: int, offset: int) -> bool:
    """
    Check if the given position is in the range of the boundary + the offset
    """
    lower_bound = (ord_letter * boundary + 1) + offset
    upper_bound = ((ord_letter+1) * boundary) + offset
    return lower_bound <= position <= upper_bound


def lexicographe(position: int, letters: str = '', offset: int = 0) -> int:
    """
    Compute the lexicographic permutation of the given position
    """
    prunned_word = _WORD.translate({ord(i): None for i in letters})

    if len(prunned_word) == 1:
        return letters + prunned_word[0]

    boundary = factorial(len(prunned_word) - 1)
    for i, current_letter in enumerate(prunned_word):

        if is_in_range(position, i, boundary, offset):
            offset += i * boundary

            return lexicographe(position, letters + current_letter, offset)


def main():
    nb_tests = int(input().strip())

    print(*[lexicographe(int(input().strip())) for _ in range(nb_tests)],
          sep='\n')


if __name__ == '__main__':
    main()
