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

        c.execute('CREATE TABLE student (regno INT PRIMARY_KEY, name TEXT, password TEXT, dob TEXT, department TEXT, sem INT)')
        c.execute('CREATE TABLE marks (regno INT, type TEXT, subcode TEXT, marks INT, department TEXT, sem INT)')
        c.execute('CREATE TABLE attendance (regno INT, subcode TEXT, attendance INT, sem INT)')
        c.execute('CREATE TABLE staff (regno TEXT, name TEXT, password TEXT, department TEXT)')
        c.execute('CREATE TABLE subjects (id INT, subname TEXT, subcode TEXT, department TEXT, sem INT)')
        c.execute('CREATE TABLE admin (regno INT, password TEXT)')
        c.execute('CREATE TABLE studenthistory (regno INT, title TEXT, description TEXT)')
        c.execute('CREATE TABLE notice (notice TEXT)')

        conn.commit()

        c.execute('INSERT INTO admin (regno, password) VALUES (123, "123")')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS1", "cs", 1)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS2", "cs", 1)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS3", "cs", 2)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS4", "cs", 3)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS5", "cs", 4)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS6", "cs", 5)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS7", "cs", 6)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "css1", "CS9", "cs", 8)')
        c.execute('INSERT INTO subjects (id, subname, subcode, department, sem) VALUES (1, "eces1", "ECE5", "ece", 5)')

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
    
    def getAll(self, select_query, data={}):
        """
        Returns the records for the SELECT query passed
        """
        self.__openDbConnection()
        if data == {}:
            self.c.execute(select_query)
        else:
            self.c.execute(select_query, data)
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
# print(db.getAll('select * from student'))