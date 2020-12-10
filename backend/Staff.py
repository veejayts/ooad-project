from backend.DatabaseHelper import DatabaseHelper

class Staff:
    db = DatabaseHelper()

    def __init__(self):
        pass
    
    def updateDetails(self, name, regno, dob, department, sem):
        """
        Updates details of existing students
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """
        student_data = {
            'name': name,
            'regno': regno,
            'dob': dob,
            'department': department,
            'sem': sem
        }

        try:
            self.db.execute('UPDATE student SET name = :name, dob = :dob, department = :department, sem = :sem WHERE regno = :regno', student_data)
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
    
    def getDepartment(self, regno):
        """
        :returns: Department of the student
        """
        record = self.db.getAll(f'SELECT department FROM staff WHERE regno = "{regno}"')
        return record[0][0]
    
    def getSubjectCodes(self, department, sem):
        """
        :returns: Subject codes of the particular department
        """
        record = self.db.getAll('SELECT subcode FROM subjects WHERE department = :department AND sem = :sem', {'department': department, 'sem': sem})
        record = [i[0] for i in record]
        return record

    def getStudentsInSem(self, department, sem, type, subcode):
        """
        :returns: Student regnos of the particular sem
        """
        record = self.db.getAll('SELECT regno, marks FROM marks WHERE sem = :sem AND type = :type AND subcode = :subcode', {'department': department, 'sem': sem, 'type': type, 'subcode': subcode})
        return record

    def setMarks(self, department, sem, type, subcode, data):
        """
        :returns: True if Updation of marks was successful else returns False
        """
        student_data = {
            'type': type,
            'subcode': subcode,
            'sem': sem,
            'department': department
        }
        for mark in data:
            self.db.execute(f'UPDATE marks SET marks = {mark[1]} WHERE department = :department AND type = :type AND sem = :sem AND subcode = :subcode AND regno = {mark[0]}', student_data)
        return True

    def getAttendance(self, regno, department, sem):
        """
        :returns: attendance of the requested student
        """
        record = self.db.getAll(f'SELECT subcode, attendance FROM attendance WHERE regno = {regno} AND sem = {sem}')
        return record

    def getSubjectAttendance(self, sem, subcode):
        """
        :returns: attendance of the requested subject
        """
        record = self.db.getAll(f'SELECT regno, attendance FROM attendance WHERE subcode = "{subcode}" AND sem = {sem}')
        return record
    
    def setAttendance(self, sem, data, subcode):
        """
        :returns: True if Updation of marks was successful else returns False
        """
        student_data = {
            'type': type,
            'subcode': subcode,
            'sem': sem,
        }
        for attendance in data:
            self.db.execute(f'UPDATE attendance SET attendance = {attendance[1]} WHERE sem = :sem AND subcode = :subcode AND regno = {attendance[0]}', student_data)
        return True

    def logout(self):
        """
        Logs out the user
        """
        print('Logged out of Staff')
