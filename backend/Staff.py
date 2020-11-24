from backend.DatabaseHelper import DatabaseHelper

class Staff:
    db = DatabaseHelper()

    def __init__(self):
        print('Staff')
    
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
        
    def enterMarks(self, name, regno, dob, attendance, maths, english, computer, percentage):
        """
        Updates marks of existing students
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
    
    def view_marks(self, regno):
        """
        :returns: Marks of requested student
        """
        record = self.db.getAll(f'SELECT * FROM student WHERE regno = "{id}"')
        record = record[0]
        data = {
            'maths_marks': record[5],
            'computer_marks': record[6],
            'english_marks': record[7],
            'percentage_marks': record[8]
        }
        return data
    
    def viewDetails(self, regno):
        """
        :returns: Details of the student
        """
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
    
    def logout(self):
        """
        Logs out the user
        """
        print('Logged out of Staff')
