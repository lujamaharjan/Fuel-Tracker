import sqlite3
import call_api

def dbCreationAndInsertion():
    # below is url to fetch json data we store url in link variable
    link = 'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json'

    # connect int with fueldata which is our database
    conn = sqlite3.connect('fueldata.db')

    #cursor help to track sql operations
    cursor = conn.cursor()

    # try block runs if and only if the program is run for first time i.e
    # when ther is no database name fueldata other wise excep block runs
    try:
        cursor.execute('''CREATE TABLE fueldata(
                        ID integer primary key Autoincrement,
                        year text,
                        petroleum_product text,
                        sale int)''')

    except sqlite3.OperationalError:
        print('Loading ...')

    else:
        # featching a data
        data = call_api.fetchJsonData(link)
        # looping through all dictionary in the list and storing to database
        for dictt in data:
            y = str(dictt['year'])
            p = str(dictt['petroleum_product'])
            s = int(dictt['sale'])
            params = (y,p,s)
            #using params to insert and update operation gives us extra security
            cursor.execute('INSERT INTO fueldata VALUES (NULL,?,?,?)',params)
            # for making SQL operation permanet we use commit
            conn.commit()

    finally:
        cursor.close()
        conn.close()
