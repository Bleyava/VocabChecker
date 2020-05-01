import mysql.connector as db
import random as random

connection = db.connect(user="root",  database="vocabs3")
cursor = connection.cursor()
cursor.execute("SELECT english, german FROM vocabulary")
vocabs = cursor.fetchall()
while 1:
    vocab = random.choice(vocabs)
    print(vocab[0])

    german = []

    if "," in vocab[1]:
        german = vocab[1].split(", ")
    else:
        german.append(vocab[1])

    res = 0

    inp = input()

    for ger in german:
        if inp == ger:
            res = 1

    if res == 1:
        print("right")

        print("UPDATE vocabulary SET correct = correct + 1 WHERE german='" + vocab[1] + "' AND english='" +
              vocab[0] + "'")

        cursor.execute("UPDATE vocabulary SET correct = correct + 1 WHERE german='"
                       + vocab[1] + "' AND english='" + vocab[0] + "'")
        connection.commit()
    else:
        print(german)
        
    print("")