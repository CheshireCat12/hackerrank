import datetime
from itertools import accumulate
from typing import List

_DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Date:

    def __init__(self, date: List[int], start: bool = False) -> None:
        self.year, self.month, self.day = date
        self.start = start

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year

    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month: int) -> None:
        if month > 12:
            self.start_new_year()
        else:
            self.__month = month

    @property
    def day(self) -> int:
        return self.__day

    @day.setter
    def day(self, day: int) -> None:
        if day > _DAYS_PER_MONTH[self.month-1]:
            self.__day = 1
            self.month += 1
        else:
            self.__day = day

    @property
    def start(self) -> bool:
        return self.__start

    @start.setter
    def start(self, start: bool) -> None:
        self.__start = start
        if start:
            self.month += 1 if self.day != 1 else 0
            if self.month == 12 and self.day != 1:
                self.start_new_year

    def __repr__(self) -> str:
        return f'Year: {self.year}, Month: {self.month}, Day: {self.day}'

    def start_new_year(self) -> None:
        self.year += 1
        self.month, self.day = 1, 1

    def tolist(self) -> List[int]:
        return [self.year, self.month, 1]

    def is_leap_year(self) -> bool:
        return self.year % 4 == 0 and (not self.year % 100 == 0 or self.year % 400 == 0)

    def weekday(self) -> int:
        return datetime.datetime(*self.tolist()).weekday()


def compute_offset_leap_year(current_date: Date, active_month: int) -> int:
    if current_date.month <= 2 and active_month > 1:
        return int(current_date.is_leap_year())

    return 0


def _sundays_per_year(current_date: Date, last_date: Date) -> int:
    starting_day: int = current_date.weekday()
    sundays_counter: int = 0
    last_month: int = last_date.month if current_date.year == last_date.year else 12
    sum_days_per_month: List[int] = list(accumulate(
        [0] + _DAYS_PER_MONTH[current_date.month-1:last_month-1]))

    for active_month, nb_days in enumerate(sum_days_per_month, current_date.month-1):
        nb_days += compute_offset_leap_year(current_date, active_month)
        sundays_counter += int((nb_days + starting_day) % 7 == 6)

    return sundays_counter


def count_sundays(current_date: Date, date_finish: Date) -> int:
    sundays_counter: int = 0

    while current_date.year <= date_finish.year:
        sundays_counter += _sundays_per_year(current_date, date_finish)

        current_date.start_new_year()

    return sundays_counter


def main():
    nb_tests = int(input().strip())

    for _ in range(nb_tests):
        date_start = Date([int(val) for val in input().strip().split()],
                          start=True)
        date_finish = Date([int(val) for val in input().strip().split()],
                           start=False)

        # Modulo the year by 2800 if the year is too large > 9999
        diff_year = date_finish.year - date_start.year
        date_start.year %= 2800
        date_finish.year = date_start.year + diff_year

        print(count_sundays(date_start, date_finish))


if __name__ == "__main__":
    main()
