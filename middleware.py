import eel
from backend.System import System

eel.init('ui')

@eel.expose
def login(username, password, login_type):
    sys = System()
    isValid = sys.login(username, password, login_type)
    return isValid

eel.start('index.html')