from backend.DatabaseHelper import DatabaseHelper

class Admin:
    db = DatabaseHelper()
    id = 0
    password = ''
    
    def enterStudentDetails(self, regno, name, d_o_b, department, sem):
        """
        Enters new student details in the database
        :returns: True if insertion of student details was successful. False if the operation was not successful.
        """
        # try:
        student_data = {
            'regno': int(regno),
            'name': name,
            'password': f'student{regno}',
            'd_o_b': d_o_b,
            'department': department,
            'sem': sem
        }

        # Checking if student already exists
        rec = self.db.getAll('SELECT regno FROM student WHERE regno = :regno', {'regno': int(regno)})
        if len(rec) >= 1:
            return False

        self.db.execute('INSERT INTO student(regno, password, name, dob, department, sem) VALUES (:regno, :password, :name, :d_o_b, :department, :sem)', student_data)

        for i in range(1, 9):
            subcodes = self.db.getAll(f'SELECT subcode FROM subjects WHERE department = :department AND sem = {i}', {'department': department})
            subcodes = [sub[0] for sub in subcodes]

            for sub in subcodes:
                self.db.execute(f'INSERT INTO marks (regno, type, subcode, marks, department, sem) VALUES (:regno, "SEM", "{sub}", 0, :department, {i})', student_data)
                self.db.execute(f'INSERT INTO attendance (regno, subcode, attendance, sem) VALUES (:regno, "{sub}", 0, {i})', student_data)
                for exam in ['CAT1', 'CAT2', 'CAT3']:
                    self.db.execute(f'INSERT INTO marks (regno, type, subcode, marks, department, sem) VALUES (:regno, "{exam}", "{sub}", 0, :department, {i})', student_data)
        return True
        # except Exception:
        #     return False
        
    def enterStaffDetails(self, regno, name, department):
        """
        Enters new staff details in the database
        :returns: True if insertion of staff details was successful. False if the operation was not successful.
        """
        staffData = {
            'regno': regno,
            'password': f'staff{regno}',
            'name': name,
            'department': department
        }
        try:
            # Checking if staff already exists
            rec = self.db.getAll('SELECT regno FROM staff WHERE regno = :regno', {'regno': int(regno)})
            if len(rec) >= 1:
                return False
            self.db.execute(f'INSERT INTO staff (regno, password, name, department) VALUES (:regno, :password, :name, :department)', staffData)
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
                    'department': record[4],
                    'sem': record[5]
                }
                return data
            else:
                record = self.db.getAll(f'SELECT * FROM staff WHERE regno = "{id}"')
                record = record[0]
                data = {
                    'name': record[1],
                    'id': record[0],
                    'department': record[3]
                }
                return data
        except:
            return False
        
    def getSemMarks(self, regno, department, sem):
        """
        :returns: A list of lists containing the marks of the particular sem of the requested student
        """
        record = self.db.getAll('SELECT * FROM marks WHERE regno = :regno AND sem = :sem', {
            'regno': regno,
            'sem': sem
        })
        return record
        
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
            self.db.execute('UPDATE student SET name = :name, dob = :dob, attendance = :attendance, maths_marks = :maths, english_marks = :english, computer_marks = :computer, percentage_marks = :percentage WHERE regno = :regno', student_data)
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