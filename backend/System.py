from backend.DatabaseHelper import DatabaseHelper

class System:
    db = DatabaseHelper()
    loginType = ''
    
    def login(self, regno, password, login_type):
        """
        Logs the user into the system
        """
        print('Login called')
        self.loginType = login_type

        try:
            credentials = self.db.getLoginCredentials(regno, login_type)
            print(credentials)
        except:
            return False

        if regno == credentials['regno'] and password == credentials['password']:
            return True
        return False