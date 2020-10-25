from .tut import TutBy
from data_base.db1 import db2
from datetime import date, timedelta
import os
import json
import psycopg2

WORK = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_parse(start_date: str, end_date: str = None):
    global WORK
    start = date(*[int(el) for el in start_date.split(".")[::-1]])
    if end_date is not None:
        end = date(*[int(el) for el in end_date.split(".")[::-1]])
    else:
        end = date.today()
    delta_days = 0
    while WORK:
        curent_date = start + timedelta(days=delta_days)
        tut_by = TutBy(curent_date.strftime("%d.%m.%Y"))
        tut_by.get_rubrics()
        tut_by.get_news()
        db2(tut_by,curent_date.strftime("%d.%m.%Y"))
        if curent_date == end:
            WORK = False
        else:
            delta_days += 1
    else:
        pass


def stop_parse():
    global WORK
    WORK = False
