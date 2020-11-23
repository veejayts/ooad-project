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

        self.db.execute('UPDATE student SET name = :name, d_o_b = :dob, attendance = :attendance, maths_marks = :maths, english_marks = :english, computer_marks = :computer, percentage_marks = :percentage WHERE regno = :regno', student_data)

        return True