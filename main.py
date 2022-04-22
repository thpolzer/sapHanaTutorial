# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import platform
from hdbcli import dbapi



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print("Platform architecture: " + platform.architecture()[0])
    conn = dbapi.connect(
        address='192.168.32.3',
        port='39013',
        user='SYSTEM',
        password='Ich.bin.52'
    )
    print('connected')

    cursor = conn.cursor()
    sql_command = "SELECT * FROM DEV.STOCKPRICES;"
    cursor.execute(sql_command)
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print("%s" % col, end=" ")
        print("  ")
    cursor.close()
    print("\n")

    # Prepared statement example
    sql_command2 = "call DEV.__00_TEST_PASSSCALAR(?);"
    #parameters = [11, "2020-12-24"]
    parameters = [0]
    cursor.execute(sql_command2, parameters)
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print("%s" % col, end=" ")
        print(" ")
    cursor.close()
    conn.close()

    sql_command3 = "call DEV.__03_TEST_WHILELOOPPROCEDURE(?);"
    #parameters = [11, "2020-12-24"]
    parameters = ['?']
    cursor.execute(sql_command3, parameters)
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print("%s" % col, end=" ")
        print(" ")
    cursor.close()
    conn.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
