#Alejandro Quezada
#11/26/2023
#Module 7 - Assignment 7.2 - Movies: Table Queries

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Pa$$w0rd",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    print("\n\n Press any key to continue...")
    
    print("\nDISPLAYING Studio RECORDS:\n")
    query1 = db.cursor()
    query1.execute("SELECT studio_id, studio_name FROM studio")
    studios = query1.fetchall()
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

    print("\nDISPLAYING Genre RECORDS:\n")
    query2 = db.cursor()
    query2.execute("SELECT genre_id, genre_name FROM genre")
    genres = query2.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

    print("\nDISPLAYING Short Film RECORDS\n")
    query3 = db.cursor()
    query3.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120")
    films = query3.fetchall()
    for film in films:
        print("Genre ID: {}\nGenre Name: {}\n".format(film[0], film[1]))
    
    print("\nDISPLAYING Director RECORDS in Order:\n")
    query4 = db.cursor()
    query4.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films = query4.fetchall()
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    
    else:
        print(err)

        
finally:
    db.close()