import eel
from backend.System import System
from backend.Staff import Staff
from backend.Student import Student
from backend.Admin import Admin

eel.init('ui')

sys = System()
global id
global isLoggedIn

@eel.expose
def login(username, password, login_type):
    isValid = False
    try:
        isValid = sys.login(username, password, login_type)
        global id
        global isLoggedIn
        id = username
        isLoggedIn = True
    except:
        isLoggedIn = False
    return isValid

@eel.expose
def getLoginType():
    return sys.loginType

@eel.expose
def enterDetails(detailType, id='', name='', dob=''):
    admin = Admin()
    if detailType == 'Student':
        success = admin.enterStudentDetails(id, name, dob)
    elif detailType == 'Staff':
        success = admin.enterStaffDetails(id, name)
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
def updateDetails(name, regno, dob, attendance, maths, english, computer, percentage):
    staff = Staff()
    success = staff.updateDetails(name, regno, dob, attendance, maths, english, computer, percentage)
    return success

@eel.expose
def getRegno():
    return id

@eel.expose
def getLoginStatus():
    return isLoggedIn

@eel.expose
def logout():
    global isLoggedIn
    isLoggedIn = False


eel.start('login.html')