from backend.DatabaseHelper import DatabaseHelper

class Admin:
    db = DatabaseHelper()
    id = 0
    password = ''
    
    def enterStudentDetails(self, regno, name, d_o_b):
        """
        Enters new student details in the database
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """

        try:
            student_data = {
                'regno': int(regno),
                'name': name,
                'password': f'student{regno}',
                'd_o_b': d_o_b
            }
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
                    'name': record[1],
                    'id': record[0]
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
            return True
        except:
            return False

    def getNotices(self):
        """
        :returns: All notices present
        """
        return self.db.getAll('SELECT * FROM notice')

    def updateDetails(self, name, regno, dob, attendance, maths, english, computer, percentage):
        """
        Updates details of existing students
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """
        student_data = {
            'name': name,
            'regno': regno,
            'dob': dob, 
            'attendance': attendance, 
            'maths': maths, 
            'english': english, 
            'computer': computer, 
            'percentage': percentage
        }

        try:
            self.db.execute('UPDATE student SET name = :name, d_o_b = :dob, attendance = :attendance, maths_marks = :maths, english_marks = :english, computer_marks = :computer, percentage_marks = :percentage WHERE regno = :regno', student_data)
            return True
        except:
            return False
        
    def updateMarks(self, name, regno, dob, attendance, maths, english, computer, percentage):
        """
        Updates details of existing students
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """
        student_data = {
            'regno': regno,
            'maths': maths, 
            'english': english, 
            'computer': computer, 
            'percentage': percentage
        }

        try:
            self.db.execute('UPDATE student SET maths_marks = :maths, english_marks = :english, computer_marks = :computer, percentage_marks = :percentage WHERE regno = :regno', student_data)
            return True
        except:
            return False
    
    def logout(self):
        """
        Logs out the user
        """
        print('Logged out of Admin')