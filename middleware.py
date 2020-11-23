import eel
from backend.System import System
from backend.Staff import Staff
from backend.Student import Student
from backend.Admin import Admin

eel.init('ui')

sys = System()

@eel.expose
def login(username, password, login_type):
    isValid = sys.login(username, password, login_type)
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

    if success:
        return True
    else:
        return False
    return True

@eel.expose
def viewDetails(detailType, regno):
    admin = Admin()
    data = admin.viewDetails(detailType, regno)
    print('Requested data')
    print(data)
    return data

eel.start('login.html')