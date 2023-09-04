import random;
from faker import Faker;
from dbConnection import db;
from config import TABLE;

fake = Faker()

num_records = 10  

cursor = db.cursor()

def areStock(stock):
    if(stock == 0):
        return True
    else: 
        return False

stock = random.randint(0, 100)

for _ in range(num_records):
    author = fake.name()
    title = fake.sentence(nb_words=4, variable_nb_words=True)
    description = fake.paragraph()
    stock = stock
    isAvaliable = areStock(stock)

    sql = f"INSERT INTO {TABLE} (author, title, description, stock, isAvaliable) VALUES ('{author}', '{title}', '{description}', {stock}, {isAvaliable});"

    cursor.execute(sql)

db.commit()

db.close()