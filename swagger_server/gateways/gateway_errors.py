'''''
Gateway not connected or session invalidated in some form
'''''
class InvalidSessionError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Account does not exist for this gateway
'''''
class InvalidAccountError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Account exists but is not permissioned for this action
'''''
class AccountPermissionError(Exception):
    def __init__(self, msg):
        self.msg = msg

'''''
Order paramters are not valid
'''''
class OrderValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg
