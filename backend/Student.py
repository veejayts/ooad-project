from backend.DatabaseHelper import DatabaseHelper

class Student:
    regno = 0
    name = ''
    attendance = 0
    d_o_b = 0
    db = DatabaseHelper()

    def viewDetails(self, regno):
        """
        :returns: Details of the student
        """
        record = self.db.getAll(f'SELECT * FROM student WHERE regno = "{regno}"')
        record = record[0]
        data = {
            'regno': record[0],
            'name': record[1],
            'dob': record[3],
            'department': record[4],
            'sem': record[5]
        }
        return data
    
    def view_marks(self, regno):
        """
        :returns: Marks of requested student
        """
        record = self.db.getAll(f'SELECT * FROM student WHERE regno = {regno}')
        record = record[0]
        data = {
            'maths_marks': record[5],
            'computer_marks': record[6],
            'english_marks': record[7],
            'percentage_marks': record[8]
        }
        return data
    
    def getDepartment(self, regno):
        """
        :returns: Department of the student
        """
        record  = self.viewDetails(regno)
        return record['department']

    def getAllMarks(self, regno, department, sem, type):
        """
        :returns: Marks of all requested sem of the student
        """
        record = self.db.getAll(f'SELECT subcode, marks FROM marks WHERE regno = {regno} AND department = "{department}" AND sem = {sem} AND type = \'{type}\'')
        return record

    def logout(self):
        """
        Logs out the user
        """
        print('Logged out of Student')