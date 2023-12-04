#Milestone 3

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "dba",
    "password": "groupproject",
    "host": "127.0.0.1",
    "database": "Willson",
    "raise_on_warnings": True
}

clientNum = 0
total = 0

try:
    db = mysql.connector.connect(**config)
    query5 = db.cursor()

    print("\n Database user {} to connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))
    
    query1 = db.cursor()
    query2 = db.cursor()
    query3 = db.cursor()
    
    print("\n\n-- DISPLAYING AVERAGE AMOUNT OF ASSETS OF ALL CLIENTS --\n")
    
    query1.execute("SELECT account_balance FROM account")
    counter1 = query1.fetchall()
    for average in counter1:
        iaverage = average[0]
        total += iaverage
        clientNum += 1
    total = total / clientNum
    print(f"The average amount of assets for the entire client list is: ${total}")
    
    print("\n\n-- DISPLAYING NUMBER OF CLIENTS WITH 10+ TRANSACTIONS IN A MONTH --\n")
    
    query2.execute("SELECT COUNT(client.client_id),client_first_name,client_last_name FROM transaction INNER JOIN account ON transaction.account_id = account.account_id \
        INNER JOIN client ON account.client_id = client.client_id GROUP BY client.client_id")
    counter2 = query2.fetchall()
    for counter in counter2:
        if counter[0] > 9:
            print("{} {} has over {} transactions overall.".format(counter[1],counter[2],counter[0]))
        else:
            print("No clients have over 10 transactions in a month.")
    
    print("\n\n-- DISPLAYING NUMBER OF CLIENTS ADDED WITHIN THE LAST 6 MONTHS --\n")
    
    query3.execute("SELECT MONTH(client.client_join_date),COUNT(*) FROM client GROUP BY MONTH(client_join_date) ORDER BY MONTH(client_join_date)")
    counter3 = query3.fetchall()
    for add in counter3:
        print("{} client(s) has been added in the {}th month of 2023".format(add[1],add[0]))
    
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()