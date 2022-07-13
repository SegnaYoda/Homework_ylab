"""
Разжатие массива дат.

Реализован метод schedule, который генерирует дни, в которые показывают фильм.
"""
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    """Декоратор по разжатию массива дат."""

    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """Генератор расписания."""
        try:
            for i in self.dates:
                delta_day = i[0]
                yield delta_day
                while delta_day != i[1]:
                    delta_day += timedelta(days=1)
                    yield delta_day
        except Exception:
            print("Проверьте данные массива расписания.")


m = Movie("sw", [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7)),
])

if __name__ == "__main__":
    for d in m.schedule():
        print(d)
