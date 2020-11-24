import sqlite3
import os

# Create DB file if not present already in the same directory
if not (os.path.isfile('sis.db')):
    """
    Tables initialised:
        - student
        - staff
        - admin
        - notice
    """
    with open('sis.db', 'w') as f:
        conn = sqlite3.connect('sis.db')
        c = conn.cursor()

        c.execute('CREATE TABLE student (regno INT PRIMARY_KEY, name TEXT, password TEXT, d_o_b TEXT, attendance INT, maths_marks INT, computer_marks INT, english_marks INT, percentage_marks INT)')
        c.execute('CREATE TABLE staff (regno TEXT, name TEXT, password TEXT)')
        c.execute('CREATE TABLE admin (regno INT, password TEXT)')
        c.execute('CREATE TABLE notice (notice TEXT)')

        conn.commit()

        c.execute('INSERT INTO admin (regno, password) VALUES (12345, "password")')

        conn.commit()
        conn.close()

class DatabaseHelper:
    conn = sqlite3.connect('sis.db')
    c = conn.cursor()

    def __init__(self):
        self.__closeDbConnection()
    
    def __openDbConnection(self):
        """
        Opens the connection to database
        """
        self.conn = sqlite3.connect('sis.db')
        self.c = self.conn.cursor()
    
    def __closeDbConnection(self):
        """
        closes the connection to database
        """
        self.conn.close()
    
    def execute(self, query, data={}):
        """
        Executes the query passed to the function
        """
        self.__openDbConnection()
        if data != {}:
            self.c.execute(query, data)
        else:
            self.c.execute(query)
        self.conn.commit()
        self.__closeDbConnection()
    
    def getAll(self, select_query):
        """
        Returns the records for the SELECT query passed
        """
        self.__openDbConnection()
        self.c.execute(select_query)
        records = self.c.fetchall()
        self.__closeDbConnection()
        return records
    
    def getLoginCredentials(self, regno, login_type):
        """
        :returns: regno and password of required user
        """
        self.__openDbConnection()
        self.c.execute(f'SELECT regno, password FROM {login_type} WHERE regno = :regno', {
            'regno': regno
        })
        record = self.c.fetchall()
        record = {'regno': record[0][0], 'password': record[0][1]}
        self.__closeDbConnection()
        return record

# db = DatabaseHelper()
# print(db.getAll('SELECT * FROM admin'))