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

try:
    db = mysql.connector.connect(**config)
    query5 = db.cursor()

    print("\n Database user {} to connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))
    
    print("\n\n-- DISPLAYING transaction RECORDS --")

    query5.execute("SELECT transaction_id, transaction_type_name, transaction_amount, transaction_date, transaction_time, client_first_name, client_last_name FROM transaction INNER JOIN transaction_type ON transaction.transaction_type_id=transaction_type.transaction_type_id \
        INNER JOIN account ON account.account_id=transaction.transaction_id INNER JOIN client ON account.client_id=client.client_id")
    transactions = query5.fetchall()
    for transaction in transactions:
        amount = float(transaction[2])
        amountString = "{:.2f}".format(amount)
        print("\nTransaction ID: {}\nType: {}\nAmount: ${}\nDate: {}\nTime: {}\nAccount Owner: {} {}".format(transaction[0],transaction[1],amountString,transaction[3],transaction[4],transaction[5],transaction[6]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()