from typing import Any
from db_con import DbConnector

import datetime

# класс отвечающий за агрегацию статистических данных
class Alg:

    def __init__(self, dt_from: datetime, dt_upto: datetime, group_type: str, input_data) -> None:
        self.dt_from = dt_from
        self.dt_upto = dt_upto
        self.group_type = group_type
        self.input_data = input_data
        self.result = {}

    # метод часовой агрегации
    def hour_type(self):
        hour = datetime.timedelta(hours=1)

    # метод дневной агрегации    
    def day_type(self):
        day = datetime.timedelta(days=1)

    # метод недельной агрегации    
    def week_type(self):
        week = datetime.timedelta(weeks=1)

    # метод месячной агрегации    
    def month_type(self):
        month = datetime.timedelta(month=1)

    def get_result(self):
        return self.result 