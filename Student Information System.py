import eel
from backend.System import System
from backend.Staff import Staff
from backend.Student import Student
from backend.Admin import Admin

eel.init('ui')

sys = System()
global id
global isLoggedIn
global department

@eel.expose
def login(username, password, login_type):
    isValid = False
    try:
        isValid = sys.login(username, password, login_type)
        global id
        global isLoggedIn
        global department

        if login_type == 'Student':
            department = Student().getDepartment(int(username))
        elif login_type == 'Staff':
            department = Staff().getDepartment(username)
        id = username
        isLoggedIn = True
    except:
        isLoggedIn = False
    return isValid

@eel.expose
def getLoginType():
    return sys.loginType

@eel.expose
def enterDetails(detailType, sId='', name='', dob='', dep='', sem=1):
    admin = Admin()
    if detailType == 'Student':
        success = admin.enterStudentDetails(sId, name, dob, dep, sem)
    elif detailType == 'Staff':
        print(dep)
        success = admin.enterStaffDetails(sId, name, dep)
    return success

@eel.expose
def viewDetails(detailType, regno):
    admin = Admin()
    data = admin.viewDetails(detailType, regno)
    return data

@eel.expose
def updateNotice(notice):
    admin = Admin()
    success = admin.updateNotice(notice)
    return success

@eel.expose
def getNotices():
    admin = Admin()
    data = admin.getNotices()
    data.reverse()
    return data

@eel.expose
def updateDetails(name, regno='', dob='', department='', sem=1):
    staff = Staff()
    success = staff.updateDetails(name, regno, dob, department, sem)
    return success

@eel.expose
def getSemMarks(regno, department, sem):
    admin = Admin()
    data = admin.getSemMarks(regno, department, sem)
    return data

@eel.expose
def getSubjectCodes(sem):
    staff = Staff()
    subcodes = staff.getSubjectCodes(department, int(sem))
    return subcodes

@eel.expose
def getStudentsInSem(sem, type, subcode):
    staff = Staff()
    students = staff.getStudentsInSem(department, int(sem), type, subcode)
    return students

@eel.expose
def setMarks(sem, data, type, subcode):
    staff = Staff()
    success = staff.setMarks(department, int(sem), type, subcode, data)
    return success

@eel.expose
def getAllMarks(regno = -1, sem = 1, type = 'CAT1'):
    student = Student()
    global id
    if regno != -1:
        data = student.getAllMarks(regno, department, sem, type)
    else:
        data = student.getAllMarks(id, department, sem, type)
    return data

@eel.expose
def getAttendance(regno = -1, sem = 1):
    staff = Staff()
    global id
    if regno != -1:
        data = staff.getAttendance(regno, department, sem)
    else:
        data = staff.getAttendance(id, department, sem)
    return data

@eel.expose
def getSubjectAttendance(sem, subcode):
    staff = Staff()
    data = staff.getSubjectAttendance(int(sem), subcode)
    return data

@eel.expose
def setAttendance(sem, data, subcode):
    staff = Staff()
    success = staff.setAttendance(int(sem), data, subcode)
    return success


@eel.expose
def getRegno():
    global id
    return id

@eel.expose
def getLoginStatus():
    global isLoggedIn
    return isLoggedIn

@eel.expose
def logout():
    global isLoggedIn
    isLoggedIn = False


eel.start('login.html')