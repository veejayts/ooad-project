from backend.DatabaseHelper import DatabaseHelper

class System:
    systemno = 1
    password = 'password'

    db = DatabaseHelper()
    loginType = ''
    
    def login(self, regno, password, login_type):
        """
        Logs the user into the system
        """
        self.loginType = login_type
        login_type = login_type.lower()

        if (login_type != 'staff'):
            regno = int(regno)

        credentials = self.db.getLoginCredentials(regno, login_type)

        if regno == credentials['regno'] and password == credentials['password']:
            return True
        return False