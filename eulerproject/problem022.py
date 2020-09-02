from typing import List


_MIN_LETTER = ord('A') - 1


class Name:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.alphabetic_value: str = sum(
            ord(letter) - _MIN_LETTER for letter in name)

    def __eq__(self, other_name: 'Name') -> bool:
        return self.name == other_name.name

    def __gt__(self, other_name: 'Name') -> bool:
        return self.name > other_name.name

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


class SortedNames():

    def __init__(self) -> None:
        self._inner_list = list()

    def append(self, value: Name) -> None:
        if not self._inner_list:
            self._inner_list.append(value)
            return

        index = 0
        while index < len(self._inner_list) and value > self._inner_list[index]:
            index += 1
        self._inner_list.insert(index, value)

    def __getitem__(self, key) -> int:
        for idx, name in enumerate(self._inner_list):
            if name == key:
                return (idx+1) * name.alphabetic_value
        else:
            raise IndexError(f'{key} not found!')

    def __repr__(self) -> List[Name]:
        return self._inner_list

    def __str__(self) -> str:
        return ', '.join([str(val) for val in self._inner_list])


def main():
    names = SortedNames()

    # Input names
    nb_names = int(input().strip())
    for _ in range(nb_names):
        tmp_name = Name(input().strip())
        names.append(tmp_name)

    # Queries
    nb_queries = int(input().strip())
    for _ in range(nb_queries):
        tmp_name = Name(input().strip())
        print(names[tmp_name])


if __name__ == '__main__':
    main()
