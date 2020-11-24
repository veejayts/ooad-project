from backend.DatabaseHelper import DatabaseHelper

class Student:
    regno = 0
    name = ''
    attendance = 0
    d_o_b = 0
    db = DatabaseHelper()

    def __init__(self, regno):
        self.regno = regno

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
    
    def logout(self):
        """
        Logs out the user
        """
        print('Logged out of Student')