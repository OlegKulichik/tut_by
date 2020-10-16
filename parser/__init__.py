import sys
sys.path.append('./parser/')
from tut import TutBy
from datetime import date, timedelta
import os
import json

WORK = True
os.mkdir("/home/oleg/Документы/PY/tut_by/NEWS")

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
        tut = TutBy(curent_date.strftime("%d.%m.%Y"))
        os.mkdir("/home/oleg/Документы/PY/tut_by/NEWS/{}".format(curent_date))
        ff = list(tut.get_rubrics().keys())
        rr = tut.get_news()
        for a in ff:
            with open("{}.json".format(a), 'tw', encoding='utf-8') as file:
                json.dump(rr, file, indent=2, ensure_ascii=False)
            os.replace("{0}.json".format(a), "NEWS/{0}/{1}.json".format(curent_date,a))
        if curent_date == end:
            WORK = False
        else:
            delta_days += 1
    else:
        pass

def stop_parse():
    global WORK
    WORK = False

if __name__ == "__main__":
    run_parse("14.10.2020")