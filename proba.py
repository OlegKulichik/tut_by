import psycopg2


con = psycopg2.connect(
  database="tut_proba", 
  user="postgres", 
  password="123456", 
  host="localhost", 
  port="5432"
)



print("Database opened successfully")
cur = con.cursor()
# cur.execute('CREATE SEQUENCE rubric_id_seq;')
cur.execute('''CREATE TABLE rubrics (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) UNIQUE NOT NULL
  );''')
# cur.execute('CREATE SEQUENCE news_id_seq;')
cur.execute('''CREATE TABLE news (
	id	SERIAL PRIMARY KEY,
	head	VARCHAR(256) NOT NULL,
	text	TEXT NOT NULL,
	link	TEXT NOT NULL,
	date	DATE NOT NULL,
	rubric_id	INTEGER NOT NULL
);''')

cur.execute('ALTER TABLE news ADD FOREIGN KEY (rubric_id) REFERENCES public.rubrics(id) ON DELETE CASCADE;')

print("Table created successfully")
con.commit()  
con.close()