from datetime import date, timedelta
import os
import json
import psycopg2

con = psycopg2.connect(
  database="tut_proba", 
  user="postgres", 
  password="123456", 
  host="localhost", 
  port="5432"
)
cur = con.cursor()
print("Database opened successfully")

def db2 (tut_by, date):
    for news in tut_by:
            cur.execute(
                "INSERT INTO rubrics (name) VALUES ('{}') ON CONFLICT (name) DO NOTHING;".format(news["rubric"])
                )
            for i in news['news']:
                cur.execute(
                    """INSERT INTO news (head, text, link, date, rubric_id) VALUES
                    ('{}', '{}', '{}', '{}',(SELECT id FROM rubrics WHERE name = '{}'));""".format(i["head"],i['text'],i['link'],date,news["rubric"])
                )
    con.commit()