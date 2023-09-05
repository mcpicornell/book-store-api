import random;
from faker import Faker;
from dbConnection import db;
from config import TABLE;

fake = Faker()

num_records = 10  

cursor = db.cursor()

def areStock(stock):
    if(stock == 0):
        return False
    else: 
        return True

for _ in range(num_records):
    stock = random.randint(0, 100)
    if(stock):
        author = fake.name()
        title = fake.sentence(nb_words=4, variable_nb_words=True)
        description = fake.paragraph()
        isAvaliable = areStock(stock)

    sql = f"INSERT INTO {TABLE} (author, title, description, stock, isAvaliable) VALUES ('{author}', '{title}', '{description}', {stock}, {isAvaliable});"

    cursor.execute(sql)

db.commit()

db.close()