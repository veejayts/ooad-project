from backend.DatabaseHelper import DatabaseHelper

class Admin:
    db = DatabaseHelper()

    def __init__(self):
        print('Admin instantiated')
    
    def enterStudentDetails(self, regno, name, d_o_b):
        """
        Enters new student details in the database
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """
        student_data = {
            'regno': regno,
            'name': name,
            'password': f'student{regno}',
            'd_o_b': d_o_b
        }
        try:
            self.db.execute('INSERT INTO student(regno, password, name, d_o_b) VALUES (:regno, :password, :name, :d_o_b)', student_data)
            return True
        except Exception:
            return False
        
    def enterStaffDetails(self, regno, name):
        """
        Enters new staff details in the database
        :returns: True if insertion of staff details was successful. False if the operation was not successful.
        """
        staffData = {
            'regno': regno,
            'password': f'staff{regno}',
            'name': name
        }
        try:
            self.db.execute(f'INSERT INTO staff (regno, password, name) VALUES (:regno, :password, :name)', staffData)
            return True
        except Exception:
            return False
        
    def viewDetails(self, detailType, id):
        """
        :returns: A dictionary containing the information of the requested student or staff
        """
        try:
            if detailType == 'Student':
                record = self.db.getAll(f'SELECT * FROM student WHERE regno = "{id}"')
                record = record[0]
                data = {
                    'regno': record[0],
                    'name': record[1],
                    'dob': record[3],
                    'attendance': record[4],
                    'maths_marks': record[5],
                    'computer_marks': record[6],
                    'english_marks': record[7],
                    'percentage_marks': record[8]
                }
                return data
            else:
                record = self.db.getAll(f'SELECT * FROM staff WHERE regno = "{id}"')
                record = record[0]
                data = {
                    'id': record[0],
                    'name': record[1]
                }
                return data
        except:
            return False
        
    def updateNotice(self, notice):
        """
        Enters new notice into the database
        """
        try:
            self.db.execute(f'INSERT INTO notice (notice) VALUES ("{notice}")')
            print('updated notice')
            return True
        except:
            print('error')
            return False

    def getNotices(self):
        """
        :returns: All notices present
        """
        return self.db.getAll('SELECT * FROM notice')