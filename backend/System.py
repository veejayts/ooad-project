from backend.DatabaseHelper import DatabaseHelper

class System:
    db = DatabaseHelper()

    def __init__(self):
        pass
    
    def login(self, regno, password, login_type):
        """
        Logs the user into the system
        """
        print('Login called')
        credentials = self.db.getLoginCredentials(regno, login_type)

        if regno == credentials['regno'] and password == credentials['password']:
            return True
        return False