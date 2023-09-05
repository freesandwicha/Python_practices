# -*- coding = utf-8 -*-
# Motto : Practice makes perfect.
# Time : 5/9/2023 10:19 am

from dataclasses import dataclass
from datetime import datetime as dt

@dataclass
class Weather:
    date: dt
    details: dict
    temp: str
    weather: list[dict]
    description: str

    def __str__(self):
        return f'[{self.date:%H:%M}] {self.temp}C° （{self.description})'



