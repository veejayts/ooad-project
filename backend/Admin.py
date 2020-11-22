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
        try:
            self.db.execute(f'INSERT INTO student(regno, name, d_o_b, attendance, maths, science, computer, english, marks_percentage) VALUES ({regno}, {name}, {d_o_b}, 0, 0, 0, 0, 0, 0)')
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
            self.db.execute(f'INSERT INTO student(regno, password, name) VALUES (:regno, :password, :name)', staffData)
            return True
        except Exception:
            return False
        