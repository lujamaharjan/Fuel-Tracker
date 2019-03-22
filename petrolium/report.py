"""
    This file is the main file which
    generates the fuel report by fetching
    data from database
"""
import sqlite3
import dbmanagement as db

def generateReport():
    db.dbCreationAndInsertion() # call function from dbmanagement.py file
    conn = sqlite3.connect('fueldata.db')
    cursor = conn.cursor()

    # fetching latest year from db
    cursor.execute('SELECT max(year) FROM fueldata')
    maxYear = cursor.fetchone()
    max = int(maxYear[0])

    #fetching oldest year from db
    cursor.execute('SELECT min(year) FROM fueldata')
    minYear = cursor.fetchone()
    min = int(minYear[0])

    #fetching all unique petroleum_product name form db
    cursor.execute('SELECT petroleum_product FROM fueldata')
    product = cursor.fetchall()
    product = list(set(product))


    print('Year \t\t Min \t Max \t Avg \t\t product')


    # Here we loop through all the unique product
    # let us not forget product is list which includes tuple
    # But tuples are unique i.e each tuple represent each product
    x = min
    for item in product:
        for innerItem in item:
            for y in range(max,min,-5):

                # fetching min sale value from db
                cursor.execute('''SELECT min(sale) FROM fueldata WHERE year>=?
                    AND year < ? AND petroleum_product = ?''',(x,x+5,innerItem))
                minSale = cursor.fetchone()

                # fetching max sale value from db
                cursor.execute('''SELECT max(sale) FROM fueldata WHERE year>=?
                    AND year < ? AND petroleum_product = ?''',(x,x+5,innerItem))
                maxSale = cursor.fetchone()

                # fetching avg sale value from db
                cursor.execute('''SELECT avg(sale) FROM fueldata WHERE year>=?
                    AND year < ? AND petroleum_product = ?''',(x,x+5,innerItem))
                avgSale = cursor.fetchone()

                print('{}-{} \t{}\t {}\t {} \t {}'.format(x,x+4,minSale[0],maxSale[0],avgSale[0],innerItem))

                x = x+5 # these are changing the year
                if(x >= max):
                    x = min

def main():
    generateReport()
if __name__ == '__main__':
    main()
